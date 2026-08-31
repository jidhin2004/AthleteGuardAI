/**
 * AthleteGuard AI - Admin Global Predictions Controller
 */

let allPredictionsCache = [];

document.addEventListener('DOMContentLoaded', function () {
  fetchPredictionsLog();

  const searchInput = document.getElementById('predictionSearchInput');
  const riskFilter = document.getElementById('predictionRiskFilter');

  if (searchInput) {
    searchInput.addEventListener('input', filterPredictionsTable);
  }
  if (riskFilter) {
    riskFilter.addEventListener('change', filterPredictionsTable);
  }

  // Mobile sidebar toggle handler
  const sidebarToggle = document.getElementById('sidebarToggle');
  const appSidebar = document.getElementById('appSidebar');
  if (sidebarToggle && appSidebar) {
    sidebarToggle.addEventListener('click', function () {
      appSidebar.classList.toggle('show');
    });
  }
});

function fetchPredictionsLog() {
  const loadingEl = document.getElementById('predictionsLoadingState');
  const emptyEl = document.getElementById('predictionsEmptyState');
  const contentEl = document.getElementById('predictionsContentArea');

  if (loadingEl) loadingEl.style.display = 'block';
  if (emptyEl) emptyEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'none';

  fetch('/api/admin/predictions')
    .then(res => {
      if (!res.ok) throw new Error(`HTTP error ${res.status}`);
      return res.json();
    })
    .then(data => {
      if (data.status !== 'success') throw new Error(data.message);

      allPredictionsCache = data.records || [];

      if (loadingEl) loadingEl.style.display = 'none';
      filterPredictionsTable();
    })
    .catch(err => {
      console.error('Predictions Log Fetch Error:', err);
      if (loadingEl) loadingEl.style.display = 'none';
      if (emptyEl) {
        emptyEl.style.display = 'block';
        emptyEl.querySelector('h4').textContent = 'Unable to load predictions.';
      }
    });
}

function filterPredictionsTable() {
  const query = (document.getElementById('predictionSearchInput')?.value || '').trim().toLowerCase();
  const selectedRisk = (document.getElementById('predictionRiskFilter')?.value || 'all').toLowerCase();

  const filtered = allPredictionsCache.filter(p => {
    // Risk Filter
    if (selectedRisk !== 'all') {
      if (!(p.risk_label || '').toLowerCase().includes(selectedRisk)) {
        return false;
      }
    }

    // Search Filter
    if (query) {
      const match = (
        (p.athlete_name || '').toLowerCase().includes(query) ||
        (p.athlete_id || '').toLowerCase().includes(query) ||
        (p.primary_sport || '').toLowerCase().includes(query) ||
        (p.risk_label || '').toLowerCase().includes(query) ||
        (p.record_date || '').toLowerCase().includes(query)
      );
      if (!match) return false;
    }

    return true;
  });

  renderPredictionsTable(filtered);
}

function renderPredictionsTable(records) {
  const tbody = document.getElementById('predictionsTableBody');
  const emptyEl = document.getElementById('predictionsEmptyState');
  const contentEl = document.getElementById('predictionsContentArea');
  const badgeEl = document.getElementById('totalPredictionsBadge');

  if (badgeEl) {
    badgeEl.textContent = `${records.length} Prediction${records.length === 1 ? '' : 's'}`;
  }

  if (!records || records.length === 0) {
    if (contentEl) contentEl.style.display = 'none';
    if (emptyEl) emptyEl.style.display = 'block';
    return;
  }

  if (emptyEl) emptyEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'block';

  tbody.innerHTML = records.map(p => `
    <tr>
      <td>
        <a href="/admin/athletes/${p.user_id}" class="fw-bold text-dark text-decoration-none">
          ${escapeHtml(p.athlete_name)}
        </a>
        <div class="fs-8 text-primary font-mono">${p.athlete_id}</div>
      </td>
      <td><span class="badge bg-secondary-subtle text-dark">${escapeHtml(p.primary_sport)}</span></td>
      <td class="fs-7 text-muted fw-medium">${p.record_date}</td>
      <td>${getBadgeHTML(p.risk_label)}</td>
      <td class="fw-bold fs-7 text-primary">${p.risk_score !== null ? p.risk_score.toFixed(1) + '%' : 'N/A'}</td>
      <td class="fs-7 text-muted">${p.sleep_hours} hrs / ${p.training_hours} hrs</td>
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

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
