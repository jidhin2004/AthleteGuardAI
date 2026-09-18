/**
 * AthleteGuard AI - Login Form Validation
 */

document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.getElementById('loginForm');
  if (!loginForm) return;

  const emailInput = document.getElementById('loginEmail');
  const passwordInput = document.getElementById('loginPassword');

  function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  }

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

  // Real-time validation listeners
  if (emailInput) {
    emailInput.addEventListener('input', function () {
      if (this.value.trim() === '') {
        setInvalid(this, 'emailError', 'Athlete ID or Email is required.');
      } else {
        setValid(this);
      }
    });
  }

  if (passwordInput) {
    passwordInput.addEventListener('input', function () {
      if (this.value.trim() === '') {
        setInvalid(this, 'passwordError', 'Password is required.');
      } else {
        setValid(this);
      }
    });
  }

  // Submit Validation
  loginForm.addEventListener('submit', function (e) {
    let isValid = true;

    if (!emailInput || emailInput.value.trim() === '') {
      setInvalid(emailInput, 'emailError', 'Please enter your Athlete ID or Email.');
      isValid = false;
    } else {
      setValid(emailInput);
    }

    if (!passwordInput || passwordInput.value.trim() === '') {
      setInvalid(passwordInput, 'passwordError', 'Please enter your password.');
      isValid = false;
    } else {
      setValid(passwordInput);
    }

    if (!isValid) {
      e.preventDefault();
      e.stopPropagation();
    }
  });
});
