/**
 * AthleteGuard AI - Registration Form Validation & Password Strength Gauge
 */

document.addEventListener('DOMContentLoaded', function () {
  const regForm = document.getElementById('registerForm');
  if (!regForm) return;

  const fullNameInput = document.getElementById('regFullName');
  const ageInput = document.getElementById('regAge');
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

  function setValid(input) {
    if (input) input.classList.remove('is-invalid');
  }

  function setInvalid(input, errorId, message) {
    if (!input) return;
    input.classList.add('is-invalid');
    const errElem = document.getElementById(errorId);
    if (errElem && message) {
      errElem.textContent = message;
    }
  }

  function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  }

  // Password Strength Calculation
  function calculateStrength(pwd) {
    let score = 0;
    if (!pwd) return 0;
    if (pwd.length >= 6) score += 1;
    if (pwd.length >= 10) score += 1;
    if (/[A-Z]/.test(pwd) && /[0-9]/.test(pwd)) score += 1;
    if (/[^A-Za-z0-9]/.test(pwd)) score += 1;
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

    if (score <= 1) {
      if (strengthBars[0]) strengthBars[0].style.backgroundColor = '#ef4444'; // Red
      if (strengthLabel) {
        strengthLabel.textContent = 'Weak';
        strengthLabel.style.color = '#ef4444';
      }
    } else if (score === 2 || score === 3) {
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

  // Password input listener
  if (passwordInput) {
    passwordInput.addEventListener('input', function () {
      updateStrengthMeter(this.value);
      if (this.value.length >= 6) {
        setValid(this);
      }
      if (confirmPasswordInput && confirmPasswordInput.value.length > 0) {
        if (confirmPasswordInput.value !== this.value) {
          setInvalid(confirmPasswordInput, 'confirmPasswordError', 'Passwords do not match.');
        } else {
          setValid(confirmPasswordInput);
        }
      }
    });
  }

  // Confirm password listener
  if (confirmPasswordInput) {
    confirmPasswordInput.addEventListener('input', function () {
      if (this.value !== passwordInput.value) {
        setInvalid(this, 'confirmPasswordError', 'Passwords do not match.');
      } else {
        setValid(this);
      }
    });
  }

  // Submit Validation
  regForm.addEventListener('submit', function (e) {
    let isValid = true;

    // Full Name
    if (!fullNameInput || fullNameInput.value.trim() === '') {
      setInvalid(fullNameInput, 'fullNameError', 'Full Name is required.');
      isValid = false;
    } else {
      setValid(fullNameInput);
    }

    // Age
    if (!ageInput || ageInput.value.trim() === '' || isNaN(ageInput.value) || Number(ageInput.value) < 10) {
      setInvalid(ageInput, 'ageError', 'Enter a valid age (10+).');
      isValid = false;
    } else {
      setValid(ageInput);
    }

    // Gender
    if (!genderSelect || genderSelect.value === '' || genderSelect.value === 'Select Gender') {
      setInvalid(genderSelect, 'genderError', 'Please select a gender.');
      isValid = false;
    } else {
      setValid(genderSelect);
    }

    // Sport
    if (!sportSelect || sportSelect.value === '' || sportSelect.value === 'Select Sport') {
      setInvalid(sportSelect, 'sportError', 'Please select a primary sport.');
      isValid = false;
    } else {
      setValid(sportSelect);
    }

    // Email
    if (!emailInput || !validateEmail(emailInput.value.trim())) {
      setInvalid(emailInput, 'emailError', 'Enter a valid email address.');
      isValid = false;
    } else {
      setValid(emailInput);
    }

    // Password length
    if (!passwordInput || passwordInput.value.length < 6) {
      setInvalid(passwordInput, 'passwordError', 'Password must be at least 6 characters.');
      isValid = false;
    } else {
      setValid(passwordInput);
    }

    // Confirm password match
    if (!confirmPasswordInput || confirmPasswordInput.value !== passwordInput.value) {
      setInvalid(confirmPasswordInput, 'confirmPasswordError', 'Passwords do not match.');
      isValid = false;
    } else {
      setValid(confirmPasswordInput);
    }

    // Terms
    if (!termsCheckbox || !termsCheckbox.checked) {
      setInvalid(termsCheckbox, 'termsError', 'You must agree to the Terms of Service.');
      isValid = false;
    } else {
      setValid(termsCheckbox);
    }

    if (!isValid) {
      e.preventDefault();
      e.stopPropagation();
    }
  });
});
