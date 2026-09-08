/**
 * AthleteGuard AI - Profile Management Core JS
 * Handles Live BMI Calculation, Photo Upload & Preview Modal, Client Validation, and Async API Profile Persistence
 */

document.addEventListener('DOMContentLoaded', () => {
  initProfileApp();
});

let selectedPhotoFile = null;

function initProfileApp() {
  const heightInput = document.getElementById('editHeight');
  const weightInput = document.getElementById('editWeight');

  // Live BMI calculation listeners
  if (heightInput && weightInput) {
    heightInput.addEventListener('input', updateLiveBmiPreview);
    weightInput.addEventListener('input', updateLiveBmiPreview);
  }

  // Profile Form Submit Handler
  const profileForm = document.getElementById('profileEditForm');
  if (profileForm) {
    profileForm.addEventListener('submit', handleProfileSave);
  }

  // Profile Photo Upload Handlers
  initPhotoUploadHandlers();
}

function initPhotoUploadHandlers() {
  const triggerBtn = document.getElementById('btnTriggerPhotoUpload');
  const fileInput = document.getElementById('photoFileInput');
  const savePhotoBtn = document.getElementById('btnSavePhoto');

  if (triggerBtn && fileInput) {
    triggerBtn.addEventListener('click', () => {
      fileInput.click();
    });

    fileInput.addEventListener('change', handleFileSelection);
  }

  if (savePhotoBtn) {
    savePhotoBtn.addEventListener('click', handlePhotoUploadSubmit);
  }
}

function handleFileSelection(e) {
  const file = e.target.files[0];
  if (!file) return;

  const errorBanner = document.getElementById('photoModalErrorBanner');
  const errorText = document.getElementById('photoModalErrorText');
  const mainErrorAlert = document.getElementById('profileErrorAlert');
  const mainErrorText = document.getElementById('profileErrorText');

  if (errorBanner) errorBanner.style.display = 'none';
  if (mainErrorAlert) mainErrorAlert.style.display = 'none';

  // Format and Size Validation
  const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
  const maxSize = 5 * 1024 * 1024; // 5 MB

  if (!validTypes.includes(file.type.toLowerCase())) {
    showUploadValidationError('Please upload a JPG, PNG, or WEBP image under 5 MB.');
    e.target.value = '';
    return;
  }

  if (file.size > maxSize) {
    showUploadValidationError('Please upload a JPG, PNG, or WEBP image under 5 MB.');
    e.target.value = '';
    return;
  }

  selectedPhotoFile = file;

  // FileReader preview
  const reader = new FileReader();
  reader.onload = function(evt) {
    const previewImg = document.getElementById('photoPreviewImg');
    const previewInitials = document.getElementById('photoPreviewInitials');

    if (previewImg) {
      previewImg.src = evt.target.result;
      previewImg.style.display = 'block';
    }
    if (previewInitials) previewInitials.style.display = 'none';

    // Show Preview / Crop Modal
    const modalElem = document.getElementById('photoUploadModal');
    if (modalElem) {
      const modalInstance = bootstrap.Modal.getOrCreateInstance(modalElem);
      modalInstance.show();
    }
  };

  reader.readAsDataURL(file);
}

