// Fetch organization details from URL parameters
const urlParams = new URLSearchParams(window.location.search);
const orgName = urlParams.get('name');
const orgDescription = urlParams.get('description');

// Set organization details in the page
document.getElementById('org-name').textContent = orgName;
document.getElementById('org-description').textContent = orgDescription;
