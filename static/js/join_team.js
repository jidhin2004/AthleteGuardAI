function showAlert(msg, type = 'success') {
  const alertEl = document.getElementById('joinTeamAlert');
  const msgEl = document.getElementById('joinTeamAlertMsg');
  if (!alertEl || !msgEl) return;
  alertEl.className = `alert alert-${type} alert-dismissible fade show`;
  msgEl.textContent = msg;
  alertEl.classList.remove('d-none');
}

async function handleJoinTeam(e) {
  e.preventDefault();
  const form = e.target;
  const btn = document.getElementById('btnSubmitJoin');
  const team_code = form.team_code.value.trim().toUpperCase();
  const csrf_token = form.csrf_token ? form.csrf_token.value : '';

  if (!team_code) {
    showAlert('Please enter a valid Team Code.', 'danger');
    return;
  }

  if (btn) {
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span> Verifying Code...';
  }

  try {
    const res = await fetch('/api/teams/join', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({ team_code, csrf_token })
    });
    const data = await res.json();

    if (btn) {
      btn.disabled = false;
      btn.innerHTML = '<i class="fa-solid fa-user-plus me-2"></i> Join Team';
    }

    if (data.status === 'success') {
      showAlert(data.message, 'success');
      form.reset();
      setTimeout(() => {
        window.location.href = '/my-team';
      }, 1200);
    } else {
      showAlert(data.message || 'Unable to join team.', 'danger');
    }
  } catch (err) {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = '<i class="fa-solid fa-user-plus me-2"></i> Join Team';
    }
    showAlert('Network error while joining team.', 'danger');
  }
}
