/**
 * AthleteGuard AI - Admin Athlete Detail Audit Controller
 */

let riskPieInstance = null;
let healthTrendInstance = null;

document.addEventListener('DOMContentLoaded', function () {
  const container = document.getElementById('athleteDetailContent');
  if (!container) return;

  const userId = container.getAttribute('data-user-id');
  if (userId) {
    fetchAthleteAuditDetail(userId);
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

function fetchAthleteAuditDetail(userId) {
  const loadingEl = document.getElementById('athleteDetailLoading');
  const contentEl = document.getElementById('athleteDetailContent');

  if (loadingEl) loadingEl.style.display = 'block';
  if (contentEl) contentEl.style.display = 'none';

  fetch(`/api/admin/athletes/${userId}`)
    .then(res => {
      if (!res.ok) throw new Error(`HTTP error ${res.status}`);
      return res.json();
    })
    .then(data => {
      if (data.status !== 'success') throw new Error(data.message);

      if (loadingEl) loadingEl.style.display = 'none';
      if (contentEl) contentEl.style.display = 'block';

      // Populate Summary Stat Cards
      renderSummaryCards(data.summary_stats);

      // Render Charts
      renderRiskPieChart(data.summary_stats);
      renderHealthTrendChart(data.trends);

      // Render Audit Sections
      renderMedicalHistory(data.medical_history);
      renderHealthRecords(data.health_records);
      renderPredictions(data.predictions);
    })
    .catch(err => {
      console.error('Athlete Audit Detail Fetch Error:', err);
      if (loadingEl) {
        loadingEl.innerHTML = `
          <div class="alert alert-danger border-0 rounded-3 shadow-sm py-4">
            <i class="fa-solid fa-triangle-exclamation fa-2x mb-2 text-danger"></i>
            <h5 class="fw-bold mb-1">Unable to load athlete details.</h5>
            <p class="fs-7 mb-0">${escapeHtml(err.message)}</p>
          </div>`;
      }
    });
}

function renderSummaryCards(stats) {
  document.getElementById('detailStatPreds').textContent = stats.total_predictions;
  
  const latestRiskEl = document.getElementById('detailStatLatestRisk');
  if (stats.latest_risk && stats.latest_risk.risk_label) {
    latestRiskEl.innerHTML = getBadgeHTML(stats.latest_risk.risk_label);
  } else {
    latestRiskEl.textContent = 'None';
  }

  document.getElementById('detailStatSleep').textContent = `${stats.avg_sleep} hrs`;
  document.getElementById('detailStatTraining').textContent = `${stats.avg_training} hrs`;
  document.getElementById('detailStatHR').textContent = `${stats.avg_hr} BPM`;
  document.getElementById('detailStatFatigue').textContent = `${stats.avg_fatigue} / 10`;
}

function renderRiskPieChart(stats) {
  const ctx = document.getElementById('athleteRiskPieChart');
  if (!ctx) return;

  if (riskPieInstance) riskPieInstance.destroy();

  const total = stats.low_count + stats.med_count + stats.high_count;
  if (total === 0) {
    ctx.parentNode.innerHTML = `
      <div class="d-flex flex-column align-items-center justify-content-center h-100 text-muted">
        <i class="fa-solid fa-chart-pie fa-3x mb-2 text-slate-300"></i>
        <p class="fs-7 fw-semibold mb-0">No prediction records available.</p>
      </div>`;
    return;
  }

  riskPieInstance = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Low Risk', 'Medium Risk', 'High Risk'],
      datasets: [{
        data: [stats.low_count, stats.med_count, stats.high_count],
        backgroundColor: ['#22c55e', '#f59e0b', '#ef4444'],
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
          labels: { usePointStyle: true, font: { family: 'Inter', size: 11, weight: '600' } }
        }
      }
    }
  });
}

function renderHealthTrendChart(trends) {
  const ctx = document.getElementById('athleteHealthTrendChart');
  if (!ctx) return;

  if (healthTrendInstance) healthTrendInstance.destroy();

  if (!trends.labels || trends.labels.length === 0) {
    ctx.parentNode.innerHTML = `
      <div class="d-flex flex-column align-items-center justify-content-center h-100 text-muted">
        <i class="fa-solid fa-chart-line fa-3x mb-2 text-slate-300"></i>
        <p class="fs-7 fw-semibold mb-0">No health trend records available.</p>
      </div>`;
    return;
  }

  healthTrendInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: trends.labels,
      datasets: [
        {
          label: 'Sleep Hours',
          data: trends.sleep,
          borderColor: '#0284c7',
          backgroundColor: 'rgba(2, 132, 199, 0.1)',
          tension: 0.3,
          fill: true
        },
        {
          label: 'Training Hours',
          data: trends.training,
          borderColor: '#f59e0b',
          backgroundColor: 'transparent',
          borderDash: [5, 5],
          tension: 0.3
        },
        {
          label: 'Risk Score (%)',
          data: trends.risk_score,
          borderColor: '#ef4444',
          backgroundColor: 'transparent',
          tension: 0.3
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          labels: { usePointStyle: true, font: { family: 'Inter', size: 11, weight: '600' } }
        }
      },
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}

