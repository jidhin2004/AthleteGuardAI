/**
 * AthleteGuard AI - Admin Dashboard JavaScript Controller
 */

let riskChartInstance = null;

document.addEventListener('DOMContentLoaded', function () {
  fetchAdminStats();

  // Mobile sidebar toggle handler
  const sidebarToggle = document.getElementById('sidebarToggle');
  const appSidebar = document.getElementById('appSidebar');
  if (sidebarToggle && appSidebar) {
    sidebarToggle.addEventListener('click', function () {
      appSidebar.classList.toggle('show');
    });
  }
});

function fetchAdminStats() {
  const loadingEl = document.getElementById('adminLoadingState');
  const errorEl = document.getElementById('adminErrorState');
  const contentEl = document.getElementById('adminDashboardContent');

  if (loadingEl) loadingEl.style.display = 'block';
  if (errorEl) errorEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'none';

  fetch('/api/admin/stats')
    .then(response => {
      if (!response.ok) throw new Error(`HTTP error ${response.status}`);
      return response.json();
    })
    .then(data => {
      if (data.status !== 'success') {
        throw new Error(data.message || 'Server error');
      }

      if (loadingEl) loadingEl.style.display = 'none';
      if (contentEl) contentEl.style.display = 'block';

      // Update Statistic Cards
      document.getElementById('statTotalAthletes').textContent = data.stats.total_athletes;
      document.getElementById('statHealthRecords').textContent = data.stats.total_health_records;
      document.getElementById('statTotalPredictions').textContent = data.stats.total_predictions;
      document.getElementById('statHighRisk').textContent = data.stats.high_risk_count;

      // Render Risk Doughnut Chart
      renderRiskChart(data.risk_distribution);

      // Render Tables
      renderRecentAthletes(data.recent_athletes);
      renderRecentPredictions(data.recent_predictions);
    })
    .catch(err => {
      console.error('Admin Dashboard Fetch Error:', err);
      if (loadingEl) loadingEl.style.display = 'none';
      if (errorEl) errorEl.style.display = 'block';
    });
}

function renderRiskChart(distData) {
  const ctx = document.getElementById('adminRiskDistributionChart');
  if (!ctx) return;

  if (riskChartInstance) {
    riskChartInstance.destroy();
  }

  const total = distData.counts.reduce((a, b) => a + b, 0);
  if (total === 0) {
    ctx.parentNode.innerHTML = `
      <div class="d-flex flex-column align-items-center justify-content-center h-100 text-muted">
        <i class="fa-solid fa-chart-pie fa-3x mb-2 text-slate-300"></i>
        <p class="fs-7 fw-semibold mb-0">No prediction records available.</p>
      </div>`;
    return;
  }

  riskChartInstance = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: distData.labels,
      datasets: [{
        data: distData.counts,
        backgroundColor: distData.colors,
        borderWidth: 2,
        borderColor: '#ffffff'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            usePointStyle: true,
            padding: 16,
            font: { family: 'Inter', size: 12, weight: '600' }
          }
        },
        tooltip: {
          callbacks: {
            label: function (context) {
              const val = context.raw || 0;
              const pct = total > 0 ? ((val / total) * 100).toFixed(1) : 0;
              return ` ${context.label}: ${val} (${pct}%)`;
            }
          }
        }
      },
      cutout: '70%'
    }
  });
}

function renderRecentAthletes(athletes) {
  const tbody = document.getElementById('recentAthletesTableBody');
  if (!tbody) return;

  if (!athletes || athletes.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="5" class="text-center py-4 text-muted fs-7">
          No athlete registrations found.
        </td>
      </tr>`;
    return;
  }

  tbody.innerHTML = athletes.map(a => `
    <tr>
      <td class="fw-bold text-primary">${a.athlete_id}</td>
      <td>
        <div class="fw-semibold text-dark">${escapeHtml(a.full_name)}</div>
        <div class="fs-8 text-muted">${escapeHtml(a.email)}</div>
      </td>
      <td><span class="badge bg-secondary-subtle text-dark fw-medium">${escapeHtml(a.primary_sport)}</span></td>
      <td class="fs-7 text-muted">${formatDate(a.created_at)}</td>
      <td class="text-center">
        <a href="/admin/athletes/${a.id}" class="btn btn-xs btn-outline-primary rounded-pill px-3 py-1 fw-bold fs-8">
          View Detail
        </a>
      </td>
    </tr>
  `).join('');
}

function renderRecentPredictions(preds) {
  const tbody = document.getElementById('recentPredictionsTableBody');
  if (!tbody) return;

  if (!preds || preds.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="6" class="text-center py-4 text-muted fs-7">
          No prediction records found.
        </td>
      </tr>`;
    return;
  }

  tbody.innerHTML = preds.map(p => `
    <tr>
      <td class="fw-semibold text-dark">${escapeHtml(p.athlete_name)}</td>
      <td><span class="badge bg-light text-dark border">${escapeHtml(p.athlete_sport)}</span></td>
      <td class="fs-7 text-muted">${p.record_date}</td>
      <td>${getBadgeHTML(p.risk_label)}</td>
      <td class="fw-bold fs-7">${p.risk_score !== null ? p.risk_score.toFixed(1) + '%' : 'N/A'}</td>
      <td class="text-center">
        <a href="/admin/athletes/${p.user_id}" class="btn btn-xs btn-outline-secondary rounded-pill px-3 py-1 fw-bold fs-8">
          Audit Athlete
        </a>
      </td>
    </tr>
  `).join('');
}

function getBadgeHTML(label) {
  if (!label) return '<span class="badge bg-secondary">Unknown</span>';
  const lower = label.toLowerCase();
  if (lower.includes('high')) {
    return `<span class="badge bg-danger-subtle text-danger border border-danger-subtle px-2.5 py-1 fw-bold"><i class="fa-solid fa-triangle-exclamation me-1"></i> HIGH RISK</span>`;
  } else if (lower.includes('medium')) {
    return `<span class="badge bg-warning-subtle text-warning-emphasis border border-warning-subtle px-2.5 py-1 fw-bold"><i class="fa-solid fa-circle-exclamation me-1"></i> MEDIUM RISK</span>`;
  }
  return `<span class="badge bg-success-subtle text-success border border-success-subtle px-2.5 py-1 fw-bold"><i class="fa-solid fa-circle-check me-1"></i> LOW RISK</span>`;
}

function formatDate(isoStr) {
  if (!isoStr) return 'N/A';
  try {
    const d = new Date(isoStr);
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  } catch (e) {
    return isoStr;
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
