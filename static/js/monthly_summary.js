/**
 * AthleteGuard AI — Monthly Summary Controller
 * Dynamically fetches 30-day health metrics, risk distribution breakdown, and longitudinal risk score trend graph.
 */

let monthlyChartInstance = null;

document.addEventListener('DOMContentLoaded', () => {
    fetchMonthlySummary();
});

function fetchMonthlySummary() {
    fetch('/api/monthly-summary')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const emptyState = document.getElementById('monthlyEmptyState');
            const contentContainer = document.getElementById('monthlyContentContainer');

            if (!data || !data.has_data || data.total_records === 0) {
                if (emptyState) emptyState.classList.remove('d-none');
                if (contentContainer) contentContainer.classList.add('d-none');
                return;
            }

            // Show main content and hide empty state
            if (emptyState) emptyState.classList.add('d-none');
            if (contentContainer) contentContainer.classList.remove('d-none');

            // Populate 8 Summary Stat Cards
            const avg = data.averages || {};
            setElementText('statTotalRecords', data.total_records || 0);
            setElementText('statAvgSleep', `${avg.sleep_hours !== undefined ? avg.sleep_hours : 0} hrs`);
            setElementText('statAvgTraining', `${avg.training_hours !== undefined ? avg.training_hours : 0} hrs`);
            setElementText('statAvgRHR', `${avg.resting_heart_rate !== undefined ? avg.resting_heart_rate : 0} bpm`);
            setElementText('statAvgFatigue', `${avg.fatigue_level !== undefined ? avg.fatigue_level : 0} / 10`);
            setElementText('statAvgStress', `${avg.stress_level !== undefined ? avg.stress_level : 0} / 10`);
            setElementText('statAvgRisk', `${avg.risk_score !== undefined ? avg.risk_score : 0}%`);
            setElementText('statTotalPredictions', data.prediction_count || 0);

            // Update Header Risk Badge
            const badge = document.getElementById('monthlyBadgeAvgRisk');
            if (badge) {
                const score = avg.risk_score || 0;
                badge.textContent = `Avg Risk: ${score}%`;
                badge.className = 'badge fs-7 px-3 py-2 rounded-pill ' + (
                    score > 65 ? 'bg-danger' :
                    score > 30 ? 'bg-warning text-dark' : 'bg-primary'
                );
            }

            // Populate Risk Level Breakdown Counts
            const dist = data.risk_distribution || {};
            setElementText('cntLowRisk', dist.low || 0);
            setElementText('cntMediumRisk', dist.medium || 0);
            setElementText('cntHighRisk', dist.high || 0);

            // Render 30-Day Risk Score Trend Chart
            renderMonthlyChart(data.trend || []);
        })
        .catch(err => {
            console.error('Error loading monthly summary:', err);
            const emptyState = document.getElementById('monthlyEmptyState');
            const contentContainer = document.getElementById('monthlyContentContainer');
            if (emptyState) emptyState.classList.remove('d-none');
            if (contentContainer) contentContainer.classList.add('d-none');
        });
}

function renderMonthlyChart(trendData) {
    const canvas = document.getElementById('monthlyRiskChart');
    if (!canvas) return;

    if (monthlyChartInstance) {
        monthlyChartInstance.destroy();
        monthlyChartInstance = null;
    }

    if (!trendData || trendData.length === 0) {
        return;
    }

    const labels = trendData.map(t => formatDateLabel(t.date));
    const scores = trendData.map(t => t.risk_score);

    const ctx = canvas.getContext('2d');
    const gradient = ctx.createLinearGradient(0, 0, 0, 260);
    gradient.addColorStop(0, 'rgba(13, 110, 253, 0.35)');
    gradient.addColorStop(1, 'rgba(13, 110, 253, 0.0)');

    monthlyChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: '30-Day Injury Risk Score (%)',
                data: scores,
                borderColor: '#0d6efd',
                borderWidth: 2.5,
                backgroundColor: gradient,
                fill: true,
                tension: 0.3,
                pointBackgroundColor: '#0d6efd',
                pointBorderColor: '#ffffff',
                pointBorderWidth: 1.5,
                pointRadius: 4,
                pointHoverRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return ` Risk Score: ${context.parsed.y}%`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    min: 0,
                    max: 100,
                    ticks: {
                        callback: function(value) { return value + '%'; },
                        stepSize: 20
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

function setElementText(id, text) {
    const el = document.getElementById(id);
    if (el) el.textContent = text;
}

function formatDateLabel(dateStr) {
    if (!dateStr) return '';
    try {
        const parts = dateStr.split('-');
        if (parts.length === 3) {
            const dateObj = new Date(parts[0], parts[1] - 1, parts[2]);
            return dateObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        }
    } catch (e) {
        // Fallback
    }
    return dateStr;
}
