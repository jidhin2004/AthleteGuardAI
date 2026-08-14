/**
 * AthleteGuard AI - Medical History Core JS
 * Handles REST API Fetching, Add/Edit Modals, Safe Deletion Dialog, Client Validation & Empty States
 */

document.addEventListener('DOMContentLoaded', () => {
  initMedicalHistory();
});

let currentDeleteTarget = { category: '', id: null };

async function initMedicalHistory() {
  bindModalOpenButtons();
  bindFormSubmits();
  bindDeleteConfirmation();
  await fetchAndRenderMedicalHistory();
}

async function fetchAndRenderMedicalHistory() {
  try {
    const response = await fetch('/api/medical-history');
    if (!response.ok) throw new Error('HTTP error ' + response.status);

    const data = await response.json();
    if (data.status !== 'success') throw new Error(data.message);

    // Update Summary Stat Cards
    const injCount = document.getElementById('summaryInjuriesCount');
    const condCount = document.getElementById('summaryConditionsCount');
    const allCount = document.getElementById('summaryAllergiesCount');
    const surgCount = document.getElementById('summarySurgeriesCount');

    if (injCount) injCount.textContent = data.summary.injuries_count;
    if (condCount) condCount.textContent = data.summary.conditions_count;
    if (allCount) allCount.textContent = data.summary.allergies_count;
    if (surgCount) surgCount.textContent = data.summary.surgeries_count;

    // Render 5 Sections
    renderInjuries(data.injuries);
    renderConditions(data.conditions);
    renderAllergies(data.allergies);
    renderMedications(data.medications);
    renderSurgeries(data.surgeries);

  } catch (err) {
    console.error("Fetch Medical History Error:", err);
    showNotification('danger', 'Unable to load medical history records. Please try again.');
  }
}

/* ==========================================
   SECTION RENDERERS WITH EMPTY STATES
   ========================================== */
function renderInjuries(items) {
  const container = document.getElementById('injuriesContainer');
  if (!container) return;

  if (!items || items.length === 0) {
    container.innerHTML = `
      <div class="col-12">
        <div class="empty-state-container">
          <div class="empty-state-icon">
            <i class="fa-solid fa-bone"></i>
          </div>
          <h4 class="empty-state-title">No previous injuries recorded</h4>
          <p class="empty-state-text">Keep your injury log up to date to help the AI accurately evaluate your injury readiness.</p>
          <button type="button" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold" onclick="openInjuryModal()">
            <i class="fa-solid fa-plus me-1"></i> Add Injury
          </button>
        </div>
      </div>`;
    return;
  }

  container.innerHTML = items.map(item => {
    let sevBadge = 'severity-badge-moderate';
    if (item.severity === 'Mild') sevBadge = 'severity-badge-mild';
    if (item.severity === 'Severe') sevBadge = 'severity-badge-severe';

    return `
      <div class="col-md-6 col-lg-4">
        <div class="medical-item-card">
          <div class="d-flex justify-content-between align-items-start mb-2">
            <div>
              <div class="medical-card-title">${escapeHtml(item.injury_type)}</div>
              <div class="medical-card-sub"><i class="fa-solid fa-location-dot text-primary me-1"></i>${escapeHtml(item.body_part)} • ${escapeHtml(item.injury_date)}</div>
            </div>
            <div class="d-flex gap-1">
              <button class="medical-action-btn" title="Edit Injury" onclick="openInjuryModal(${item.id}, ${escapeJsonString(item)})">
                <i class="fa-solid fa-pen-to-square"></i>
              </button>
              <button class="medical-action-btn btn-delete" title="Delete Injury" onclick="confirmDelete('injuries', ${item.id})">
                <i class="fa-solid fa-trash-can"></i>
              </button>
            </div>
          </div>
          <div class="d-flex align-items-center gap-2 mb-2">
            <span class="${sevBadge}">${escapeHtml(item.severity)}</span>
            <span class="status-badge-recovered">${escapeHtml(item.recovery_status)}</span>
          </div>
          <div class="fs-8 text-muted"><strong>Treatment:</strong> ${escapeHtml(item.treatment)}</div>
          ${item.notes ? `<div class="fs-8 text-muted mt-1"><em>${escapeHtml(item.notes)}</em></div>` : ''}
        </div>
      </div>`;
  }).join('');
}

