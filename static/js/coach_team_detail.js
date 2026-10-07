document.addEventListener('DOMContentLoaded', () => {
  if (typeof CURRENT_TEAM_ID !== 'undefined') {
    loadTeamDetail();
  }
});

let selectedAthleteId = null;

function showAlert(msg, type = 'success') {
  const alertEl = document.getElementById('teamDetailAlert');
  const msgEl = document.getElementById('teamDetailAlertMsg');
  if (!alertEl || !msgEl) return;
  alertEl.className = `alert alert-${type} alert-dismissible fade show`;
  msgEl.textContent = msg;
  alertEl.classList.remove('d-none');
}

async function loadTeamDetail() {
  await loadCheckinTracking();
}

async function loadCheckinTracking() {
  const loadingEl = document.getElementById('membersLoading');
  const noMembersEl = document.getElementById('noMembersState');
  const tableWrapperEl = document.getElementById('membersTableWrapper');
  const badgeEl = document.getElementById('memberCountBadge');

  if (loadingEl) loadingEl.classList.remove('d-none');
  if (noMembersEl) noMembersEl.classList.add('d-none');
  if (tableWrapperEl) tableWrapperEl.classList.add('d-none');

  try {
    const res = await fetch(`/api/coach/teams/${CURRENT_TEAM_ID}/daily-checkins`);
    const data = await res.json();

    if (loadingEl) loadingEl.classList.add('d-none');

    if (data.status === 'success') {
      // Update Summary Cards
      const totalEl = document.getElementById('statTotalPlayers');
      const submittedEl = document.getElementById('statSubmittedToday');
      const pendingEl = document.getElementById('statPendingToday');
      const completionEl = document.getElementById('statCompletionRate');
      const progressBarEl = document.getElementById('checkinProgressBar');
      const dateDisplayEl = document.getElementById('checkinDateDisplay');

      if (totalEl) totalEl.textContent = data.total_players;
      if (submittedEl) submittedEl.textContent = data.submitted;
      if (pendingEl) pendingEl.textContent = data.pending;
      if (completionEl) completionEl.textContent = `${data.completion_percentage}%`;
      if (dateDisplayEl && data.checkin_date) dateDisplayEl.textContent = data.checkin_date;

      if (progressBarEl) {
        progressBarEl.style.width = `${data.completion_percentage}%`;
        progressBarEl.setAttribute('aria-valuenow', data.completion_percentage);
      }

      if (badgeEl) badgeEl.textContent = `Members: ${data.total_players}`;

      if (data.total_players === 0) {
        if (noMembersEl) noMembersEl.classList.remove('d-none');
      } else {
        renderMembersTable(data.players);
        if (tableWrapperEl) tableWrapperEl.classList.remove('d-none');
      }
    } else {
      showAlert(data.message || 'Unable to load check-in tracking data.', 'danger');
    }
  } catch (err) {
    if (loadingEl) loadingEl.classList.add('d-none');
    showAlert('Network error fetching check-in tracking data.', 'danger');
  }
}

function renderMembersTable(players) {
  const tbody = document.getElementById('membersTbody');
  if (!tbody) return;

  tbody.innerHTML = players.map(p => {
    const isSubmitted = p.checkin_status === 'Submitted';
    const checkinBadge = isSubmitted
      ? `<span class="badge bg-success-subtle text-success border border-success-subtle rounded-pill px-3 py-1 fw-bold"><i class="fa-solid fa-circle-check me-1"></i> Submitted Today</span>`
      : `<span class="badge bg-warning-subtle text-warning-emphasis border border-warning-subtle rounded-pill px-3 py-1 fw-bold"><i class="fa-solid fa-clock-rotate-left me-1"></i> Pending Today</span>`;

    const lastUpdateBadge = p.last_update === 'Today'
      ? `<span class="text-success fw-bold"><i class="fa-solid fa-calendar-day me-1"></i> Today</span>`
      : p.last_update === 'Yesterday'
      ? `<span class="text-secondary fw-semibold"><i class="fa-solid fa-calendar-minus me-1"></i> Yesterday</span>`
      : p.last_update === 'Never'
      ? `<span class="text-muted fst-italic">Never</span>`
      : `<span class="text-dark fs-7">${escapeHtml(p.last_update)}</span>`;

    return `
      <tr>
        <td>
          <div class="d-flex align-items-center gap-2">
            <div class="avatar-circle bg-primary text-white" style="width: 34px; height: 34px; font-size: 0.85rem;">
              ${p.athlete_name[0] ? p.athlete_name[0].toUpperCase() : 'A'}
            </div>
            <div>
              <div class="fw-bold text-dark">${escapeHtml(p.athlete_name)}</div>
              <div class="text-muted fs-8">${escapeHtml(p.athlete_email)}</div>
            </div>
          </div>
        </td>
        <td><code>${escapeHtml(p.athlete_code || ('ATH-' + p.athlete_id))}</code></td>
        <td>${checkinBadge}</td>
        <td>${lastUpdateBadge}</td>
        <td><span class="fs-7 text-muted">${p.joined_at_formatted || 'Active Member'}</span></td>
        <td class="text-end">
          <button type="button" class="btn btn-outline-danger btn-sm rounded-pill px-3" onclick="confirmRemoveMember(${p.athlete_id}, '${escapeHtml(p.athlete_name)}')">
            <i class="fa-solid fa-user-minus me-1"></i> Remove
          </button>
        </td>
      </tr>
    `;
  }).join('');
}

function confirmRemoveMember(athleteId, athleteName) {
  selectedAthleteId = athleteId;
  const nameSpan = document.getElementById('removeAthleteName');
  if (nameSpan) nameSpan.textContent = athleteName;

  const confirmBtn = document.getElementById('btnConfirmRemoveMember');
  if (confirmBtn) {
    confirmBtn.onclick = () => executeRemoveMember(athleteId);
  }

  const modalEl = document.getElementById('removeMemberModal');
  const modal = new bootstrap.Modal(modalEl);
  modal.show();
}

async function executeRemoveMember(athleteId) {
  const confirmBtn = document.getElementById('btnConfirmRemoveMember');
  if (confirmBtn) {
    confirmBtn.disabled = true;
    confirmBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span> Removing...';
  }

  try {
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';
    const res = await fetch(`/api/coach/teams/${CURRENT_TEAM_ID}/members/${athleteId}/remove`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      }
    });
    const data = await res.json();

    if (confirmBtn) {
      confirmBtn.disabled = false;
      confirmBtn.innerHTML = '<i class="fa-solid fa-user-xmark me-1"></i> Yes, Remove Athlete';
    }

    const modalEl = document.getElementById('removeMemberModal');
    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) modal.hide();

    if (data.status === 'success') {
      showAlert(data.message, 'success');
      loadTeamDetail();
    } else {
      alert(data.message || 'Failed to remove athlete.');
    }
  } catch (err) {
    if (confirmBtn) {
      confirmBtn.disabled = false;
      confirmBtn.innerHTML = '<i class="fa-solid fa-user-xmark me-1"></i> Yes, Remove Athlete';
    }
    alert('Network error while removing member.');
  }
}

function copyTeamCode(code) {
  navigator.clipboard.writeText(code).then(() => {
    showAlert(`Team code '${code}' copied to clipboard!`, 'info');
  }).catch(() => {
    alert(`Team code: ${code}`);
  });
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}
