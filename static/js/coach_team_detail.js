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
  const loadingEl = document.getElementById('membersLoading');
  const noMembersEl = document.getElementById('noMembersState');
  const tableWrapperEl = document.getElementById('membersTableWrapper');
  const badgeEl = document.getElementById('memberCountBadge');

  if (loadingEl) loadingEl.classList.remove('d-none');
  if (noMembersEl) noMembersEl.classList.add('d-none');
  if (tableWrapperEl) tableWrapperEl.classList.add('d-none');

  try {
    const res = await fetch(`/api/coach/teams/${CURRENT_TEAM_ID}`);
    const data = await res.json();

    if (loadingEl) loadingEl.classList.add('d-none');

    if (data.status === 'success') {
      if (badgeEl) badgeEl.textContent = `Members: ${data.member_count}`;

      if (data.member_count === 0) {
        if (noMembersEl) noMembersEl.classList.remove('d-none');
      } else {
        renderMembersTable(data.members);
        if (tableWrapperEl) tableWrapperEl.classList.remove('d-none');
      }
    } else {
      showAlert(data.message || 'Unable to load team roster.', 'danger');
    }
  } catch (err) {
    if (loadingEl) loadingEl.classList.add('d-none');
    showAlert('Network error fetching team roster.', 'danger');
  }
}

function renderMembersTable(members) {
  const tbody = document.getElementById('membersTbody');
  if (!tbody) return;

  tbody.innerHTML = members.map(m => `
    <tr>
      <td>
        <div class="d-flex align-items-center gap-2">
          <div class="avatar-circle bg-primary text-white" style="width: 34px; height: 34px; font-size: 0.85rem;">
            ${m.athlete_name[0] ? m.athlete_name[0].toUpperCase() : 'A'}
          </div>
          <div>
            <div class="fw-bold text-dark">${escapeHtml(m.athlete_name)}</div>
          </div>
        </div>
      </td>
      <td><code>${escapeHtml(m.athlete_code)}</code></td>
      <td><span class="text-muted fs-7">${escapeHtml(m.athlete_email)}</span></td>
      <td><span class="badge bg-light text-dark border">${escapeHtml(m.athlete_sport || 'General')}</span></td>
      <td><span class="fs-7 text-muted">${m.joined_at_formatted}</span></td>
      <td><span class="badge bg-success-subtle text-success border border-success-subtle rounded-pill">Active</span></td>
      <td class="text-end">
        <button type="button" class="btn btn-outline-danger btn-sm rounded-pill px-3" onclick="confirmRemoveMember(${m.athlete_id}, '${escapeHtml(m.athlete_name)}')">
          <i class="fa-solid fa-user-minus me-1"></i> Remove
        </button>
      </td>
    </tr>
  `).join('');
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