function renderConditions(items) {
  const container = document.getElementById('conditionsContainer');
  if (!container) return;

  if (!items || items.length === 0) {
    container.innerHTML = `
      <div class="col-12">
        <div class="empty-state-container py-4">
          <div class="empty-state-icon" style="width:44px; height:44px; font-size:1.2rem;">
            <i class="fa-solid fa-stethoscope"></i>
          </div>
          <h5 class="empty-state-title fs-6">No medical conditions recorded</h5>
          <p class="empty-state-text fs-7 mb-2">Log any diagnosed medical conditions or health concerns.</p>
          <button type="button" class="btn btn-outline-primary btn-sm rounded-pill px-3 fw-semibold" onclick="openConditionModal()">
            <i class="fa-solid fa-plus me-1"></i> Add Condition
          </button>
        </div>
      </div>`;
    return;
  }

  container.innerHTML = items.map(item => `
    <div class="col-md-6 col-lg-4">
      <div class="medical-item-card">
        <div class="d-flex justify-content-between align-items-start mb-2">
          <div>
            <div class="medical-card-title">${escapeHtml(item.condition_name)}</div>
            <div class="medical-card-sub">Diagnosed: ${escapeHtml(item.diagnosis_date)}</div>
          </div>
          <div class="d-flex gap-1">
            <button class="medical-action-btn" title="Edit Condition" onclick="openConditionModal(${item.id}, ${escapeJsonString(item)})">
              <i class="fa-solid fa-pen-to-square"></i>
            </button>
            <button class="medical-action-btn btn-delete" title="Delete Condition" onclick="confirmDelete('conditions', ${item.id})">
              <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>
        </div>
        <span class="badge bg-primary-subtle text-primary border fw-semibold">${escapeHtml(item.status)}</span>
        ${item.notes ? `<div class="fs-8 text-muted mt-2"><em>${escapeHtml(item.notes)}</em></div>` : ''}
      </div>
    </div>`).join('');
}

function renderAllergies(items) {
  const container = document.getElementById('allergiesContainer');
  if (!container) return;

  if (!items || items.length === 0) {
    container.innerHTML = `
      <div class="col-12">
        <div class="empty-state-container py-4">
          <div class="empty-state-icon" style="width:44px; height:44px; font-size:1.2rem;">
            <i class="fa-solid fa-hand-dots"></i>
          </div>
          <h5 class="empty-state-title fs-6">No allergies recorded</h5>
          <p class="empty-state-text fs-7 mb-2">Record medication, food, or environmental allergies.</p>
          <button type="button" class="btn btn-outline-primary btn-sm rounded-pill px-3 fw-semibold" onclick="openAllergyModal()">
            <i class="fa-solid fa-plus me-1"></i> Add Allergy
          </button>
        </div>
      </div>`;
    return;
  }

  container.innerHTML = items.map(item => `
    <div class="col-md-6 col-lg-4">
      <div class="medical-item-card">
        <div class="d-flex justify-content-between align-items-start mb-2">
          <div>
            <div class="medical-card-title">${escapeHtml(item.allergy_name)}</div>
            <div class="medical-card-sub">${escapeHtml(item.allergy_type)}</div>
          </div>
          <div class="d-flex gap-1">
            <button class="medical-action-btn" title="Edit Allergy" onclick="openAllergyModal(${item.id}, ${escapeJsonString(item)})">
              <i class="fa-solid fa-pen-to-square"></i>
            </button>
            <button class="medical-action-btn btn-delete" title="Delete Allergy" onclick="confirmDelete('allergies', ${item.id})">
              <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>
        </div>
        <div class="fs-8 text-muted"><strong>Reaction:</strong> ${escapeHtml(item.reaction)}</div>
        ${item.notes ? `<div class="fs-8 text-muted mt-1"><em>${escapeHtml(item.notes)}</em></div>` : ''}
      </div>
    </div>`).join('');
}

