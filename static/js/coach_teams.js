document.addEventListener('DOMContentLoaded', () => {
  loadCoachTeams();
});

function showAlert(msg, type = 'success') {
  const alertEl = document.getElementById('teamsAlert');
  const msgEl = document.getElementById('teamsAlertMsg');
  if (!alertEl || !msgEl) return;
  alertEl.className = `alert alert-${type} alert-dismissible fade show`;
  msgEl.textContent = msg;
  alertEl.classList.remove('d-none');
}

async function loadCoachTeams() {
  const loadingEl = document.getElementById('teamsLoading');
  const noTeamsEl = document.getElementById('noTeamsState');
  const gridEl = document.getElementById('teamsGrid');

  if (loadingEl) loadingEl.classList.remove('d-none');
  if (noTeamsEl) noTeamsEl.classList.add('d-none');
  if (gridEl) gridEl.classList.add('d-none');

  try {
    const res = await fetch('/api/coach/teams');
    const data = await res.json();

    if (loadingEl) loadingEl.classList.add('d-none');

    if (data.status === 'success') {
      if (data.count === 0) {
        if (noTeamsEl) noTeamsEl.classList.remove('d-none');
      } else {
        renderTeamsGrid(data.teams);
        if (gridEl) gridEl.classList.remove('d-none');
      }
    } else {
      showAlert(data.message || 'Unable to load teams.', 'danger');
    }
  } catch (err) {
    if (loadingEl) loadingEl.classList.add('d-none');
    showAlert('Network error while fetching teams.', 'danger');
  }
}

function renderTeamsGrid(teams) {
  const gridEl = document.getElementById('teamsGrid');
  if (!gridEl) return;

  gridEl.innerHTML = teams.map(t => `
    <div class="col-md-6 col-lg-4">
      <div class="card-master h-100 p-4 shadow-sm position-relative">
        <div class="d-flex justify-content-between align-items-start mb-3">
          <div>
            <span class="badge bg-info text-dark rounded-pill fw-semibold px-3 py-1 me-1">${escapeHtml(t.sport)}</span>
            <span class="badge bg-secondary rounded-pill px-2 py-1 fs-8">Season: ${escapeHtml(t.season || '2026-27')}</span>
          </div>
          <span class="badge bg-success rounded-pill px-2.5 py-1">Active</span>
        </div>

        <h4 class="fw-bold text-dark mb-1">${escapeHtml(t.team_name)}</h4>
        ${t.description ? `<p class="text-muted fs-7 mb-2 text-truncate" title="${escapeHtml(t.description)}">${escapeHtml(t.description)}</p>` : ''}
        <p class="text-muted fs-7 mb-3"><i class="fa-regular fa-calendar text-primary me-1"></i> Created ${t.created_at_formatted}</p>

        <div class="p-3 bg-light rounded-3 border mb-3">
          <div class="d-flex justify-content-between align-items-center mb-1">
            <span class="text-muted fs-8 text-uppercase fw-semibold">Team Code</span>
            <button class="btn btn-sm btn-link text-decoration-none p-0 fs-8 fw-semibold" onclick="copyTeamCode('${t.team_code}')">
              <i class="fa-regular fa-copy me-1"></i> Copy
            </button>
          </div>
          <code class="fs-4 fw-bold text-primary">${t.team_code}</code>
        </div>

        <div class="d-flex justify-content-between align-items-center pt-2 border-top">
          <span class="text-dark fw-bold fs-7"><i class="fa-solid fa-users text-primary me-1"></i> Players: ${t.member_count}</span>
          <a href="/coach/teams/${t.id}" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">
            View Team <i class="fa-solid fa-arrow-right ms-1"></i>
          </a>
        </div>
      </div>
    </div>
  `).join('');
}

async function handleCreateTeam(e) {
  e.preventDefault();
  const form = e.target;
  const btn = document.getElementById('btnSubmitCreateTeam');
  const team_name = form.team_name.value.trim();
  const sport = form.sport.value.trim();
  const season = form.season ? form.season.value.trim() : '2026-27';
  const description = form.description ? form.description.value.trim() : '';
  const csrf_token = form.csrf_token ? form.csrf_token.value : '';

  if (!team_name || !sport) {
    alert('Please fill out all required fields.');
    return;
  }

  if (btn) {
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span> Creating...';
  }

  try {
    const res = await fetch('/api/coach/teams', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({ team_name, sport, season, description, csrf_token })
    });
    const data = await res.json();

    if (btn) {
      btn.disabled = false;
      btn.innerHTML = '<i class="fa-solid fa-check-circle me-1"></i> Create Team';
    }

    if (data.status === 'success') {
      const modalEl = document.getElementById('createTeamModal');
      const modal = bootstrap.Modal.getInstance(modalEl);
      if (modal) modal.hide();

      form.reset();

      // Populate Success Modal
      document.getElementById('successTeamName').textContent = data.team.team_name;
      document.getElementById('successSport').textContent = data.team.sport;
      document.getElementById('successSeason').textContent = `Season: ${data.team.season}`;
      document.getElementById('successTeamCode').textContent = data.team.team_code;

      const successModalEl = document.getElementById('teamCreatedSuccessModal');
      if (successModalEl) {
        const successModal = new bootstrap.Modal(successModalEl);
        successModal.show();
      }

      showAlert(data.message, 'success');
      loadCoachTeams();
    } else {
      alert(data.message || 'Failed to create team.');
    }
  } catch (err) {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = '<i class="fa-solid fa-check-circle me-1"></i> Create Team';
    }
    alert('Network error while creating team.');
  }
}

function copyTeamCode(code) {
  navigator.clipboard.writeText(code).then(() => {
    showAlert(`Team code '${code}' copied to clipboard!`, 'info');
  }).catch(() => {
    alert(`Team code: ${code}`);
  });
}

function copySuccessTeamCode() {
  const code = document.getElementById('successTeamCode').textContent;
  copyTeamCode(code);
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}
