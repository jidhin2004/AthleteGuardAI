/**
 * AthleteGuard AI - Admin Global Health Records Controller
 */

let allHealthRecordsCache = [];

document.addEventListener('DOMContentLoaded', function () {
  fetchHealthRecordsLog();

  const searchInput = document.getElementById('healthSearchInput');
  if (searchInput) {
    searchInput.addEventListener('input', filterHealthTable);
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

function fetchHealthRecordsLog() {
  const loadingEl = document.getElementById('healthLoadingState');
  const emptyEl = document.getElementById('healthEmptyState');
  const contentEl = document.getElementById('healthContentArea');

  if (loadingEl) loadingEl.style.display = 'block';
  if (emptyEl) emptyEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'none';

  fetch('/api/admin/health-records')
    .then(res => {
      if (!res.ok) throw new Error(`HTTP error ${res.status}`);
      return res.json();
    })
    .then(data => {
      if (data.status !== 'success') throw new Error(data.message);

      allHealthRecordsCache = data.records || [];

      if (loadingEl) loadingEl.style.display = 'none';
      filterHealthTable();
    })
    .catch(err => {
      console.error('Health Records Fetch Error:', err);
      if (loadingEl) loadingEl.style.display = 'none';
      if (emptyEl) {
        emptyEl.style.display = 'block';
        emptyEl.querySelector('h4').textContent = 'Unable to load health records.';
      }
    });
}

function filterHealthTable() {
  const query = (document.getElementById('healthSearchInput')?.value || '').trim().toLowerCase();

  const filtered = allHealthRecordsCache.filter(r => {
    if (!query) return true;
    return (
      (r.athlete_name || '').toLowerCase().includes(query) ||
      (r.athlete_id || '').toLowerCase().includes(query) ||
      (r.primary_sport || '').toLowerCase().includes(query) ||
      (r.record_date || '').toLowerCase().includes(query) ||
      (r.injury_details || '').toLowerCase().includes(query)
    );
  });

  renderHealthTable(filtered);
}

function renderHealthTable(records) {
  const tbody = document.getElementById('healthTableBody');
  const emptyEl = document.getElementById('healthEmptyState');
  const contentEl = document.getElementById('healthContentArea');
  const badgeEl = document.getElementById('totalRecordsBadge');

  if (badgeEl) {
    badgeEl.textContent = `${records.length} Record${records.length === 1 ? '' : 's'}`;
  }

  if (!records || records.length === 0) {
    if (contentEl) contentEl.style.display = 'none';
    if (emptyEl) emptyEl.style.display = 'block';
    return;
  }

  if (emptyEl) emptyEl.style.display = 'none';
  if (contentEl) contentEl.style.display = 'block';

  tbody.innerHTML = records.map(r => `
    <tr>
      <td>
        <a href="/admin/athletes/${r.user_id}" class="fw-bold text-dark text-decoration-none">
          ${escapeHtml(r.athlete_name)}
        </a>
        <div class="fs-8 text-primary font-mono">${r.athlete_id}</div>
      </td>
      <td><span class="badge bg-secondary-subtle text-dark">${escapeHtml(r.primary_sport)}</span></td>
      <td class="fs-7 text-muted fw-medium">${r.record_date}</td>
      <td class="fw-semibold">${r.sleep_hours} hrs</td>
      <td class="fw-semibold">${r.training_hours} hrs</td>
      <td class="fw-semibold">${r.resting_heart_rate} BPM</td>
      <td><span class="badge bg-light text-dark border">${r.fatigue_level} / 10</span></td>
      <td><span class="badge bg-light text-dark border">${r.stress_level} / 10</span></td>
      <td>${r.previous_injury ? '<span class="badge bg-danger-subtle text-danger fw-bold">YES</span>' : '<span class="badge bg-success-subtle text-success">NO</span>'}</td>
    </tr>
  `).join('');
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