function renderMedications(items) {
  const container = document.getElementById('medicationsContainer');
  if (!container) return;

  if (!items || items.length === 0) {
    container.innerHTML = `
      <div class="col-12">
        <div class="empty-state-container py-4">
          <div class="empty-state-icon" style="width:44px; height:44px; font-size:1.2rem;">
            <i class="fa-solid fa-pills"></i>
          </div>
          <h5 class="empty-state-title fs-6">No current medications recorded</h5>
          <p class="empty-state-text fs-7 mb-2">List any active prescription or over-the-counter medications.</p>
          <button type="button" class="btn btn-outline-primary btn-sm rounded-pill px-3 fw-semibold" onclick="openMedicationModal()">
            <i class="fa-solid fa-plus me-1"></i> Add Medication
          </button>
        </div>
      </div>`;
    return;
  }

  container.innerHTML = items.map(item => `
    <div class="col-md-6 col-lg-4">
      <div class="medical-item-card">
        <div class="d-flex justify-content-between align-items-start mb-2">
          <div>
            <div class="medical-card-title">${escapeHtml(item.medication_name)}</div>
            <div class="medical-card-sub">Dosage: ${escapeHtml(item.dosage)} • ${escapeHtml(item.frequency)}</div>
          </div>
          <div class="d-flex gap-1">
            <button class="medical-action-btn" title="Edit Medication" onclick="openMedicationModal(${item.id}, ${escapeJsonString(item)})">
              <i class="fa-solid fa-pen-to-square"></i>
            </button>
            <button class="medical-action-btn btn-delete" title="Delete Medication" onclick="confirmDelete('medications', ${item.id})">
              <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>
        </div>
        <div class="fs-8 text-muted"><strong>Period:</strong> ${escapeHtml(item.start_date)} to ${escapeHtml(item.end_date)}</div>
        ${item.notes ? `<div class="fs-8 text-muted mt-1"><em>${escapeHtml(item.notes)}</em></div>` : ''}
      </div>
    </div>`).join('');
}

function renderSurgeries(items) {
  const container = document.getElementById('surgeriesContainer');
  if (!container) return;

  if (!items || items.length === 0) {
    container.innerHTML = `
      <div class="col-12">
        <div class="empty-state-container py-4">
          <div class="empty-state-icon" style="width:44px; height:44px; font-size:1.2rem;">
            <i class="fa-solid fa-hospital-user"></i>
          </div>
          <h5 class="empty-state-title fs-6">No surgery history recorded</h5>
          <p class="empty-state-text fs-7 mb-2">Record past surgical procedures and hospitalizations.</p>
          <button type="button" class="btn btn-outline-primary btn-sm rounded-pill px-3 fw-semibold" onclick="openSurgeryModal()">
            <i class="fa-solid fa-plus me-1"></i> Add Surgery
          </button>
        </div>
      </div>`;
    return;
  }

  container.innerHTML = items.map(item => `
    <div class="col-md-6 col-lg-4">
      <div class="medical-item-card">
        <div class="d-flex justify-content-between align-items-start mb-2">
          <div>
            <div class="medical-card-title">${escapeHtml(item.surgery_name)}</div>
            <div class="medical-card-sub">${escapeHtml(item.body_part)} • ${escapeHtml(item.surgery_date)}</div>
          </div>
          <div class="d-flex gap-1">
            <button class="medical-action-btn" title="Edit Surgery" onclick="openSurgeryModal(${item.id}, ${escapeJsonString(item)})">
              <i class="fa-solid fa-pen-to-square"></i>
            </button>
            <button class="medical-action-btn btn-delete" title="Delete Surgery" onclick="confirmDelete('surgeries', ${item.id})">
              <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>
        </div>
        <div class="fs-8 text-muted"><strong>Facility:</strong> ${escapeHtml(item.hospital_clinic)}</div>
        ${item.notes ? `<div class="fs-8 text-muted mt-1"><em>${escapeHtml(item.notes)}</em></div>` : ''}
      </div>
    </div>`).join('');
}

/* ==========================================
   MODAL CONTROLS & FORM POPULATION
   ========================================== */
function bindModalOpenButtons() {
  const btnInj = document.getElementById('btnOpenAddInjury');
  const btnCond = document.getElementById('btnOpenAddCondition');
  const btnAll = document.getElementById('btnOpenAddAllergy');
  const btnMed = document.getElementById('btnOpenAddMedication');
  const btnSurg = document.getElementById('btnOpenAddSurgery');

  if (btnInj) btnInj.addEventListener('click', () => openInjuryModal());
  if (btnCond) btnCond.addEventListener('click', () => openConditionModal());
  if (btnAll) btnAll.addEventListener('click', () => openAllergyModal());
  if (btnMed) btnMed.addEventListener('click', () => openMedicationModal());
  if (btnSurg) btnSurg.addEventListener('click', () => openSurgeryModal());
}

