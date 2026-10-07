/**
 * AthleteGuard AI - Daily Health Monitoring Core JS
 * Handles Live Form Input Syncing, Today's Health Summary, Client Validation,
 * Duplicate Record Detection, and Scikit-Learn Random Forest Prediction API
 */

document.addEventListener('DOMContentLoaded', () => {
  initDailyMonitoring();
});

let isPreviousInjurySelected = false;

function initDailyMonitoring() {
  bindSliderSyncing();
  bindFormSubmit();
  checkTodayRecordStatus();
}

function bindSliderSyncing() {
  const sleepSlider = document.getElementById('sleepHoursSlider');
  const sleepInput = document.getElementById('sleepHoursInput');
  const sleepDisplay = document.getElementById('sleepDisplayVal');
  const summarySleep = document.getElementById('summarySleep');

  if (sleepSlider && sleepInput) {
    sleepSlider.addEventListener('input', (e) => {
      const val = parseFloat(e.target.value).toFixed(1);
      sleepInput.value = val;
      if (sleepDisplay) sleepDisplay.textContent = `${val} hrs`;
      if (summarySleep) summarySleep.textContent = `${val} hrs`;
    });

    sleepInput.addEventListener('input', (e) => {
      let val = parseFloat(e.target.value) || 0;
      val = Math.min(12, Math.max(0, val));
      sleepSlider.value = val;
      if (sleepDisplay) sleepDisplay.textContent = `${val} hrs`;
      if (summarySleep) summarySleep.textContent = `${val} hrs`;
    });
  }

  const trainingSlider = document.getElementById('trainingHoursSlider');
  const trainingInput = document.getElementById('trainingHoursInput');
  const trainingDisplay = document.getElementById('trainingDisplayVal');
  const summaryTraining = document.getElementById('summaryTraining');

  if (trainingSlider && trainingInput) {
    trainingSlider.addEventListener('input', (e) => {
      const val = parseFloat(e.target.value).toFixed(1);
      trainingInput.value = val;
      if (trainingDisplay) trainingDisplay.textContent = `${val} hrs`;
      if (summaryTraining) summaryTraining.textContent = `${val} hrs`;
    });

    trainingInput.addEventListener('input', (e) => {
      let val = parseFloat(e.target.value) || 0;
      val = Math.min(12, Math.max(0, val));
      trainingSlider.value = val;
      if (trainingDisplay) trainingDisplay.textContent = `${val} hrs`;
      if (summaryTraining) summaryTraining.textContent = `${val} hrs`;
    });
  }

  const hrInput = document.getElementById('restingHeartRate');
  const summaryHR = document.getElementById('summaryHeartRate');
  if (hrInput) {
    hrInput.addEventListener('input', (e) => {
      const val = parseInt(e.target.value) || '--';
      if (summaryHR) summaryHR.textContent = `${val} BPM`;
    });
  }

  const fatigueSlider = document.getElementById('fatigueSlider');
  const fatigueDisplay = document.getElementById('fatigueDisplayVal');
  const summaryFatigue = document.getElementById('summaryFatigue');
  if (fatigueSlider) {
    fatigueSlider.addEventListener('input', (e) => {
      const val = e.target.value;
      if (fatigueDisplay) fatigueDisplay.textContent = `${val} / 10`;
      if (summaryFatigue) summaryFatigue.textContent = `${val}/10`;
    });
  }

  const stressSlider = document.getElementById('stressSlider');
  const stressDisplay = document.getElementById('stressDisplayVal');
  const summaryStress = document.getElementById('summaryStress');
  if (stressSlider) {
    stressSlider.addEventListener('input', (e) => {
      const val = e.target.value;
      if (stressDisplay) stressDisplay.textContent = `${val} / 10`;
      if (summaryStress) summaryStress.textContent = `${val}/10`;
    });
  }
}

function setPreviousInjury(hasInj) {
  isPreviousInjurySelected = hasInj;
  const valElem = document.getElementById('previousInjuryVal');
  if (valElem) valElem.value = hasInj ? 'true' : 'false';

  const btnNo = document.getElementById('btnPrevInjNo');
  const btnYes = document.getElementById('btnPrevInjYes');
  const detailsContainer = document.getElementById('injuryDetailsContainer');
  const summaryPrevInj = document.getElementById('summaryPrevInj');

  if (hasInj) {
    if (btnYes) btnYes.classList.add('active');
    if (btnNo) btnNo.classList.remove('active');
    if (detailsContainer) detailsContainer.style.display = 'block';
    if (summaryPrevInj) summaryPrevInj.textContent = 'Yes';
  } else {
    if (btnNo) btnNo.classList.add('active');
    if (btnYes) btnYes.classList.remove('active');
    if (detailsContainer) detailsContainer.style.display = 'none';
    if (summaryPrevInj) summaryPrevInj.textContent = 'No';
  }
}

