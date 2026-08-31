/**
 * AthleteGuard AI - Dynamic Prediction History
 * Handles API fetching, dynamic table population, search filtering,
 * risk level filtering, pagination, error/empty states, and details modal.
 */

document.addEventListener('DOMContentLoaded', () => {
  initPredictionHistory();
});

let allRecords = [];
let filteredRecords = [];
let currentPage = 1;
const ITEMS_PER_PAGE = 10;

function initPredictionHistory() {
  bindEventListeners();
  fetchPredictionHistory();
}

function bindEventListeners() {
  const searchInput = document.getElementById('historySearchInput');
  const riskFilter = document.getElementById('historyRiskFilter');
  const btnRetry = document.getElementById('btnRetryHistory');

  if (searchInput) {
    searchInput.addEventListener('input', () => {
      applyFilters();
    });
  }

  if (riskFilter) {
    riskFilter.addEventListener('change', () => {
      applyFilters();
    });
  }

  if (btnRetry) {
    btnRetry.addEventListener('click', () => {
      fetchPredictionHistory();
    });
  }
}

async function fetchPredictionHistory() {
  showState('loading');

  try {
    const response = await fetch('/api/predictions/history');
    const data = await response.json();

    if (!response.ok || data.status !== 'success') {
      throw new Error(data.message || 'Unable to load prediction history. Please try again.');
    }

    allRecords = data.records || [];
    filteredRecords = [...allRecords];
    currentPage = 1;

    updateHeaderBadge(allRecords.length);

    if (allRecords.length === 0) {
      showState('empty');
    } else {
      showState('content');
      applyFilters();
    }
  } catch (err) {
    console.error('Fetch Prediction History Error:', err);
    showState('error');
  }
}

function updateHeaderBadge(totalCount) {
  const badge = document.getElementById('totalRecordsBadge');
  if (badge) {
    badge.textContent = `Total: ${totalCount} Record${totalCount === 1 ? '' : 's'}`;
  }
}

function applyFilters() {
  const searchInput = document.getElementById('historySearchInput');
  const riskFilter = document.getElementById('historyRiskFilter');

  const query = searchInput ? searchInput.value.trim().toLowerCase() : '';
  const selectedRisk = riskFilter ? riskFilter.value.toLowerCase() : 'all';

  filteredRecords = allRecords.filter(rec => {
    // Risk Filter
    if (selectedRisk !== 'all') {
      const recRisk = (rec.risk_label || '').toLowerCase();
      if (!recRisk.includes(selectedRisk)) {
        return false;
      }
    }

    // Search Query (Date, Risk Label, Injury Details, Stats)
    if (query) {
      const dateStr = formatDate(rec.record_date).toLowerCase();
      const rawDate = (rec.record_date || '').toLowerCase();
      const riskLabel = (rec.risk_label || '').toLowerCase();
      const details = (rec.injury_details || '').toLowerCase();

      const matches = dateStr.includes(query) ||
                      rawDate.includes(query) ||
                      riskLabel.includes(query) ||
                      details.includes(query);
      if (!matches) return false;
    }

    return true;
  });

  currentPage = 1;
  renderTable();
}

