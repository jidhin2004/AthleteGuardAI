/**
 * AthleteGuard AI - Admin Global Predictions & Case Review Controller
 */

let allPredictionsCache = [];
let currentReviewRecordId = null;

let currentReviewAthleteUserId = null;

document.addEventListener('DOMContentLoaded', function () {
  fetchPredictionsLog();

  const searchInput = document.getElementById('predictionSearchInput');
  const riskFilter = document.getElementById('predictionRiskFilter');
  const statusFilter = document.getElementById('predictionStatusFilter');

  if (searchInput) {
    searchInput.addEventListener('input', filterPredictionsTable);
  }
  if (riskFilter) {
    riskFilter.addEventListener('change', filterPredictionsTable);
  }
  if (statusFilter) {
    statusFilter.addEventListener('change', filterPredictionsTable);
  }

  // Send Notification & Save Case Review Handler
  const btnSendNotif = document.getElementById('btnSendNotification') || document.getElementById('btnSaveCaseReview');
  if (btnSendNotif) {
    btnSendNotif.addEventListener('click', submitCaseReviewUpdate);
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

      // Check if URL has ?record_id= parameter from Dashboard redirect
      const urlParams = new URLSearchParams(window.location.search);
      const targetRecordId = urlParams.get('record_id');
      if (targetRecordId) {
        openCaseReviewModal(targetRecordId);
      }
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
  const selectedStatus = (document.getElementById('predictionStatusFilter')?.value || 'all');

  const filtered = allPredictionsCache.filter(p => {
    // Risk Filter
    if (selectedRisk !== 'all') {
      if (!(p.risk_label || '').toLowerCase().includes(selectedRisk)) {
        return false;
      }
    }

    // Status Filter
    if (selectedStatus !== 'all') {
      const pStatus = p.review_status || 'Pending Review';
      if (pStatus.toLowerCase() !== selectedStatus.toLowerCase()) {
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
        (p.review_status || '').toLowerCase().includes(query) ||
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
    badgeEl.textContent = `${records.length} Case${records.length === 1 ? '' : 's'}`;
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
      <td class="fw-bold fs-7 ${p.risk_score > 65 ? 'text-danger' : 'text-primary'}">${p.risk_score !== null ? p.risk_score.toFixed(1) + '%' : 'N/A'}</td>
      <td>${getStatusBadgeHTML(p.review_status)}</td>
      <td class="text-center">
        <button type="button" class="btn btn-sm btn-primary rounded-pill px-3 py-1 fw-bold fs-8 shadow-sm" onclick="openCaseReviewModal(${p.id})">
          <i class="fa-regular fa-pen-to-square me-1"></i> Review Case
        </button>
      </td>
    </tr>
  `).join('');
}

function openCaseReviewModal(recordId) {
  currentReviewRecordId = recordId;

  fetch(`/api/admin/cases/${recordId}`)
    .then(res => res.json())
    .then(data => {
      if (data.status !== 'success') throw new Error(data.message);

      const record = data.record;
      const athlete = data.athlete;

      currentReviewAthleteUserId = athlete.id;

      document.getElementById('modalAthleteName').textContent = athlete.full_name;
      document.getElementById('modalAthleteId').textContent = athlete.athlete_id;
      document.getElementById('modalAthleteSport').textContent = `${athlete.primary_sport} Athlete`;
      document.getElementById('modalRecordDate').textContent = `Recorded: ${record.record_date}`;

      document.getElementById('modalRiskBadge').innerHTML = getBadgeHTML(record.risk_label);
      document.getElementById('modalRiskScore').textContent = `${record.risk_score !== null ? record.risk_score.toFixed(1) + '%' : 'N/A'} Score`;

      // Biometrics
      document.getElementById('modalSleep').textContent = `${record.sleep_hours} hrs`;
      document.getElementById('modalTraining').textContent = `${record.training_hours} hrs`;
      document.getElementById('modalHR').textContent = `${record.resting_heart_rate} BPM`;
      document.getElementById('modalFatigue').textContent = `Level ${record.fatigue_level}/10`;
      document.getElementById('modalStress').textContent = `Level ${record.stress_level}/10`;
      document.getElementById('modalPrevInjury').textContent = record.previous_injury ? `Yes (${record.injury_details || 'Recorded'})` : 'None Reported';

      // Status selector
      document.getElementById('modalReviewStatusSelect').value = record.review_status || 'Pending Review';
      document.getElementById('modalNewNoteInput').value = '';

      // Notes History
      renderModalNotes(data.notes);

      // Show Bootstrap Modal
      const modalEl = document.getElementById('caseReviewModal');
      const bsModal = new bootstrap.Modal(modalEl);
      bsModal.show();
    })
    .catch(err => {
      console.error('Case Detail Error:', err);
      alert('Unable to load case details. Please try again.');
    });
}

function renderModalNotes(notes) {
  const container = document.getElementById('modalNotesHistory');
  if (!container) return;

  if (!notes || notes.length === 0) {
    container.innerHTML = `<p class="fs-7 text-muted italic mb-0">No previous administrative notes for this case.</p>`;
    return;
  }

  container.innerHTML = notes.map(n => `
    <div class="card bg-white border p-3 rounded-3 mb-2">
      <div class="d-flex justify-content-between align-items-center mb-1">
        <span class="fw-bold text-dark fs-7"><i class="fa-solid fa-user-shield text-info me-1"></i> ${escapeHtml(n.admin_name)}</span>
        <span class="fs-8 text-muted">${n.created_at_formatted}</span>
      </div>
      <p class="fs-7 text-secondary mb-0">${escapeHtml(n.note)}</p>
    </div>
  `).join('');
}

function submitCaseReviewUpdate() {
  if (!currentReviewRecordId || !currentReviewAthleteUserId) return;

  const newStatus = document.getElementById('modalReviewStatusSelect').value;
  const noteText = (document.getElementById('modalNewNoteInput').value || '').trim();

  if (!noteText) {
    alert("Please enter a recommendation or message for the athlete.");
    return;
  }

  if (!confirm("Send this notification to this athlete?")) {
    return;
  }

  const btnSend = document.getElementById('btnSendNotification') || document.getElementById('btnSaveCaseReview');
  const originalHtml = btnSend.innerHTML;
  btnSend.disabled = true;
  btnSend.innerHTML = `<span class="spinner-border spinner-border-sm me-1"></span> Sending...`;

  // First update status
  fetch(`/api/admin/cases/${currentReviewRecordId}/status`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': typeof getCsrfToken === 'function' ? getCsrfToken() : ''
    },
    body: JSON.stringify({ review_status: newStatus })
  })
    .then(res => res.json())
    .then(statusData => {
      // Next send notification
      return fetch('/api/admin/notifications', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': typeof getCsrfToken === 'function' ? getCsrfToken() : ''
        },
        body: JSON.stringify({
          athlete_id: currentReviewAthleteUserId,
          related_prediction_id: currentReviewRecordId,
          message: noteText
        })
      });
    })
    .then(res => res.json())
    .then(data => {
      btnSend.disabled = false;
      btnSend.innerHTML = originalHtml;

      if (data.status !== 'success') {
        alert(data.message || 'Unable to send notification to athlete.');
        return;
      }

      alert("Notification sent successfully.");

      // Hide modal
      const modalEl = document.getElementById('caseReviewModal');
      const bsModal = bootstrap.Modal.getInstance(modalEl);
      if (bsModal) bsModal.hide();

      // Refresh predictions table
      fetchPredictionsLog();
    })
    .catch(err => {
      console.error('Case Update Error:', err);
      btnSend.disabled = false;
      btnSend.innerHTML = originalHtml;
      alert('Unable to send notification. Please check server connection.');
    });
}

function getStatusBadgeHTML(status) {
  if (!status) status = 'Pending Review';
  switch (status) {
    case 'Pending Review':
      return `<span class="badge bg-warning text-dark border border-warning-subtle fw-semibold px-2.5 py-1"><i class="fa-regular fa-clock me-1"></i> Pending Review</span>`;
    case 'Under Review':
      return `<span class="badge bg-info text-dark border border-info-subtle fw-semibold px-2.5 py-1"><i class="fa-solid fa-magnifying-glass me-1"></i> Under Review</span>`;
    case 'Needs Attention':
      return `<span class="badge bg-danger text-white fw-bold px-2.5 py-1"><i class="fa-solid fa-triangle-exclamation me-1"></i> Needs Attention</span>`;
    case 'Monitoring':
      return `<span class="badge bg-primary text-white fw-semibold px-2.5 py-1"><i class="fa-solid fa-eye me-1"></i> Monitoring</span>`;
    case 'Resolved':
      return `<span class="badge bg-success text-white fw-semibold px-2.5 py-1"><i class="fa-solid fa-circle-check me-1"></i> Resolved</span>`;
    default:
      return `<span class="badge bg-secondary text-white fw-semibold px-2.5 py-1">${escapeHtml(status)}</span>`;
  }
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