async function checkTodayRecordStatus() {
  try {
    const response = await fetch('/api/daily-monitoring/today');
    if (!response.ok) return;

    const data = await response.json();
    if (data.status === 'success' && data.has_today_record && data.record) {
      const rec = data.record;

      if (document.getElementById('sleepHoursSlider')) document.getElementById('sleepHoursSlider').value = rec.sleep_hours;
      if (document.getElementById('sleepHoursInput')) document.getElementById('sleepHoursInput').value = rec.sleep_hours;
      if (document.getElementById('sleepDisplayVal')) document.getElementById('sleepDisplayVal').textContent = `${rec.sleep_hours} hrs`;
      if (document.getElementById('summarySleep')) document.getElementById('summarySleep').textContent = `${rec.sleep_hours} hrs`;

      if (document.getElementById('trainingHoursSlider')) document.getElementById('trainingHoursSlider').value = rec.training_hours;
      if (document.getElementById('trainingHoursInput')) document.getElementById('trainingHoursInput').value = rec.training_hours;
      if (document.getElementById('trainingDisplayVal')) document.getElementById('trainingDisplayVal').textContent = `${rec.training_hours} hrs`;
      if (document.getElementById('summaryTraining')) document.getElementById('summaryTraining').textContent = `${rec.training_hours} hrs`;

      if (document.getElementById('restingHeartRate')) document.getElementById('restingHeartRate').value = rec.resting_heart_rate;
      if (document.getElementById('summaryHeartRate')) document.getElementById('summaryHeartRate').textContent = `${rec.resting_heart_rate} BPM`;

      if (document.getElementById('fatigueSlider')) document.getElementById('fatigueSlider').value = rec.fatigue_level;
      if (document.getElementById('fatigueDisplayVal')) document.getElementById('fatigueDisplayVal').textContent = `${rec.fatigue_level} / 10`;
      if (document.getElementById('summaryFatigue')) document.getElementById('summaryFatigue').textContent = `${rec.fatigue_level}/10`;

      if (document.getElementById('stressSlider')) document.getElementById('stressSlider').value = rec.stress_level;
      if (document.getElementById('stressDisplayVal')) document.getElementById('stressDisplayVal').textContent = `${rec.stress_level} / 10`;
      if (document.getElementById('summaryStress')) document.getElementById('summaryStress').textContent = `${rec.stress_level}/10`;

      setPreviousInjury(rec.previous_injury);
      if (rec.injury_details && document.getElementById('injuryDetailsText')) {
        document.getElementById('injuryDetailsText').value = rec.injury_details;
      }

      // Show Today's Record Banner
      const todayBanner = document.getElementById('todayRecordedBanner');
      if (todayBanner) todayBanner.style.display = 'flex';

      const btnUpdateRec = document.getElementById('btnToggleUpdateRecord');
      if (btnUpdateRec) {
        btnUpdateRec.addEventListener('click', () => {
          const formCard = document.getElementById('healthMonitoringForm');
          if (formCard) formCard.scrollIntoView({ behavior: 'smooth' });
        });
      }

      // Render prediction result if available
      if (rec.risk_score !== null && rec.risk_score !== undefined) {
        const riskLabel = rec.risk_label || 'Low Risk';
        const badgeColor = riskLabel.toLowerCase().includes('high') ? 'danger' : (riskLabel.toLowerCase().includes('medium') ? 'warning' : 'success');
        renderPredictionResult({
          risk_score: rec.risk_score,
          risk_label: riskLabel,
          badge_color: badgeColor,
          contributing_factors: ['Recorded daily health parameters for today.'],
          recommendations: ['Continue maintaining current recovery and workload balance.']
        });
      }
    }
  } catch (err) {
    console.error("Check today record error:", err);
  }
}

function bindFormSubmit() {
  const form = document.getElementById('healthMonitoringForm');
  if (form) {
    form.addEventListener('submit', handleFormSubmit);
  }
}