function renderMedicalHistory(medical) {
  // Injuries
  const injTbody = document.getElementById('detailInjuriesTbody');
  if (injTbody) {
    if (!medical.injuries || medical.injuries.length === 0) {
      injTbody.innerHTML = `<tr><td colspan="6" class="text-center py-3 text-muted fs-7">No prior injury records recorded.</td></tr>`;
    } else {
      injTbody.innerHTML = medical.injuries.map(i => `
        <tr>
          <td class="fw-bold text-dark">${escapeHtml(i.injury_type)}</td>
          <td><span class="badge bg-light text-dark border">${escapeHtml(i.body_part)}</span></td>
          <td class="fs-7 text-muted">${i.injury_date}</td>
          <td><span class="badge ${i.severity === 'Severe' ? 'bg-danger' : i.severity === 'Moderate' ? 'bg-warning text-dark' : 'bg-info text-dark'}">${escapeHtml(i.severity)}</span></td>
          <td class="fs-7 text-muted">${escapeHtml(i.treatment)}</td>
          <td><span class="badge bg-secondary-subtle text-dark">${escapeHtml(i.recovery_status)}</span></td>
        </tr>
      `).join('');
    }
  }

  // Conditions
  const condList = document.getElementById('detailConditionsList');
  if (condList) {
    if (!medical.conditions || medical.conditions.length === 0) {
      condList.innerHTML = `<div class="p-3 bg-light rounded text-muted">No medical conditions on file.</div>`;
    } else {
      condList.innerHTML = medical.conditions.map(c => `
        <div class="p-2.5 bg-light rounded mb-2 d-flex justify-content-between align-items-center">
          <div>
            <strong class="text-dark">${escapeHtml(c.condition_name)}</strong>
            <div class="fs-8 text-muted">Diagnosed: ${c.diagnosis_date}</div>
          </div>
          <span class="badge bg-primary-subtle text-primary">${escapeHtml(c.status)}</span>
        </div>
      `).join('');
    }
  }

  // Allergies
  const algList = document.getElementById('detailAllergiesList');
  if (algList) {
    if (!medical.allergies || medical.allergies.length === 0) {
      algList.innerHTML = `<div class="p-3 bg-light rounded text-muted">No known allergies on file.</div>`;
    } else {
      algList.innerHTML = medical.allergies.map(a => `
        <div class="p-2.5 bg-light rounded mb-2 d-flex justify-content-between align-items-center">
          <div>
            <strong class="text-dark">${escapeHtml(a.allergy_name)}</strong>
            <div class="fs-8 text-muted">Type: ${escapeHtml(a.allergy_type)}</div>
          </div>
          <span class="badge bg-warning-subtle text-warning-emphasis">${escapeHtml(a.reaction)}</span>
        </div>
      `).join('');
    }
  }
}

function renderHealthRecords(records) {
  const tbody = document.getElementById('detailHealthTbody');
  if (!tbody) return;

  if (!records || records.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" class="text-center py-4 text-muted fs-7">No daily health monitoring submissions.</td></tr>`;
    return;
  }

  tbody.innerHTML = records.map(r => `
    <tr>
      <td class="fw-bold text-dark">${r.record_date}</td>
      <td class="fw-semibold">${r.sleep_hours} hrs</td>
      <td class="fw-semibold">${r.training_hours} hrs</td>
      <td class="fw-semibold">${r.resting_heart_rate} BPM</td>
      <td><span class="badge bg-secondary-subtle text-dark">${r.fatigue_level} / 10</span></td>
      <td><span class="badge bg-secondary-subtle text-dark">${r.stress_level} / 10</span></td>
      <td>${r.previous_injury ? '<span class="badge bg-danger-subtle text-danger fw-bold">YES</span>' : '<span class="badge bg-success-subtle text-success">NO</span>'}</td>
    </tr>
  `).join('');
}

function renderPredictions(preds) {
  const tbody = document.getElementById('detailPredictionsTbody');
  if (!tbody) return;

  if (!preds || preds.length === 0) {
    tbody.innerHTML = `<tr><td colspan="6" class="text-center py-4 text-muted fs-7">No machine learning prediction records.</td></tr>`;
    return;
  }

  tbody.innerHTML = preds.map(p => `
    <tr>
      <td class="fw-bold text-dark">${p.record_date}</td>
      <td>${getBadgeHTML(p.risk_label)}</td>
      <td class="fw-bold fs-7 text-primary">${p.risk_score !== null ? p.risk_score.toFixed(1) + '%' : 'N/A'}</td>
      <td class="fs-7 text-muted">${p.sleep_hours} hrs</td>
      <td class="fs-7 text-muted">${p.training_hours} hrs</td>
      <td class="fs-7 text-muted">${p.resting_heart_rate} BPM</td>
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
