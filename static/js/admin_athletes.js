/**
 * AthleteGuard AI - Admin Athletes Roster Controller
 */

let allAthletesCache = [];

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
        (a.primary_sport || '').toLowerCase().includes(query)
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

  tbody.innerHTML = athletes.map(a => `
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
      <td class="fw-semibold text-dark">${a.age}</td>
      <td class="fs-7 text-muted">${formatDate(a.created_at)}</td>
      <td class="text-center">
        <a href="/admin/athletes/${a.id}" class="btn btn-sm btn-outline-primary rounded-pill px-3 py-1 fw-bold fs-8">
          <i class="fa-solid fa-eye me-1"></i> Audit Detail
        </a>
      </td>
    </tr>
  `).join('');
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
