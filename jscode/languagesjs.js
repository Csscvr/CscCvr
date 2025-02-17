// Function to set the language preference
function setLanguage(language) {
    localStorage.setItem('preferredLanguage', language);
    loadContent(language);
}

// Function to load content based on the selected language
function loadContent(language) {
    const greetingElement = document.getElementById('greeting');
    switch (language) {
        case 'en':
            greetingElement.textContent = 'Hello! Welcome to our website.';
            break;
        case 'es':
            greetingElement.textContent = '¡Hola! Bienvenido a nuestro sitio web.';
            break;
        case 'fr':
            greetingElement.textContent = 'Bonjour! Bienvenue sur notre site Web.';
            break;
        default:
            greetingElement.textContent = 'Hello! Welcome to our website.';
    }
}

// Function to retrieve the user's preferred language on page load
function retrieveLanguagePreference() {
    const preferredLanguage = localStorage.getItem('preferredLanguage');
    if (preferredLanguage) {
        loadContent(preferredLanguage);
    } else {
        // If no preference is set, load default content (English)
        loadContent('en');
    }
}

// Call the function to retrieve the language preference when the page loads
window.onload = retrieveLanguagePreference;

// Example of how to set the language when a button is clicked
// You would need to call setLanguage('en'), setLanguage('es'), or setLanguage('fr') from your button click handlers