function openInjuryModal(id = null, data = null) {
  const form = document.getElementById('injuryForm');
  if (form) form.reset();

  document.getElementById('injuryId').value = id || '';
  document.getElementById('injuryModalLabel').innerHTML = id ? '<i class="fa-solid fa-pen-to-square text-info me-2"></i> Edit Injury Record' : '<i class="fa-solid fa-bone text-danger me-2"></i> Add Injury Record';

  if (data) {
    document.getElementById('injuryType').value = data.injury_type || '';
    document.getElementById('bodyPart').value = data.body_part || '';
    document.getElementById('injuryDate').value = data.injury_date || '';
    document.getElementById('injurySeverity').value = data.severity || 'Moderate';
    document.getElementById('injuryTreatment').value = data.treatment !== 'N/A' ? data.treatment : '';
    document.getElementById('recoveryStatus').value = data.recovery_status || 'Recovered';
    document.getElementById('injuryNotes').value = data.notes || '';
  }

  bootstrap.Modal.getOrCreateInstance(document.getElementById('injuryModal')).show();
}

function openConditionModal(id = null, data = null) {
  const form = document.getElementById('conditionForm');
  if (form) form.reset();

  document.getElementById('conditionId').value = id || '';
  document.getElementById('conditionModalLabel').innerHTML = id ? '<i class="fa-solid fa-pen-to-square text-info me-2"></i> Edit Medical Condition' : '<i class="fa-solid fa-file-waveform text-primary me-2"></i> Add Medical Condition';

  if (data) {
    document.getElementById('conditionName').value = data.condition_name || '';
    document.getElementById('diagnosisDate').value = data.diagnosis_date !== 'N/A' ? data.diagnosis_date : '';
    document.getElementById('conditionStatus').value = data.status || 'Active';
    document.getElementById('conditionNotes').value = data.notes || '';
  }

  bootstrap.Modal.getOrCreateInstance(document.getElementById('conditionModal')).show();
}

function openAllergyModal(id = null, data = null) {
  const form = document.getElementById('allergyForm');
  if (form) form.reset();

  document.getElementById('allergyId').value = id || '';
  document.getElementById('allergyModalLabel').innerHTML = id ? '<i class="fa-solid fa-pen-to-square text-info me-2"></i> Edit Allergy Record' : '<i class="fa-solid fa-hand-dots text-warning me-2"></i> Add Allergy Record';

  if (data) {
    document.getElementById('allergyName').value = data.allergy_name || '';
    document.getElementById('allergyType').value = data.allergy_type || 'Medication';
    document.getElementById('allergyReaction').value = data.reaction !== 'N/A' ? data.reaction : '';
    document.getElementById('allergyNotes').value = data.notes || '';
  }

  bootstrap.Modal.getOrCreateInstance(document.getElementById('allergyModal')).show();
}

function openMedicationModal(id = null, data = null) {
  const form = document.getElementById('medicationForm');
  if (form) form.reset();

  document.getElementById('medicationId').value = id || '';
  document.getElementById('medicationModalLabel').innerHTML = id ? '<i class="fa-solid fa-pen-to-square text-info me-2"></i> Edit Medication' : '<i class="fa-solid fa-pills text-info me-2"></i> Add Medication';

  if (data) {
    document.getElementById('medicationName').value = data.medication_name || '';
    document.getElementById('medDosage').value = data.dosage !== 'N/A' ? data.dosage : '';
    document.getElementById('medFrequency').value = data.frequency !== 'N/A' ? data.frequency : '';
    document.getElementById('medStartDate').value = data.start_date !== 'N/A' ? data.start_date : '';
    document.getElementById('medEndDate').value = data.end_date !== 'Ongoing' ? data.end_date : '';
    document.getElementById('medNotes').value = data.notes || '';
  }

  bootstrap.Modal.getOrCreateInstance(document.getElementById('medicationModal')).show();
}

