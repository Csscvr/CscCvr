const passwordInput = document.getElementById('password');
const strengthMeterFill = document.getElementById('strength-meter-fill');
const strengthMessage = document.getElementById('strength-message');

passwordInput.addEventListener('input', testPasswordStrength);

function testPasswordStrength() {
  const password = passwordInput.value;
  let strength = 0;

  // Check password length
  if (password.length < 10) {
    strength = 0;
  } else if (password.length >= 10 && password.length < 15) {
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
    strength = strength + 0.5;
  }

  // Check for numbers
  if (/\d/.test(password)) {
    strength = strength + 0.5;
  }

  // Check for special characters
  if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
    strength = strength + 0.5;
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
      message = 'Extreamly weak';
      strengthMeterFill.className = 'strength-meter-fill weak';
      break;
    case 1:
      meterWidth = 30;
      message = 'Very Weak
      strengthMeterFill.className = 'strength-meter-fill weak'
      break;
    case 2:
      meterWidth = 40;
      message = 'Weak';
      strengthMeterFill.className = 'strength-meter-fill weak';
      break;
    case 3:
      meterWidth = 50;
      message = '50% Below Medium';
      strengthMeterFill.className = 'strength-meter-fill medium';
      break;
    case 4:
      meterWidth = 60;
      message = 'Medium'
      strengthMeterFill.className = 'strength-meter-fill medium'
      break;
    case 5:
      meterWidth = 70;
      message = ' 50% Below Strong';
      strengthMeterFill.className = 'strength-meter-fill strong';
      break;
    case 6:
      meterWidth = 80;
      message = 'strong';
      strengthMeterFill.className = 'strength-meter-fill strong';
      break;
    case 7 :
      meterWidth = 90;
      message = '50% Below Very Strong'
      strengthMeterFill.className = 'strength-meter-fill strong+'
      break;
    case 8:
      meterWidth = 100;
      message = 'Very Strong'
      strengthMeterFill.className = 'strength-meter-fill strong+'
  }

  strengthMeterFill.style.width = `${meterWidth}%`;
  strengthMessage.textContent = message;
}