async function handleFormSubmit(e) {
  e.preventDefault();

  const btnPredict = document.getElementById('btnPredictRisk');
  const alertSuccess = document.getElementById('monitoringSuccessAlert');
  const alertError = document.getElementById('monitoringErrorAlert');
  const errorText = document.getElementById('monitoringErrorText');

  if (alertError) alertError.style.display = 'none';

  const sleepInputEl = document.getElementById('sleepHoursInput');
  const trainingInputEl = document.getElementById('trainingHoursInput');
  const rhrInputEl = document.getElementById('restingHeartRate');
  const fatigueSliderEl = document.getElementById('fatigueSlider');
  const stressSliderEl = document.getElementById('stressSlider');
  const prevInjValEl = document.getElementById('previousInjuryVal');
  const injDetailsEl = document.getElementById('injuryDetailsText');

  const sleepHours = sleepInputEl ? parseFloat(sleepInputEl.value) : 7.5;
  const trainingHours = trainingInputEl ? parseFloat(trainingInputEl.value) : 3.5;
  const restingHeartRate = rhrInputEl ? parseInt(rhrInputEl.value) : 65;
  const fatigueLevel = fatigueSliderEl ? parseInt(fatigueSliderEl.value) : 5;
  const stressLevel = stressSliderEl ? parseInt(stressSliderEl.value) : 5;
  const previousInjury = prevInjValEl ? (prevInjValEl.value === 'true') : false;
  const injuryDetails = injDetailsEl ? injDetailsEl.value.trim() : '';

  let isValid = true;

  if (isNaN(sleepHours) || sleepHours < 0 || sleepHours > 12) {
    markInvalid('sleepHoursInput', 'sleepHoursError', 'Sleep hours must be between 0 and 12.');
    isValid = false;
  } else {
    markValid('sleepHoursInput', 'sleepHoursError');
  }

  if (isNaN(trainingHours) || trainingHours < 0 || trainingHours > 12) {
    markInvalid('trainingHoursInput', 'trainingHoursError', 'Training hours must be between 0 and 12.');
    isValid = false;
  } else {
    markValid('trainingHoursInput', 'trainingHoursError');
  }

  if (isNaN(restingHeartRate) || restingHeartRate < 30 || restingHeartRate > 180) {
    markInvalid('restingHeartRate', 'heartRateError', 'Enter resting heart rate between 30 and 180 BPM.');
    isValid = false;
  } else {
    markValid('restingHeartRate', 'heartRateError');
  }

  if (!isValid) return;

  const csrfToken = (typeof getCsrfToken === 'function' ? getCsrfToken() : '') || 
                    document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || 
                    document.querySelector('input[name="csrf_token"]')?.value || '';

  const payload = {
    sleep_hours: sleepHours,
    training_hours: trainingHours,
    resting_heart_rate: restingHeartRate,
    fatigue_level: fatigueLevel,
    stress_level: stressLevel,
    previous_injury: previousInjury,
    injury_details: injuryDetails,
    csrf_token: csrfToken
  };

  const origBtnText = btnPredict ? btnPredict.innerHTML : '<i class="fa-solid fa-shield-halved me-2"></i> Predict Injury Risk';
  if (btnPredict) {
    btnPredict.disabled = true;
    btnPredict.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Analyzing Health Data...';
  }

  try {
    const response = await fetch('/api/predictions/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(payload)
    });

    const resData = await response.json();

    if (!response.ok || resData.status !== 'success') {
      throw new Error(resData.message || 'Unable to analyze your health data right now. Please try again.');
    }

    // Render ML Prediction Result Card
    if (resData.prediction) {
      renderPredictionResult(resData.prediction);
    }

    // Show Success Alert
    if (alertSuccess) {
      alertSuccess.style.display = 'flex';
      window.scrollTo({ top: 0, behavior: 'smooth' });
      setTimeout(() => { alertSuccess.style.display = 'none'; }, 4000);
    }

    // Show Today Recorded Banner
    const todayBanner = document.getElementById('todayRecordedBanner');
    if (todayBanner) todayBanner.style.display = 'flex';

  } catch (err) {
    console.error("Prediction Submit Error:", err);
    if (alertError) {
      if (errorText) errorText.textContent = err.message || 'Unable to analyze your health data right now. Please try again.';
      alertError.style.display = 'flex';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  } finally {
    if (btnPredict) {
      btnPredict.disabled = false;
      btnPredict.innerHTML = origBtnText;
    }
  }
}

function renderPredictionResult(pred) {
  const card = document.getElementById('predictionResultCard');
  const scoreElem = document.getElementById('resultRiskScore');
  const badgeElem = document.getElementById('resultRiskBadge');
  const factorsList = document.getElementById('resultFactorsList');
  const recsText = document.getElementById('resultRecommendationsText');

  if (!card) return;

  if (scoreElem) {
    const scoreVal = (pred.risk_score !== null && pred.risk_score !== undefined) ? pred.risk_score : 0;
    scoreElem.textContent = `${scoreVal}%`;
  }
  
  if (badgeElem) {
    const riskLabel = pred.risk_label || 'Low Risk';
    const badgeColor = pred.badge_color || (riskLabel.toLowerCase().includes('high') ? 'danger' : (riskLabel.toLowerCase().includes('medium') ? 'warning' : 'success'));
    badgeElem.textContent = riskLabel.toUpperCase();
    badgeElem.className = `badge fs-6 px-3 py-1.5 rounded-pill fw-bold bg-${badgeColor}`;
  }

  if (factorsList && pred.contributing_factors) {
    factorsList.innerHTML = pred.contributing_factors.map(f => 
      `<li class="mb-1"><i class="fa-solid fa-angle-right text-info me-2"></i>${escapeHtml(f)}</li>`
    ).join('');
  }

  if (recsText && pred.recommendations) {
    recsText.innerHTML = pred.recommendations.map(r => 
      `<div class="mb-1"><i class="fa-solid fa-circle-check text-success me-2"></i>${escapeHtml(r)}</div>`
    ).join('');
  }

  card.style.display = 'block';
  card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function markInvalid(inputId, errorId, message) {
  const input = document.getElementById(inputId);
  const errDiv = document.getElementById(errorId);
  if (input) input.classList.add('is-invalid');
  if (errDiv) {
    errDiv.textContent = message;
    errDiv.style.display = 'block';
  }
}

function markValid(inputId, errorId) {
  const input = document.getElementById(inputId);
  const errDiv = document.getElementById(errorId);
  if (input) input.classList.remove('is-invalid');
  if (errDiv) errDiv.style.display = 'none';
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
