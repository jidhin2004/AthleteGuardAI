/**
 * AthleteGuard AI - Dashboard Core JS
 * Handles API Data Fetching, Chart.js Integration, Time Filtering & Mobile Sidebar Toggle
 */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Sidebar Drawer Toggle
  const sidebar = document.getElementById('appSidebar');
  const toggleBtn = document.getElementById('sidebarToggle');

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('show');
    });

    document.addEventListener('click', (e) => {
      if (window.innerWidth <= 991.98) {
        if (!sidebar.contains(e.target) && !toggleBtn.contains(e.target)) {
          sidebar.classList.remove('show');
        }
      }
    });
  }

  // Dynamic Date Display (e.g., "Thursday, 13 August 2026")
  const dateElem = document.getElementById('currentDateDisplay');
  if (dateElem) {
    const now = new Date();
    const options = { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' };
    dateElem.textContent = now.toLocaleDateString('en-US', options);
  }

  // Dashboard Data Service & Chart Management
  initDashboardApp();
});

let healthTrendsChartInstance = null;
let riskDistChartInstance = null;
let currentTrendFilter = '7_days';
let dashboardDataCache = null;

async function initDashboardApp() {
  const loadingOverlay = document.getElementById('dashboardLoading');
  const errorBanner = document.getElementById('dashboardErrorBanner');
  const mainContent = document.getElementById('dashboardMainGrid');
  const emptyState = document.getElementById('dashboardEmptyState');

  try {
    if (loadingOverlay) loadingOverlay.style.display = 'block';
    if (errorBanner) errorBanner.style.display = 'none';
    if (emptyState) emptyState.style.display = 'none';

    // Fetch dashboard data from Flask API
    const response = await fetch('/api/dashboard-data');
    if (!response.ok) throw new Error(`HTTP Error ${response.status}`);

    const data = await response.json();
    dashboardDataCache = data;

    if (loadingOverlay) loadingOverlay.style.display = 'none';

    // Update Model Status Indicator in Top Header
    const modelStatusElem = document.getElementById('headerModelStatus');
    if (modelStatusElem && data.model_status) {
      modelStatusElem.textContent = data.model_status;
    }

    // Check if user has predictions
    if (!data.has_predictions) {
      if (mainContent) mainContent.style.display = 'none';
      if (emptyState) emptyState.style.display = 'block';
      return;
    }

    if (mainContent) mainContent.style.display = 'block';

    // Populate Statistics Cards
    updateStatCards(data.stats);

    // Populate Current Risk Gauge & Prediction Summary
    updateRiskGauge(data.stats.injury_risk_percent, data.stats.risk_level, data.stats.last_prediction_date, data.risk_summary);

    // Populate Today's Health Overview
    updateTodaysHealthOverview(data.todays_health_overview);

    // Initialize Chart.js Line Chart (Health Trends)
    renderHealthTrendsChart(data.health_trends[currentTrendFilter]);

    // Initialize Chart.js Doughnut Chart (Risk Distribution)
    renderRiskDistributionChart(data.risk_distribution);

    // Bind Time Filter Buttons (7 Days / 30 Days)
    setupTimeFilterListeners();

  } catch (err) {
    console.error("Dashboard initialization error:", err);
    if (loadingOverlay) loadingOverlay.style.display = 'none';
    if (mainContent) mainContent.style.display = 'none';
    if (errorBanner) errorBanner.style.display = 'block';
  }
}

function updateStatCards(stats) {
  const riskVal = document.getElementById('statRiskPercent');
  const totalVal = document.getElementById('statTotalPredictions');
  const sleepVal = document.getElementById('statAvgSleep');
  const trainVal = document.getElementById('statAvgTraining');

  if (riskVal) riskVal.textContent = `${stats.injury_risk_percent}%`;
  if (totalVal) totalVal.textContent = stats.total_predictions;
  if (sleepVal) sleepVal.textContent = `${stats.avg_sleep_hrs} hrs`;
  if (trainVal) trainVal.textContent = `${stats.avg_training_hrs} hrs`;
}

function updateRiskGauge(percent, level, lastDate, summary) {
  const gauge = document.getElementById('riskCircleGauge');
  const numElem = document.getElementById('riskGaugeNumber');
  const badgeElem = document.getElementById('riskLevelBadge');
  const headingElem = document.getElementById('riskHeadingText');
  const lastDateElem = document.getElementById('riskLastPredictionDate');

  // Summary box elements
  const summaryLevel = document.getElementById('summaryRiskLevel');
  const summaryScore = document.getElementById('summaryRiskScore');
  const summaryDate = document.getElementById('summaryPredictedOn');

  if (numElem) numElem.textContent = `${percent}%`;
  if (lastDateElem) lastDateElem.textContent = lastDate || '13 August 2026';

  let colorHex = '#22c55e'; // Low Risk (Green)
  let badgeClass = 'badge bg-success';
  let headingText = 'Low Injury Risk Detected';

  if (percent > 65) {
    colorHex = '#ef4444'; // High Risk (Red)
    badgeClass = 'badge bg-danger';
    headingText = 'High Injury Risk Detected';
  } else if (percent > 30) {
    colorHex = '#f59e0b'; // Medium Risk (Orange)
    badgeClass = 'badge bg-warning text-dark';
    headingText = 'Medium Injury Risk Detected';
  }

  if (gauge) {
    gauge.style.background = `conic-gradient(${colorHex} 0% ${percent}%, #e2e8f0 ${percent}% 100%)`;
    gauge.style.boxShadow = `0 4px 14px ${colorHex}40`;
  }

  if (badgeElem) {
    badgeElem.className = badgeClass;
    badgeElem.textContent = `${level.toUpperCase()}`;
  }

  if (headingElem) {
    headingElem.textContent = headingText;
    headingElem.style.color = colorHex;
  }

  // Populate Prediction Summary Box
  if (summary) {
    if (summaryLevel) {
      summaryLevel.textContent = summary.risk_level;
      summaryLevel.style.color = colorHex;
    }
    if (summaryScore) summaryScore.textContent = `${summary.risk_percent}%`;
    if (summaryDate) summaryDate.textContent = summary.predicted_on;
  }
}

