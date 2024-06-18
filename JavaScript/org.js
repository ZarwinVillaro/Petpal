function toggleButtons(organization) {
    var buttons = organization.querySelectorAll('.apply-button, .view-button');
    buttons.forEach(function(button) {
        button.style.display = button.style.display === 'none' ? 'inline-block' : 'none';
    });
}

function viewOrganizationDetails(organizationId) {
    window.location.href = `organization_details.html?id=${organizationId}`;
}