function renderTable() {
  const tbody = document.getElementById('historyTableBody');
  const noMatchesAlert = document.getElementById('noFilterMatchesAlert');
  if (!tbody) return;

  tbody.innerHTML = '';

  if (filteredRecords.length === 0) {
    if (noMatchesAlert) noMatchesAlert.style.display = 'block';
    renderPagination(0);
    return;
  } else {
    if (noMatchesAlert) noMatchesAlert.style.display = 'none';
  }

  const totalPages = Math.ceil(filteredRecords.length / ITEMS_PER_PAGE);
  if (currentPage > totalPages) currentPage = totalPages;
  if (currentPage < 1) currentPage = 1;

  const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
  const pageRecords = filteredRecords.slice(startIndex, startIndex + ITEMS_PER_PAGE);

  pageRecords.forEach(rec => {
    const tr = document.createElement('tr');
    
    const riskBadgeHtml = getRiskBadgeHtml(rec.risk_label);
    const scoreColorClass = getScoreColorClass(rec.risk_label);
    const prevInjText = rec.previous_injury ? '<span class="badge bg-warning-subtle text-dark fw-bold">Yes</span>' : '<span class="text-muted">No</span>';

    tr.innerHTML = `
      <td class="fw-semibold text-dark">${formatDate(rec.record_date)}</td>
      <td>${rec.sleep_hours} hrs</td>
      <td>${rec.training_hours} hrs</td>
      <td>${rec.resting_heart_rate} BPM</td>
      <td>${rec.fatigue_level}/10</td>
      <td>${rec.stress_level}/10</td>
      <td>${prevInjText}</td>
      <td>${riskBadgeHtml}</td>
      <td class="fw-bold ${scoreColorClass}">${rec.risk_score !== null ? rec.risk_score + '%' : 'N/A'}</td>
      <td class="text-center">
        <button type="button" class="btn btn-sm btn-outline-primary rounded-pill px-3 fw-bold" onclick="viewRecordDetails(${rec.id})">
          <i class="fa-solid fa-eye me-1"></i> View
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });

  renderPagination(filteredRecords.length);
}

function renderPagination(totalItems) {
  const container = document.getElementById('historyPagination');
  if (!container) return;

  if (totalItems <= ITEMS_PER_PAGE) {
    container.style.display = 'none';
    return;
  }

  container.style.display = 'flex';
  const totalPages = Math.ceil(totalItems / ITEMS_PER_PAGE);

  let html = `
    <ul class="pagination pagination-sm m-0">
      <li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
        <button class="page-link" onclick="changePage(${currentPage - 1})"><i class="fa-solid fa-chevron-left"></i></button>
      </li>
  `;

  for (let p = 1; p <= totalPages; p++) {
    html += `
      <li class="page-item ${p === currentPage ? 'active' : ''}">
        <button class="page-link" onclick="changePage(${p})">${p}</button>
      </li>
    `;
  }

  html += `
      <li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
        <button class="page-link" onclick="changePage(${currentPage + 1})"><i class="fa-solid fa-chevron-right"></i></button>
      </li>
    </ul>
  `;

  container.innerHTML = html;
}

function changePage(page) {
  const totalPages = Math.ceil(filteredRecords.length / ITEMS_PER_PAGE);
  if (page < 1 || page > totalPages) return;
  currentPage = page;
  renderTable();
}

function viewRecordDetails(recordId) {
  const rec = allRecords.find(r => r.id === recordId);
  if (!rec) return;

  document.getElementById('modalDetailDate').textContent = formatDate(rec.record_date);
  document.getElementById('modalDetailSleep').textContent = `${rec.sleep_hours} Hours`;
  document.getElementById('modalDetailTraining').textContent = `${rec.training_hours} Hours`;
  document.getElementById('modalDetailHeartRate').textContent = `${rec.resting_heart_rate} BPM`;
  document.getElementById('modalDetailFatigue').textContent = `${rec.fatigue_level} / 10`;
  document.getElementById('modalDetailStress').textContent = `${rec.stress_level} / 10`;

  const prevInjElem = document.getElementById('modalDetailPrevInj');
  if (prevInjElem) {
    if (rec.previous_injury) {
      prevInjElem.innerHTML = `<span class="badge bg-warning text-dark">Yes</span> ${rec.injury_details ? `<span class="text-muted ms-2">(${escapeHtml(rec.injury_details)})</span>` : ''}`;
    } else {
      prevInjElem.innerHTML = `<span class="badge bg-secondary">No</span>`;
    }
  }

  document.getElementById('modalDetailRiskBadge').innerHTML = getRiskBadgeHtml(rec.risk_label);
  
  const scoreElem = document.getElementById('modalDetailRiskScore');
  if (scoreElem) {
    scoreElem.textContent = rec.risk_score !== null ? `${rec.risk_score}%` : 'N/A';
    scoreElem.className = `fw-bold fs-4 ${getScoreColorClass(rec.risk_label)}`;
  }

  const modalElem = document.getElementById('predictionDetailsModal');
  if (modalElem && window.bootstrap) {
    const modal = new bootstrap.Modal(modalElem);
    modal.show();
  }
}

function getRiskBadgeHtml(riskLabel) {
  const label = (riskLabel || 'Low Risk').toUpperCase();
  if (label.includes('LOW')) {
    return `<span class="badge bg-success"><i class="fa-solid fa-circle-check me-1"></i>Low Risk</span>`;
  } else if (label.includes('MEDIUM')) {
    return `<span class="badge bg-warning text-dark"><i class="fa-solid fa-triangle-exclamation me-1"></i>Medium Risk</span>`;
  } else {
    return `<span class="badge bg-danger"><i class="fa-solid fa-circle-xmark me-1"></i>High Risk</span>`;
  }
}

function getScoreColorClass(riskLabel) {
  const label = (riskLabel || 'Low Risk').toUpperCase();
  if (label.includes('LOW')) {
    return 'text-success';
  } else if (label.includes('MEDIUM')) {
    return 'text-warning';
  } else {
    return 'text-danger';
  }
}

function showState(state) {
  const loading = document.getElementById('historyLoadingState');
  const error = document.getElementById('historyErrorState');
  const empty = document.getElementById('historyEmptyState');
  const content = document.getElementById('historyContentArea');

  if (loading) loading.style.display = state === 'loading' ? 'block' : 'none';
  if (error) error.style.display = state === 'error' ? 'block' : 'none';
  if (empty) empty.style.display = state === 'empty' ? 'block' : 'none';
  if (content) content.style.display = state === 'content' ? 'block' : 'none';
}

function formatDate(dateStr) {
  if (!dateStr) return 'N/A';
  try {
    const parts = dateStr.split('-');
    if (parts.length === 3) {
      const year = parseInt(parts[0]);
      const month = parseInt(parts[1]) - 1;
      const day = parseInt(parts[2]);
      const d = new Date(year, month, day);
      return d.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
    }
    return dateStr;
  } catch (e) {
    return dateStr;
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