function openSurgeryModal(id = null, data = null) {
  const form = document.getElementById('surgeryForm');
  if (form) form.reset();

  document.getElementById('surgeryId').value = id || '';
  document.getElementById('surgeryModalLabel').innerHTML = id ? '<i class="fa-solid fa-pen-to-square text-info me-2"></i> Edit Surgery Record' : '<i class="fa-solid fa-syringe text-success me-2"></i> Add Surgery Record';

  if (data) {
    document.getElementById('surgeryName').value = data.surgery_name || '';
    document.getElementById('surgeryBodyPart').value = data.body_part || '';
    document.getElementById('surgeryDate').value = data.surgery_date || '';
    document.getElementById('hospitalClinic').value = data.hospital_clinic !== 'N/A' ? data.hospital_clinic : '';
    document.getElementById('surgeryNotes').value = data.notes || '';
  }

  bootstrap.Modal.getOrCreateInstance(document.getElementById('surgeryModal')).show();
}

/* ==========================================
   FORM SUBMITS (POST / PUT)
   ========================================== */
function bindFormSubmits() {
  const formInj = document.getElementById('injuryForm');
  const formCond = document.getElementById('conditionForm');
  const formAll = document.getElementById('allergyForm');
  const formMed = document.getElementById('medicationForm');
  const formSurg = document.getElementById('surgeryForm');

  if (formInj) formInj.addEventListener('submit', (e) => handleRecordSubmit(e, 'injuries', 'injuryId', 'btnSaveInjury', 'injuryModal'));
  if (formCond) formCond.addEventListener('submit', (e) => handleRecordSubmit(e, 'conditions', 'conditionId', 'btnSaveCondition', 'conditionModal'));
  if (formAll) formAll.addEventListener('submit', (e) => handleRecordSubmit(e, 'allergies', 'allergyId', 'btnSaveAllergy', 'allergyModal'));
  if (formMed) formMed.addEventListener('submit', (e) => handleRecordSubmit(e, 'medications', 'medicationId', 'btnSaveMedication', 'medicationModal'));
  if (formSurg) formSurg.addEventListener('submit', (e) => handleRecordSubmit(e, 'surgeries', 'surgeryId', 'btnSaveSurgery', 'surgeryModal'));
}

