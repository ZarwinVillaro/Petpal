const form = document.getElementById('applicationForm');

form.addEventListener('submit', function(event) {
  const fullName = document.getElementById('fullName');
  const email = document.getElementById('email');
  const phone = document.getElementById('phone');
  const address = document.getElementById('address');

  let isValid = true;

  if (!fullName.value) {
    event.preventDefault();
    document.getElementById('fullNameError').textContent = 'Please enter your full name.';
    isValid = false;
  }

  if (!email.value) {
    event.preventDefault();
    document.getElementById('emailError').textContent = 'Please enter your email address.';
    isValid = false;
  }

  if (!phone.value) {
    event.preventDefault();
    document.getElementById('phoneError').textContent = 'Please enter your phone number.';
    isValid = false;
  }

  if (!address.value) {
    event.preventDefault();
    document.getElementById('addressError').textContent = 'Please enter your address.';
    isValid = false;
  }

  if (isValid) {
    Swal.fire({
      position: "center",
      icon: "success",
      title: "Your work has been saved",
      showConfirmButton: false,
      timer: 5300
    }).then(() => {
      form.submit();
    });
  }
});
