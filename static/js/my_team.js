document.addEventListener('DOMContentLoaded', () => {
  loadMyTeams();
});

let selectedLeaveTeamId = null;

function showAlert(msg, type = 'success') {
  const alertEl = document.getElementById('myTeamAlert');
  const msgEl = document.getElementById('myTeamAlertMsg');
  if (!alertEl || !msgEl) return;
  alertEl.className = `alert alert-${type} alert-dismissible fade show`;
  msgEl.textContent = msg;
  alertEl.classList.remove('d-none');
}

async function loadMyTeams() {
  const loadingEl = document.getElementById('myTeamLoading');
  const noTeamEl = document.getElementById('noMyTeamState');
  const containerEl = document.getElementById('myTeamContainer');

  if (loadingEl) loadingEl.classList.remove('d-none');
  if (noTeamEl) noTeamEl.classList.add('d-none');
  if (containerEl) containerEl.classList.add('d-none');

  try {
    const res = await fetch('/api/my-team');
    const data = await res.json();

    if (loadingEl) loadingEl.classList.add('d-none');

    if (data.status === 'success') {
      if (data.count === 0) {
        if (noTeamEl) noTeamEl.classList.remove('d-none');
      } else {
        renderMyTeams(data.teams);
        if (containerEl) containerEl.classList.remove('d-none');
      }
    } else {
      showAlert(data.message || 'Unable to load your team info.', 'danger');
    }
  } catch (err) {
    if (loadingEl) loadingEl.classList.add('d-none');
    showAlert('Network error fetching team membership.', 'danger');
  }
}

function renderMyTeams(teams) {
  const containerEl = document.getElementById('myTeamContainer');
  if (!containerEl) return;

  containerEl.innerHTML = teams.map(t => `
    <div class="col-md-6 col-lg-6">
      <div class="card-master p-4 shadow-sm border rounded-4 h-100 position-relative">
        <div class="d-flex justify-content-between align-items-start mb-3">
          <div>
            <span class="badge bg-info text-dark rounded-pill px-3 py-1.5 fw-semibold me-1">${escapeHtml(t.team_sport)}</span>
            <span class="badge bg-secondary rounded-pill px-2.5 py-1.5 fs-8">Season: ${escapeHtml(t.team_season || '2026-27')}</span>
          </div>
          <span class="badge bg-success rounded-pill px-3 py-1.5"><i class="fa-solid fa-circle-check me-1"></i> Active Member</span>
        </div>

        <h3 class="fw-bold text-dark mb-1">${escapeHtml(t.team_name)}</h3>
        <p class="text-muted fs-7 mb-3"><i class="fa-solid fa-user-tie text-primary me-1"></i> Coach: <strong>${escapeHtml(t.coach_name)}</strong></p>

        <div class="p-3 bg-light rounded-3 border mb-4">
          <div class="row g-2 text-center fs-7">
            <div class="col-6 border-end">
              <span class="text-muted fs-8 text-uppercase d-block fw-semibold">Team Code</span>
              <code class="fw-bold fs-5 text-primary">${escapeHtml(t.team_code)}</code>
            </div>
            <div class="col-6">
              <span class="text-muted fs-8 text-uppercase d-block fw-semibold">Joined Date</span>
              <strong class="text-dark fs-6">${t.joined_at_formatted}</strong>
            </div>
          </div>
        </div>

        <div class="d-flex justify-content-between align-items-center pt-2 border-top">
          <span class="text-muted fs-7"><i class="fa-solid fa-shield-halved text-success me-1"></i> Status: Active</span>
          <span class="text-muted fs-8">Verified Membership</span>
        </div>
      </div>
    </div>
  `).join('');
}

function confirmLeaveTeam(teamId, teamName) {
  selectedLeaveTeamId = teamId;
  const nameSpan = document.getElementById('leaveTeamName');
  if (nameSpan) nameSpan.textContent = teamName;

  const confirmBtn = document.getElementById('btnConfirmLeaveTeam');
  if (confirmBtn) {
    confirmBtn.onclick = () => executeLeaveTeam(teamId);
  }

  const modalEl = document.getElementById('leaveTeamModal');
  const modal = new bootstrap.Modal(modalEl);
  modal.show();
}

async function executeLeaveTeam(teamId) {
  const confirmBtn = document.getElementById('btnConfirmLeaveTeam');
  if (confirmBtn) {
    confirmBtn.disabled = true;
    confirmBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span> Leaving...';
  }

  try {
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';
    const res = await fetch('/api/teams/leave', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({ team_id: teamId })
    });
    const data = await res.json();

    if (confirmBtn) {
      confirmBtn.disabled = false;
      confirmBtn.innerHTML = '<i class="fa-solid fa-check-circle me-1"></i> Yes, Leave Team';
    }

    const modalEl = document.getElementById('leaveTeamModal');
    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) modal.hide();

    if (data.status === 'success') {
      showAlert(data.message, 'warning');
      loadMyTeams();
    } else {
      alert(data.message || 'Unable to leave team.');
    }
  } catch (err) {
    if (confirmBtn) {
      confirmBtn.disabled = false;
      confirmBtn.innerHTML = '<i class="fa-solid fa-check-circle me-1"></i> Yes, Leave Team';
    }
    alert('Network error while leaving team.');
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}