function updateTodaysHealthOverview(today) {
  const container = document.getElementById('todaysOverviewContainer');
  const fallback = document.getElementById('todaysOverviewFallback');

  if (!today || !today.has_today_data) {
    if (container) container.style.display = 'none';
    if (fallback) fallback.style.display = 'block';
    return;
  }

  if (container) container.style.display = 'flex';
  if (fallback) fallback.style.display = 'none';

  const sleepElem = document.getElementById('todaySleepVal');
  const trainElem = document.getElementById('todayTrainingVal');
  const hrElem = document.getElementById('todayHeartRateVal');
  const fatigueElem = document.getElementById('todayFatigueVal');
  const stressElem = document.getElementById('todayStressVal');
  const injuryElem = document.getElementById('todayInjuryVal');

  if (sleepElem) sleepElem.textContent = today.sleep_hrs;
  if (trainElem) trainElem.textContent = today.training_hrs;
  if (hrElem) hrElem.textContent = today.heart_rate;
  if (fatigueElem) fatigueElem.textContent = today.fatigue;
  if (stressElem) stressElem.textContent = today.stress;
  if (injuryElem) injuryElem.textContent = today.previous_injury;
}

function renderHealthTrendsChart(trendData) {
  const ctx = document.getElementById('healthTrendsChartCanvas');
  if (!ctx) return;

  if (healthTrendsChartInstance) {
    healthTrendsChartInstance.destroy();
  }

  healthTrendsChartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: trendData.labels,
      datasets: [
        {
          label: 'Sleep Hours (hrs)',
          data: trendData.sleep,
          borderColor: '#1d4ed8',
          backgroundColor: 'rgba(29, 78, 216, 0.08)',
          borderWidth: 2.5,
          tension: 0.35,
          fill: true,
          pointRadius: 4,
          pointBackgroundColor: '#1d4ed8'
        },
        {
          label: 'Training Hours (hrs)',
          data: trendData.training,
          borderColor: '#38bdf8',
          backgroundColor: 'rgba(56, 189, 248, 0.08)',
          borderWidth: 2.5,
          tension: 0.35,
          fill: true,
          pointRadius: 4,
          pointBackgroundColor: '#38bdf8'
        },
        {
          label: 'Resting HR (bpm)',
          data: trendData.resting_hr,
          borderColor: '#ef4444',
          borderWidth: 2,
          borderDash: [5, 5],
          tension: 0.35,
          fill: false,
          pointRadius: 3,
          pointBackgroundColor: '#ef4444'
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          labels: {
            font: { family: "'Inter', sans-serif", size: 12, weight: '500' },
            usePointStyle: true,
            boxWidth: 8
          }
        },
        tooltip: {
          backgroundColor: '#060d1b',
          titleFont: { family: "'Outfit', sans-serif", size: 13, weight: '700' },
          bodyFont: { family: "'Inter', sans-serif", size: 12 },
          padding: 10,
          cornerRadius: 8
        }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: { font: { family: "'Inter', sans-serif", size: 11 }, color: '#64748b' }
        },
        y: {
          grid: { color: '#f1f5f9' },
          ticks: { font: { family: "'Inter', sans-serif", size: 11 }, color: '#64748b' }
        }
      }
    }
  });
}

function renderRiskDistributionChart(riskData) {
  const ctx = document.getElementById('riskDistributionChartCanvas');
  if (!ctx) return;

  if (riskDistChartInstance) {
    riskDistChartInstance.destroy();
  }

  riskDistChartInstance = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: riskData.labels,
      datasets: [{
        data: riskData.counts,
        backgroundColor: riskData.colors,
        borderWidth: 3,
        borderColor: '#ffffff'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '70%',
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            font: { family: "'Inter', sans-serif", size: 12, weight: '500' },
            usePointStyle: true,
            padding: 15
          }
        },
        tooltip: {
          backgroundColor: '#060d1b',
          titleFont: { family: "'Outfit', sans-serif", size: 13, weight: '700' },
          bodyFont: { family: "'Inter', sans-serif", size: 12 },
          padding: 10,
          cornerRadius: 8
        }
      }
    }
  });
}

function setupTimeFilterListeners() {
  const btn7 = document.getElementById('filter7Days');
  const btn30 = document.getElementById('filter30Days');

  if (btn7 && btn30) {
    btn7.addEventListener('click', () => {
      btn7.classList.add('active', 'btn-primary');
      btn7.classList.remove('btn-outline-secondary');
      btn30.classList.remove('active', 'btn-primary');
      btn30.classList.add('btn-outline-secondary');

      currentTrendFilter = '7_days';
      if (dashboardDataCache) {
        renderHealthTrendsChart(dashboardDataCache.health_trends['7_days']);
      }
    });

    btn30.addEventListener('click', () => {
      btn30.classList.add('active', 'btn-primary');
      btn30.classList.remove('btn-outline-secondary');
      btn7.classList.remove('active', 'btn-primary');
      btn7.classList.add('btn-outline-secondary');

      currentTrendFilter = '30_days';
      if (dashboardDataCache) {
        renderHealthTrendsChart(dashboardDataCache.health_trends['30_days']);
      }
    });
  }
}

function retryDashboardFetch() {
  initDashboardApp();
}
