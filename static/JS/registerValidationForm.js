const form = document.getElementById('regform');
const FName = document.getElementById('FName');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  checkInputs();
});

function checkInputs() {
  // get the value from the form and trim it
  const FNameValue = FName.value.trim();

  //////////////// CHECK FOR USERNAME INPUT ////////////////

  if (FNameValue === '') {
    // call the error function
    setErrorFor(FName, 'This field cannot be blank'); //  function created bellow
  } else {
    // call successful function
    setSuccessFor(FName); // function created bellow
  }
}

function setErrorFor(input, message) {
  const form_Field = input.parentElement; // .form-control
  const small = form_Field.querySelector('small');

  // add error message inside the small tag
  small.innerText = message;

  // add error class
  form_Field.className = 'formField error';
}

function setSuccessFor(input) {
  const form_Field = input.parentElement; // .form-control

  // add error class
  form_Field.className = 'formField success';
}
