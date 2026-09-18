/**
 * AthleteGuard AI - Registration Form Validation & Password Strength Gauge
 */

document.addEventListener('DOMContentLoaded', function () {
  const regForm = document.getElementById('registerForm');
  if (!regForm) return;

  const fullNameInput = document.getElementById('regFullName');
  const dobInput = document.getElementById('regDOB');
  const genderSelect = document.getElementById('regGender');
  const sportSelect = document.getElementById('regSport');
  const emailInput = document.getElementById('regEmail');
  const passwordInput = document.getElementById('regPassword');
  const confirmPasswordInput = document.getElementById('regConfirmPassword');
  const termsCheckbox = document.getElementById('regTerms');

  const strengthBars = [
    document.getElementById('bar1'),
    document.getElementById('bar2'),
    document.getElementById('bar3')
  ];
  const strengthLabel = document.getElementById('strengthLabel');

  function setValid(input, errorId) {
    if (input) input.classList.remove('is-invalid');
    if (errorId) {
      const errElem = document.getElementById(errorId);
      if (errElem) {
        errElem.style.display = 'none';
        errElem.classList.remove('d-block');
      }
    }
  }

  function setInvalid(input, errorId, message) {
    if (!input) return;
    input.classList.add('is-invalid');
    const errElem = document.getElementById(errorId);
    if (errElem) {
      if (message) errElem.textContent = message;
      errElem.style.display = 'block';
      errElem.classList.add('d-block');
    }
  }

  function validateFullName(name) {
    if (!name || name.trim() === '') {
      return 'Full Name is required.';
    }
    const trimmed = name.trim();
    if (trimmed.length < 2) {
      return 'Full Name must be at least 2 characters long.';
    }
    if (!/^[a-zA-Z\s'-]+$/.test(trimmed)) {
      return 'Full Name should contain letters and spaces only.';
    }
    return null;
  }

  function validateEmail(email) {
    if (!email || email.trim() === '') {
      return 'Email address is required.';
    }
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!re.test(String(email).toLowerCase())) {
      return 'Please enter a valid email address (e.g. athlete@example.com).';
    }
    return null;
  }

  function validateDOB(dobVal) {
    if (!dobVal || dobVal.trim() === '') {
      return 'Date of Birth is required.';
    }
    const parts = dobVal.split('-');
    if (parts.length !== 3) {
      return 'Please select a valid Date of Birth.';
    }
    const selectedDate = new Date(Number(parts[0]), Number(parts[1]) - 1, Number(parts[2]));
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    if (isNaN(selectedDate.getTime())) {
      return 'Please select a valid Date of Birth.';
    }

    if (selectedDate > today) {
      return 'Date of Birth cannot be in the future.';
    }

    let age = today.getFullYear() - selectedDate.getFullYear();
    const m = today.getMonth() - selectedDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < selectedDate.getDate())) {
      age--;
    }

    if (age < 1 || age > 120) {
      return `Date of Birth produces invalid age (${age}). Must be 1 to 120.`;
    }

    return null;
  }

  // Password Strength Calculation & Detailed Validation (5-Point Rule)
  function getPasswordValidationError(pwd) {
    if (!pwd || pwd.length === 0) {
      return 'Password is required.';
    }
    if (pwd.length < 8) {
      return 'Password must be at least 8 characters long.';
    }
    if (!/[A-Z]/.test(pwd)) {
      return 'Password must contain at least one uppercase letter (A-Z).';
    }
    if (!/[a-z]/.test(pwd)) {
      return 'Password must contain at least one lowercase letter (a-z).';
    }
    if (!/[0-9]/.test(pwd)) {
      return 'Password must contain at least one number (0-9).';
    }
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(pwd)) {
      return 'Password must contain at least one special character (e.g. !@#$%^&*).';
    }
    return null;
  }

  function calculateStrength(pwd) {
    let score = 0;
    if (!pwd) return 0;
    if (pwd.length >= 8) score += 1;
    if (/[A-Z]/.test(pwd) && /[a-z]/.test(pwd)) score += 1;
    if (/[0-9]/.test(pwd)) score += 1;
    if (/[!@#$%^&*(),.?":{}|<>]/.test(pwd)) score += 1;
    return score;
  }

  function updateStrengthMeter(pwd) {
    const score = calculateStrength(pwd);

    // Reset bars
    strengthBars.forEach(bar => {
      if (bar) bar.style.backgroundColor = 'var(--border-color)';
    });

    if (!pwd) {
      if (strengthLabel) strengthLabel.textContent = 'Strength';
      return;
    }

    if (score <= 2) {
      if (strengthBars[0]) strengthBars[0].style.backgroundColor = '#ef4444'; // Red
      if (strengthLabel) {
        strengthLabel.textContent = 'Weak';
        strengthLabel.style.color = '#ef4444';
      }
    } else if (score === 3) {
      if (strengthBars[0]) strengthBars[0].style.backgroundColor = '#f59e0b';
      if (strengthBars[1]) strengthBars[1].style.backgroundColor = '#f59e0b'; // Amber
      if (strengthLabel) {
        strengthLabel.textContent = 'Medium';
        strengthLabel.style.color = '#f59e0b';
      }
    } else {
      strengthBars.forEach(bar => {
        if (bar) bar.style.backgroundColor = '#10b981'; // Green
      });
      if (strengthLabel) {
        strengthLabel.textContent = 'Strong';
        strengthLabel.style.color = '#10b981';
      }
    }
  }

  // Real-time input listeners
  if (fullNameInput) {
    fullNameInput.addEventListener('input', function () {
      const err = validateFullName(this.value);
      if (err) setInvalid(this, 'fullNameError', err);
      else setValid(this, 'fullNameError');
    });
  }

  if (dobInput) {
    dobInput.addEventListener('change', function () {
      const err = validateDOB(this.value);
      if (err) setInvalid(this, 'dobError', err);
      else setValid(this, 'dobError');
    });
    dobInput.addEventListener('input', function () {
      const err = validateDOB(this.value);
      if (err) setInvalid(this, 'dobError', err);
      else setValid(this, 'dobError');
    });
  }

  if (genderSelect) {
    genderSelect.addEventListener('change', function () {
      if (!this.value || (this.value !== 'Male' && this.value !== 'Female')) setInvalid(this, 'genderError', 'Please select Male or Female.');
      else setValid(this, 'genderError');
    });
  }

  if (sportSelect) {
    sportSelect.addEventListener('change', function () {
      if (!this.value || this.value === 'Select Sport') setInvalid(this, 'sportError', 'Please select a primary sport.');
      else setValid(this, 'sportError');
    });
  }

  if (emailInput) {
    emailInput.addEventListener('input', function () {
      const err = validateEmail(this.value);
      if (err) setInvalid(this, 'emailError', err);
      else setValid(this, 'emailError');
    });
  }

  if (passwordInput) {
    passwordInput.addEventListener('input', function () {
      updateStrengthMeter(this.value);
      const pwdError = getPasswordValidationError(this.value);
      if (pwdError) {
        setInvalid(this, 'passwordError', pwdError);
      } else {
        setValid(this, 'passwordError');
      }
      if (confirmPasswordInput && confirmPasswordInput.value.length > 0) {
        if (confirmPasswordInput.value !== this.value) {
          setInvalid(confirmPasswordInput, 'confirmPasswordError', 'Passwords do not match.');
        } else {
          setValid(confirmPasswordInput, 'confirmPasswordError');
        }
      }
    });
  }

  if (confirmPasswordInput) {
    confirmPasswordInput.addEventListener('input', function () {
      if (!this.value || this.value.length === 0) {
        setInvalid(this, 'confirmPasswordError', 'Please confirm your password.');
      } else if (this.value !== passwordInput.value) {
        setInvalid(this, 'confirmPasswordError', 'Passwords do not match.');
      } else {
        setValid(this, 'confirmPasswordError');
      }
    });
  }

  if (termsCheckbox) {
    termsCheckbox.addEventListener('change', function () {
      if (!this.checked) setInvalid(this, 'termsError', 'You must agree to the Terms of Service and Privacy Policy.');
      else setValid(this, 'termsError');
    });
  }

  // Submit Validation
  regForm.addEventListener('submit', function (e) {
    let isValid = true;

    // Full Name
    const nameErr = validateFullName(fullNameInput ? fullNameInput.value : '');
    if (nameErr) {
      setInvalid(fullNameInput, 'fullNameError', nameErr);
      isValid = false;
    } else {
      setValid(fullNameInput, 'fullNameError');
    }

    // Date of Birth
    const dobErr = validateDOB(dobInput ? dobInput.value : '');
    if (dobErr) {
      setInvalid(dobInput, 'dobError', dobErr);
      isValid = false;
    } else {
      setValid(dobInput, 'dobError');
    }

    // Gender
    if (!genderSelect || !genderSelect.value || (genderSelect.value !== 'Male' && genderSelect.value !== 'Female')) {
      setInvalid(genderSelect, 'genderError', 'Please select Male or Female.');
      isValid = false;
    } else {
      setValid(genderSelect, 'genderError');
    }

    // Sport
    if (!sportSelect || !sportSelect.value || sportSelect.value === 'Select Sport') {
      setInvalid(sportSelect, 'sportError', 'Please select a primary sport.');
      isValid = false;
    } else {
      setValid(sportSelect, 'sportError');
    }

    // Email
    const emailErr = validateEmail(emailInput ? emailInput.value : '');
    if (emailErr) {
      setInvalid(emailInput, 'emailError', emailErr);
      isValid = false;
    } else {
      setValid(emailInput, 'emailError');
    }

    // Password strength validation
    const pwdError = getPasswordValidationError(passwordInput ? passwordInput.value : '');
    if (pwdError) {
      setInvalid(passwordInput, 'passwordError', pwdError);
      isValid = false;
    } else {
      setValid(passwordInput, 'passwordError');
    }

    // Confirm password match
    if (!confirmPasswordInput || !confirmPasswordInput.value || confirmPasswordInput.value !== (passwordInput ? passwordInput.value : '')) {
      const matchErr = !confirmPasswordInput || !confirmPasswordInput.value ? 'Please confirm your password.' : 'Passwords do not match.';
      setInvalid(confirmPasswordInput, 'confirmPasswordError', matchErr);
      isValid = false;
    } else {
      setValid(confirmPasswordInput, 'confirmPasswordError');
    }

    // Terms
    if (!termsCheckbox || !termsCheckbox.checked) {
      setInvalid(termsCheckbox, 'termsError', 'You must agree to the Terms of Service and Privacy Policy.');
      isValid = false;
    } else {
      setValid(termsCheckbox, 'termsError');
    }

    if (!isValid) {
      e.preventDefault();
      e.stopPropagation();
    }
  });
});

