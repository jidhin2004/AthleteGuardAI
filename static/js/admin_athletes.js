/**
 * AthleteGuard AI - Admin Athletes Roster & Account Management Controller
 */

let allAthletesCache = [];
let pendingStatusChangeUser = null;

document.addEventListener('DOMContentLoaded', function () {
  fetchAthletesRoster();

  const searchInput = document.getElementById('athleteSearchInput');
  const sportFilter = document.getElementById('athleteSportFilter');

  if (searchInput) {
    searchInput.addEventListener('input', filterAthletesTable);
  }
  if (sportFilter) {
    sportFilter.addEventListener('change', filterAthletesTable);
  }

  // Confirmation button click listener
  const btnConfirm = document.getElementById('btnConfirmStatusChange');
  if (btnConfirm) {
    btnConfirm.addEventListener('click', executeStatusChange);
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

function fetchAthletesRoster() {
  const loadingEl = document.getElementById('athletesLoadingState');
  const emptyEl = document.getElementById('athletesEmptyState');
  const contentEl = document.getElementById('athletesContentArea');

  if (loadingEl) loadingEl.style.display = 'block';
  if (emptyEl) emptyEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'none';

  fetch('/api/admin/athletes')
    .then(res => {
      if (!res.ok) throw new Error(`HTTP error ${res.status}`);
      return res.json();
    })
    .then(data => {
      if (data.status !== 'success') throw new Error(data.message);

      allAthletesCache = data.athletes || [];
      populateSportOptions(allAthletesCache);

      if (loadingEl) loadingEl.style.display = 'none';
      filterAthletesTable();
    })
    .catch(err => {
      console.error('Athletes Roster Fetch Error:', err);
      if (loadingEl) loadingEl.style.display = 'none';
      if (emptyEl) {
        emptyEl.style.display = 'block';
        emptyEl.querySelector('h4').textContent = 'Unable to load athletes roster.';
      }
    });
}

function populateSportOptions(athletes) {
  const select = document.getElementById('athleteSportFilter');
  if (!select) return;

  const sportsSet = new Set();
  athletes.forEach(a => {
    if (a.primary_sport) sportsSet.add(a.primary_sport);
  });

  const currentVal = select.value;
  select.innerHTML = '<option value="all">All Sports</option>';

  Array.from(sportsSet).sort().forEach(s => {
    const opt = document.createElement('option');
    opt.value = s.toLowerCase();
    opt.textContent = s;
    select.appendChild(opt);
  });

  select.value = currentVal;
}

function filterAthletesTable() {
  const query = (document.getElementById('athleteSearchInput')?.value || '').trim().toLowerCase();
  const selectedSport = (document.getElementById('athleteSportFilter')?.value || 'all').toLowerCase();

  const filtered = allAthletesCache.filter(a => {
    // Sport Filter
    if (selectedSport !== 'all' && (a.primary_sport || '').toLowerCase() !== selectedSport) {
      return false;
    }

    // Search Filter
    if (query) {
      const match = (
        (a.full_name || '').toLowerCase().includes(query) ||
        (a.email || '').toLowerCase().includes(query) ||
        (a.athlete_id || '').toLowerCase().includes(query) ||
        (a.primary_sport || '').toLowerCase().includes(query) ||
        (a.account_status || '').toLowerCase().includes(query)
      );
      if (!match) return false;
    }

    return true;
  });

  renderAthletesTable(filtered);
}

function renderAthletesTable(athletes) {
  const tbody = document.getElementById('athletesTableBody');
  const emptyEl = document.getElementById('athletesEmptyState');
  const contentEl = document.getElementById('athletesContentArea');
  const badgeEl = document.getElementById('totalAthletesBadge');

  if (badgeEl) {
    badgeEl.textContent = `${athletes.length} Athlete${athletes.length === 1 ? '' : 's'}`;
  }

  if (!athletes || athletes.length === 0) {
    if (contentEl) contentEl.style.display = 'none';
    if (emptyEl) emptyEl.style.display = 'block';
    return;
  }

  if (emptyEl) emptyEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'block';

  tbody.innerHTML = athletes.map(a => {
    const isActive = (a.account_status || 'active').toLowerCase() === 'active';
    const statusBadge = isActive
      ? `<span class="badge bg-success-subtle text-success border border-success-subtle px-2.5 py-1 fw-bold"><i class="fa-solid fa-circle-check me-1"></i> Active</span>`
      : `<span class="badge bg-secondary-subtle text-secondary border border-secondary-subtle px-2.5 py-1 fw-bold"><i class="fa-solid fa-ban me-1"></i> Inactive</span>`;

    const toggleBtn = isActive
      ? `<button type="button" class="btn btn-sm btn-outline-danger rounded-pill px-2.5 py-1 fw-bold fs-8 ms-1" onclick="promptStatusToggle(${a.id}, 'deactivate', '${escapeHtml(a.full_name)}')">
           <i class="fa-solid fa-user-slash me-1"></i> Deactivate
         </button>`
      : `<button type="button" class="btn btn-sm btn-outline-success rounded-pill px-2.5 py-1 fw-bold fs-8 ms-1" onclick="promptStatusToggle(${a.id}, 'activate', '${escapeHtml(a.full_name)}')">
           <i class="fa-solid fa-user-check me-1"></i> Activate
         </button>`;

    return `
      <tr>
        <td class="fw-bold text-primary">${a.athlete_id}</td>
        <td>
          <div class="fw-bold text-dark">${escapeHtml(a.full_name)}</div>
        </td>
        <td class="text-muted fs-7">${escapeHtml(a.email)}</td>
        <td>
          <span class="badge bg-secondary-subtle text-dark border px-2.5 py-1 font-sans">
            ${escapeHtml(a.primary_sport)}
          </span>
        </td>
        <td>${statusBadge}</td>
        <td class="fs-7 text-muted">${formatDate(a.created_at)}</td>
        <td class="text-center">
          <a href="/admin/athletes/${a.id}" class="btn btn-sm btn-outline-primary rounded-pill px-2.5 py-1 fw-bold fs-8">
            <i class="fa-solid fa-eye me-1"></i> View
          </a>
          ${toggleBtn}
        </td>
      </tr>
    `;
  }).join('');
}

function promptStatusToggle(userId, targetAction, athleteName) {
  pendingStatusChangeUser = { userId, targetAction, athleteName };

  const modalTitle = document.getElementById('statusModalTitle');
  const modalBody = document.getElementById('statusModalBodyText');
  const iconContainer = document.getElementById('statusModalIconContainer');
  const btnConfirm = document.getElementById('btnConfirmStatusChange');

  if (targetAction === 'deactivate') {
    modalTitle.textContent = `Deactivate Athlete Account`;
    modalBody.textContent = `Are you sure you want to deactivate the account for '${athleteName}'? The athlete will be unable to log in, but all historical health records and predictions will be preserved.`;
    iconContainer.innerHTML = `<i class="fa-solid fa-user-slash fa-3x text-danger"></i>`;
    btnConfirm.className = 'btn btn-danger fw-bold px-4 rounded-3 shadow-sm';
    btnConfirm.textContent = 'Deactivate Account';
  } else {
    modalTitle.textContent = `Activate Athlete Account`;
    modalBody.textContent = `Are you sure you want to reactivate the account for '${athleteName}'? The athlete will regain login access to their dashboard.`;
    iconContainer.innerHTML = `<i class="fa-solid fa-user-check fa-3x text-success"></i>`;
    btnConfirm.className = 'btn btn-success fw-bold px-4 rounded-3 shadow-sm';
    btnConfirm.textContent = 'Activate Account';
  }

  const modalEl = document.getElementById('accountStatusModal');
  const bsModal = new bootstrap.Modal(modalEl);
  bsModal.show();
}

function executeStatusChange() {
  if (!pendingStatusChangeUser) return;

  const { userId, targetAction, athleteName } = pendingStatusChangeUser;
  const endpoint = `/api/admin/athletes/${userId}/${targetAction}`;

  const btnConfirm = document.getElementById('btnConfirmStatusChange');
  const originalText = btnConfirm.textContent;
  btnConfirm.disabled = true;
  btnConfirm.textContent = 'Processing...';

  fetch(endpoint, { method: 'POST' })
    .then(res => res.json())
    .then(data => {
      btnConfirm.disabled = false;
      btnConfirm.textContent = originalText;

      if (data.status !== 'success') {
        alert(data.message || 'Unable to change account status.');
        return;
      }

      // Close modal
      const modalEl = document.getElementById('accountStatusModal');
      const bsModal = bootstrap.Modal.getInstance(modalEl);
      if (bsModal) bsModal.hide();

      // Refresh roster
      fetchAthletesRoster();
    })
    .catch(err => {
      console.error('Account Status Change Error:', err);
      btnConfirm.disabled = false;
      btnConfirm.textContent = originalText;
      alert('Network error. Unable to change account status.');
    });
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
