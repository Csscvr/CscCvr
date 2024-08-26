const passwordInput = document.getElementById('password');
const strengthMeterFill = document.getElementById('strength-meter-fill');
const strengthMessage = document.getElementById('strength-message');

passwordInput.addEventListener('input', testPasswordStrength);

function testPasswordStrength() {
  const password = passwordInput.value;
  let strength = 0;

  // Check password length
  if (password.length < 8) {
    strength = 0;
  } else if (password.length >= 8 && password.length < 12) {
    strength = 1;
  } else {
    strength = 2;
  }

  // Check for uppercase letters
  if (/[A-Z]/.test(password)) {
    strength++;
  }

  // Check for lowercase letters
  if (/[a-z]/.test(password)) {
    strength++;
  }

  // Check for numbers
  if (/\d/.test(password)) {
    strength++;
  }

  // Check for special characters
  if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
    strength++;
  }

  // Update strength meter and message
  updateStrengthMeter(strength);
}

function updateStrengthMeter(strength) {
  let meterWidth = 0;
  let message = '';

  switch (strength) {
    case 0:
      meterWidth = 20;
      message = 'Very weak';
      strengthMeterFill.className = 'strength-meter-fill weak';
      break;
    case 1:
      meterWidth = 40;
      message = 'Weak';
      strengthMeterFill.className = 'strength-meter-fill weak';
      break;
    case 2:
      meterWidth = 60;
      message = 'Medium';
      strengthMeterFill.className = 'strength-meter-fill medium';
      break;
    case 3:
      meterWidth = 80;
      message = 'Strong';
      strengthMeterFill.className = 'strength-meter-fill strong';
      break;
    case 4:
      meterWidth = 100;
      message = 'Very strong';
      strengthMeterFill.className = 'strength-meter-fill strong';
      break;
  }

  strengthMeterFill.style.width = `${meterWidth}%`;
  strengthMessage.textContent = message;
}