function showUploadValidationError(message) {
  const mainErrorAlert = document.getElementById('profileErrorAlert');
  const mainErrorText = document.getElementById('profileErrorText');

  if (mainErrorAlert && mainErrorText) {
    mainErrorText.textContent = message;
    mainErrorAlert.style.display = 'flex';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

async function handlePhotoUploadSubmit() {
  if (!selectedPhotoFile) {
    showUploadValidationError('No photo file selected.');
    return;
  }

  const savePhotoBtn = document.getElementById('btnSavePhoto');
  const errorBanner = document.getElementById('photoModalErrorBanner');
  const errorText = document.getElementById('photoModalErrorText');
  const successAlert = document.getElementById('profileSuccessAlert');
  const successText = document.getElementById('profileSuccessText');

  if (errorBanner) errorBanner.style.display = 'none';

  // Change button state to Uploading...
  const originalText = savePhotoBtn.innerHTML;
  savePhotoBtn.disabled = true;
  savePhotoBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Uploading...';

  try {
    const formData = new FormData();
    formData.append('profile_photo', selectedPhotoFile);

    const response = await fetch('/api/profile/photo', {
      method: 'POST',
      body: formData
    });

    const resData = await response.json();

    if (!response.ok || resData.status !== 'success') {
      throw new Error(resData.message || 'Please upload a JPG, PNG, or WEBP image under 5 MB.');
    }

    // Success -> Hide Modal
    const modalElem = document.getElementById('photoUploadModal');
    if (modalElem) {
      const modalInstance = bootstrap.Modal.getInstance(modalElem);
      if (modalInstance) modalInstance.hide();
    }

    // Update Avatars dynamically across page
    updateAllAvatarsUI(resData.profile_photo_url);

    // Show Success Toast
    if (successAlert) {
      if (successText) successText.textContent = 'Profile photo updated successfully.';
      successAlert.style.display = 'flex';
      window.scrollTo({ top: 0, behavior: 'smooth' });
      setTimeout(() => {
        successAlert.style.display = 'none';
      }, 5000);
    }

    // Clear file input
    const fileInput = document.getElementById('photoFileInput');
    if (fileInput) fileInput.value = '';
    selectedPhotoFile = null;

  } catch (err) {
    console.error("Photo Upload Error:", err);
    if (errorText) errorText.textContent = err.message || 'Unable to update your profile photo. Please try again.';
    if (errorBanner) errorBanner.style.display = 'block';
  } finally {
    savePhotoBtn.disabled = false;
    savePhotoBtn.innerHTML = originalText;
  }
}

function updateAllAvatarsUI(photoUrl) {
  // Summary Header Card Avatar
  const summaryAvatarContainer = document.getElementById('viewSummaryAvatar');
  if (summaryAvatarContainer) {
    summaryAvatarContainer.innerHTML = `<img src="${photoUrl}" alt="Athlete Profile Photo" class="profile-avatar-img" id="viewSummaryPhoto">`;
  }

  // Sidebar Avatar
  const sidebarAvatarCircle = document.getElementById('sidebarAvatarCircle');
  if (sidebarAvatarCircle) {
    sidebarAvatarCircle.innerHTML = `<img src="${photoUrl}" alt="Athlete Profile Photo">`;
  }

  // Topbar Avatar
  const topbarAvatarCircle = document.getElementById('topbarAvatarCircle');
  if (topbarAvatarCircle) {
    topbarAvatarCircle.innerHTML = `<img src="${photoUrl}" alt="Athlete Profile Photo">`;
  }
}

function updateLiveBmiPreview() {
  const hRaw = document.getElementById('editHeight').value.trim();
  const wRaw = document.getElementById('editWeight').value.trim();
  const bmiBadge = document.getElementById('liveBmiBadge');

  const hVal = parseFloat(hRaw);
  const wVal = parseFloat(wRaw);

  if (!hRaw || !wRaw || isNaN(hVal) || isNaN(wVal) || hVal <= 0 || wVal <= 0) {
    if (bmiBadge) {
      bmiBadge.className = 'badge bg-secondary';
      bmiBadge.textContent = 'BMI: N/A';
    }
    return;
  }

  const hMeters = hVal / 100.0;
  const bmi = (wVal / (hMeters * hMeters)).toFixed(1);

  let category = 'Normal';
  let badgeClass = 'badge bg-success';

  if (bmi < 18.5) {
    category = 'Underweight';
    badgeClass = 'badge bg-info text-dark';
  } else if (bmi >= 18.5 && bmi <= 24.9) {
    category = 'Normal';
    badgeClass = 'badge bg-success';
  } else if (bmi >= 25.0 && bmi <= 29.9) {
    category = 'Overweight';
    badgeClass = 'badge bg-warning text-dark';
  } else {
    category = 'Obese';
    badgeClass = 'badge bg-danger';
  }

  if (bmiBadge) {
    bmiBadge.className = badgeClass;
    bmiBadge.textContent = `BMI: ${bmi} (${category})`;
  }
}

async function handleProfileSave(e) {
  e.preventDefault();

  const form = e.target;
  const submitBtn = document.getElementById('btnSaveProfile');
  const successAlert = document.getElementById('profileSuccessAlert');
  const successText = document.getElementById('profileSuccessText');
  const errorAlert = document.getElementById('profileErrorAlert');
  const errorText = document.getElementById('profileErrorText');

  if (errorAlert) errorAlert.style.display = 'none';

  const fullName = document.getElementById('editFullName').value.trim();
  const ageRaw = document.getElementById('editAge').value.trim();
  const email = document.getElementById('editEmail').value.trim();
  const heightRaw = document.getElementById('editHeight').value.trim();
  const weightRaw = document.getElementById('editWeight').value.trim();
  const phone = document.getElementById('editPhone').value.trim();

  let isValid = true;

  if (!fullName) {
    markInvalid('editFullName', 'fullNameError', 'Full Name is required.');
    isValid = false;
  } else {
    markValid('editFullName', 'fullNameError');
  }

  const age = parseInt(ageRaw);
  if (!ageRaw || isNaN(age) || age <= 0 || age > 120) {
    markInvalid('editAge', 'ageError', 'Enter a valid positive age.');
    isValid = false;
  } else {
    markValid('editAge', 'ageError');
  }

  if (!email || !email.includes('@')) {
    markInvalid('editEmail', 'emailError', 'Enter a valid email address.');
    isValid = false;
  } else {
    markValid('editEmail', 'emailError');
  }

  let height = null;
  if (heightRaw !== '') {
    height = parseFloat(heightRaw);
    if (isNaN(height) || height <= 0 || height > 300) {
      markInvalid('editHeight', 'heightError', 'Enter a positive height in cm.');
      isValid = false;
    } else {
      markValid('editHeight', 'heightError');
    }
  } else {
    markValid('editHeight', 'heightError');
  }

  let weight = null;
  if (weightRaw !== '') {
    weight = parseFloat(weightRaw);
    if (isNaN(weight) || weight <= 0 || weight > 500) {
      markInvalid('editWeight', 'weightError', 'Enter a positive weight in kg.');
      isValid = false;
    } else {
      markValid('editWeight', 'weightError');
    }
  } else {
    markValid('editWeight', 'weightError');
  }

  markValid('editPhone', 'phoneError');

  if (!isValid) return;

  const payload = {
    full_name: fullName,
    age: age,
    gender: document.getElementById('editGender').value,
    email: email,
    phone: phone,
    primary_sport: document.getElementById('editSport').value,
    height_cm: height,
    weight_kg: weight,
    emergency_name: document.getElementById('editEmergencyName').value.trim(),
    emergency_relationship: document.getElementById('editEmergencyRelationship').value.trim(),
    emergency_phone: document.getElementById('editEmergencyPhone').value.trim()
  };

  const originalBtnText = submitBtn.innerHTML;
  submitBtn.disabled = true;
  submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Saving...';

  try {
    const response = await fetch('/api/profile', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const resData = await response.json();

    if (!response.ok || resData.status !== 'success') {
      throw new Error(resData.message || 'Unable to update your profile. Please try again.');
    }

    const modalElem = document.getElementById('editProfileModal');
    const modalInstance = bootstrap.Modal.getInstance(modalElem) || new bootstrap.Modal(modalElem);
    modalInstance.hide();

    if (successAlert) {
      if (successText) successText.textContent = 'Profile updated successfully.';
      successAlert.style.display = 'flex';
      window.scrollTo({ top: 0, behavior: 'smooth' });
      setTimeout(() => {
        successAlert.style.display = 'none';
      }, 5000);
    }

    updateProfileViewUI(resData.user);

  } catch (err) {
    console.error("Profile Save Error:", err);
    if (errorText) errorText.textContent = err.message || 'Unable to update your profile. Please try again.';
    if (errorAlert) errorAlert.style.display = 'flex';
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = originalBtnText;
  }
}

function updateProfileViewUI(u) {
  const summaryName = document.getElementById('viewSummaryName');
  const summarySport = document.getElementById('viewSummarySport');
  const summaryEmail = document.getElementById('viewSummaryEmail');

  if (summaryName) summaryName.textContent = u.full_name;
  if (summarySport) summarySport.textContent = `${u.primary_sport} Athlete`;
  if (summaryEmail) summaryEmail.textContent = u.email;

  const nameVal = document.getElementById('viewFullName');
  const ageVal = document.getElementById('viewAge');
  const genderVal = document.getElementById('viewGender');
  const emailVal = document.getElementById('viewEmail');
  const phoneVal = document.getElementById('viewPhone');

  if (nameVal) nameVal.textContent = u.full_name;
  if (ageVal) ageVal.textContent = u.age ? `${u.age} years` : 'Not provided';
  if (genderVal) genderVal.textContent = u.gender || 'Not provided';
  if (emailVal) emailVal.textContent = u.email;
  if (phoneVal) phoneVal.textContent = u.phone || 'Not provided';

  const sportVal = document.getElementById('viewSport');
  const heightVal = document.getElementById('viewHeight');
  const weightVal = document.getElementById('viewWeight');
  const bmiVal = document.getElementById('viewBmiVal');
  const bmiBadge = document.getElementById('viewBmiBadge');

  if (sportVal) sportVal.textContent = u.primary_sport;
  if (heightVal) heightVal.textContent = u.height_cm ? `${u.height_cm} cm` : 'Not provided';
  if (weightVal) weightVal.textContent = u.weight_kg ? `${u.weight_kg} kg` : 'Not provided';
  if (bmiVal) bmiVal.textContent = u.bmi ? u.bmi : 'N/A';
  if (bmiBadge && u.bmi_category) {
    bmiBadge.className = u.bmi_category.badge_class;
    bmiBadge.textContent = u.bmi_category.label;
  }

  const emName = document.getElementById('viewEmergencyName');
  const emRel = document.getElementById('viewEmergencyRel');
  const emPhone = document.getElementById('viewEmergencyPhone');

  if (emName) emName.textContent = u.emergency_name || 'Not provided';
  if (emRel) emRel.textContent = u.emergency_relationship || 'Not provided';
  if (emPhone) emPhone.textContent = u.emergency_phone || 'Not provided';
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