async function handleRecordSubmit(e, endpoint, idElemId, btnId, modalId) {
  e.preventDefault();

  const idVal = document.getElementById(idElemId).value;
  const isEdit = Boolean(idVal);
  const btn = document.getElementById(btnId);

  // Collect Payload
  let payload = {};
  if (endpoint === 'injuries') {
    const type = document.getElementById('injuryType').value.trim();
    const part = document.getElementById('bodyPart').value.trim();
    const date = document.getElementById('injuryDate').value;
    if (!type || !part || !date) {
      if (!type) markInvalid('injuryType', 'injuryTypeError', 'Injury Type is required.');
      if (!part) markInvalid('bodyPart', 'bodyPartError', 'Body Part is required.');
      if (!date) markInvalid('injuryDate', 'injuryDateError', 'Injury Date is required.');
      return;
    }
    payload = {
      injury_type: type,
      body_part: part,
      injury_date: date,
      severity: document.getElementById('injurySeverity').value,
      treatment: document.getElementById('injuryTreatment').value.trim(),
      recovery_status: document.getElementById('recoveryStatus').value,
      notes: document.getElementById('injuryNotes').value.trim()
    };
  } else if (endpoint === 'conditions') {
    const name = document.getElementById('conditionName').value.trim();
    if (!name) {
      markInvalid('conditionName', 'conditionNameError', 'Condition Name is required.');
      return;
    }
    payload = {
      condition_name: name,
      diagnosis_date: document.getElementById('diagnosisDate').value,
      status: document.getElementById('conditionStatus').value,
      notes: document.getElementById('conditionNotes').value.trim()
    };
  } else if (endpoint === 'allergies') {
    const name = document.getElementById('allergyName').value.trim();
    if (!name) {
      markInvalid('allergyName', 'allergyNameError', 'Allergy Name is required.');
      return;
    }
    payload = {
      allergy_name: name,
      allergy_type: document.getElementById('allergyType').value,
      reaction: document.getElementById('allergyReaction').value.trim(),
      notes: document.getElementById('allergyNotes').value.trim()
    };
  } else if (endpoint === 'medications') {
    const name = document.getElementById('medicationName').value.trim();
    if (!name) {
      markInvalid('medicationName', 'medicationNameError', 'Medication Name is required.');
      return;
    }
    payload = {
      medication_name: name,
      dosage: document.getElementById('medDosage').value.trim(),
      frequency: document.getElementById('medFrequency').value.trim(),
      start_date: document.getElementById('medStartDate').value,
      end_date: document.getElementById('medEndDate').value,
      notes: document.getElementById('medNotes').value.trim()
    };
  } else if (endpoint === 'surgeries') {
    const name = document.getElementById('surgeryName').value.trim();
    const part = document.getElementById('surgeryBodyPart').value.trim();
    const date = document.getElementById('surgeryDate').value;
    if (!name || !part || !date) {
      if (!name) markInvalid('surgeryName', 'surgeryNameError', 'Surgery Name is required.');
      if (!part) markInvalid('surgeryBodyPart', 'surgeryBodyPartError', 'Body Part is required.');
      if (!date) markInvalid('surgeryDate', 'surgeryDateError', 'Surgery Date is required.');
      return;
    }
    payload = {
      surgery_name: name,
      body_part: part,
      surgery_date: date,
      hospital_clinic: document.getElementById('hospitalClinic').value.trim(),
      notes: document.getElementById('surgeryNotes').value.trim()
    };
  }

  // Submit API call
  const url = isEdit ? `/api/${endpoint}/${idVal}` : `/api/${endpoint}`;
  const method = isEdit ? 'PUT' : 'POST';

  const origBtnText = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span> Saving...';

  try {
    const response = await fetch(url, {
      method: method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const resData = await response.json();
    if (!response.ok || resData.status !== 'success') {
      throw new Error(resData.message || 'Unable to save medical record.');
    }

    // Close Modal
    const modalElem = document.getElementById(modalId);
    bootstrap.Modal.getInstance(modalElem).hide();

    // Show Success Toast
    const msg = isEdit ? 'Record updated successfully.' : 'Record added successfully.';
    showNotification('success', resData.message || msg);

    // Refresh UI
    await fetchAndRenderMedicalHistory();

  } catch (err) {
    console.error("Save Record Error:", err);
    showNotification('danger', err.message || 'Unable to save medical history. Please try again.');
  } finally {
    btn.disabled = false;
    btn.innerHTML = origBtnText;
  }
}

/* ==========================================
   SAFE DELETE CONFIRMATION DIALOG
   ========================================== */
function bindDeleteConfirmation() {
  const btnConfirm = document.getElementById('btnConfirmDelete');
  if (btnConfirm) {
    btnConfirm.addEventListener('click', handleRecordDelete);
  }
}

function confirmDelete(category, id) {
  currentDeleteTarget = { category, id };
  bootstrap.Modal.getOrCreateInstance(document.getElementById('deleteConfirmModal')).show();
}

async function handleRecordDelete() {
  const { category, id } = currentDeleteTarget;
  if (!category || !id) return;

  const btn = document.getElementById('btnConfirmDelete');
  const origBtnText = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span> Deleting...';

  try {
    const response = await fetch(`/api/${category}/${id}`, {
      method: 'DELETE'
    });

    const resData = await response.json();
    if (!response.ok || resData.status !== 'success') {
      throw new Error(resData.message || 'Unable to delete record.');
    }

    bootstrap.Modal.getInstance(document.getElementById('deleteConfirmModal')).hide();
    showNotification('success', resData.message || 'Record deleted successfully.');

    await fetchAndRenderMedicalHistory();

  } catch (err) {
    console.error("Delete Error:", err);
    showNotification('danger', err.message || 'Unable to delete medical record. Please try again.');
  } finally {
    btn.disabled = false;
    btn.innerHTML = origBtnText;
    currentDeleteTarget = { category: '', id: null };
  }
}

/* ==========================================
   HELPER UTILITIES
   ========================================== */
function showNotification(type, message) {
  const succAlert = document.getElementById('medicalSuccessAlert');
  const succText = document.getElementById('medicalSuccessText');
  const errAlert = document.getElementById('medicalErrorAlert');
  const errText = document.getElementById('medicalErrorText');

  if (type === 'success' && succAlert) {
    if (succText) succText.textContent = message;
    succAlert.style.display = 'flex';
    if (errAlert) errAlert.style.display = 'none';
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(() => { succAlert.style.display = 'none'; }, 4000);
  } else if (errAlert) {
    if (errText) errText.textContent = message;
    errAlert.style.display = 'flex';
    if (succAlert) succAlert.style.display = 'none';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
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

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function escapeJsonString(obj) {
  return JSON.stringify(obj).replace(/'/g, "&apos;").replace(/"/g, "&quot;");
}
