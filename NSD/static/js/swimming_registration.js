document.addEventListener("DOMContentLoaded", function () {
    let dobInput = document.getElementById("client_dob");
    let ageInput = document.getElementById("client_age");

    // Set max date to ensure only users above 20 years can register
    let today = new Date();
    let minYear = today.getFullYear() - 16; // 16 years ago
    let minDate = `${minYear}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
    dobInput.setAttribute("max", minDate);

    // Calculate age when user selects a DOB
    dobInput.addEventListener("change", function () {
        let dob = new Date(this.value);
        let age = today.getFullYear() - dob.getFullYear();
        let monthDiff = today.getMonth() - dob.getMonth();
        let dayDiff = today.getDate() - dob.getDate();

        // Adjust age if birthday hasn't occurred yet this year
        if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
            age--;
        }

        // Populate the age input field
        ageInput.value = age;
    });
});



document.addEventListener("DOMContentLoaded", function () {
    const dropdownSelected = document.querySelector(".swim-register-dropdown-selected");
    const dropdownList = document.querySelector(".swim-register-dropdown-list");
    const dropdownArrow = document.querySelector(".swim-register-dropdown-arrow");
    const countryCodeInput = document.getElementById("register-country_code");
    const selectedFlag = document.getElementById("register-selected-flag");
    const selectedCode = document.getElementById("register-selected-code");

    // Toggle dropdown
    dropdownSelected.addEventListener("click", function () {
        dropdownList.style.display = dropdownList.style.display === "block" ? "none" : "block";
        dropdownSelected.classList.toggle("swim-register-dropdown-open");
    });

    // Select country
    document.querySelectorAll(".swim-register-dropdown-item").forEach(item => {
        item.addEventListener("click", function () {
            let flag = this.getAttribute("data-flag");
            let code = this.getAttribute("data-code");

            selectedFlag.src = flag;
            selectedCode.textContent = code;
            countryCodeInput.value = code;

            dropdownList.style.display = "none";
            dropdownSelected.classList.remove("swim-register-dropdown-open");
        });
    });

    // Hide dropdown when clicking outside
    document.addEventListener("click", function (event) {
        if (!dropdownSelected.contains(event.target) && !dropdownList.contains(event.target)) {
            dropdownList.style.display = "none";
            dropdownSelected.classList.remove("swim-register-dropdown-open");
        }
    });
});




// Applicant phone number Implementation
document.addEventListener("DOMContentLoaded", function () {
    const dropdownSelected = document.querySelector(".swim-applicant-register-dropdown-selected");
    const dropdownList = document.querySelector(".swim-applicant-register-dropdown-list");
    const dropdownArrow = document.querySelector(".swim-applicant-register-dropdown-arrow");
    const countryCodeInput = document.getElementById("applicant-register-country_code");
    const selectedFlag = document.getElementById("applicant-register-selected-flag");
    const selectedCode = document.getElementById("applicant-register-selected-code");

    // Toggle dropdown
    dropdownSelected.addEventListener("click", function () {
        dropdownList.style.display = dropdownList.style.display === "block" ? "none" : "block";
        dropdownSelected.classList.toggle("swim-applicant-register-dropdown-open");
    });

    // Select country
    document.querySelectorAll(".swim-applicant-register-dropdown-item").forEach(item => {
        item.addEventListener("click", function () {
            let flag = this.getAttribute("data-flag");
            let code = this.getAttribute("data-code");

            selectedFlag.src = flag;
            selectedCode.textContent = code;
            countryCodeInput.value = code;

            dropdownList.style.display = "none";
            dropdownSelected.classList.remove("swim-applicant-register-dropdown-open");
        });
    });

    // Hide dropdown when clicking outside
    document.addEventListener("click", function (event) {
        if (!dropdownSelected.contains(event.target) && !dropdownList.contains(event.target)) {
            dropdownList.style.display = "none";
            dropdownSelected.classList.remove("swim-applicant-register-dropdown-open");
        }
    });
});



function handleSwimmingRegistrationFormSubmit(event) {
    event.preventDefault();

    var surname = document.getElementById('surname').value;
    var firstname = document.getElementById('firstname').value;
    var others = document.getElementById('others').value;
    var dob = document.getElementById('client_dob').value;
    var next_of_kin_phone = document.getElementById('phone').value;
    var applicant_phone = document.getElementById('applicant_phone').value;
    var sex = document.getElementById('sex').value;
    var health = document.getElementById('health').value;
    var experience = document.getElementById('experience').value;
    var residential_address = document.getElementById('resident').value;
    var programme = document.getElementById('course_type').value;
    var duration = document.getElementById('duration').value;
    // var password = document.getElementById('password').value;
    // var confirm_password = document.getElementById('confirm_password').value;
    var terms = document.getElementById('terms').value;
    // var profile_picture = document.getElementById('profile_picture').value;

    var spinner = document.querySelector('.swim-register-spinner');
    var buttonText = document.querySelector('.swim-register-button-text');
    var form = document.getElementById('swim-registration-form');

    // && profile_picture

    // console.log(surname, firstname, others, dob, next_of_kin_phone, applicant_phone, sex, health, experience, residential_address, programme, duration, terms)

    // Check if all fields are filled
    if (surname && firstname && others && dob && next_of_kin_phone && applicant_phone && sex && health && experience && 
        residential_address && programme && duration && terms
    ) {
            
        spinner.style.display = 'inline-block'; // Show spinner
        // buttonText.style.display = 'none'; 
        buttonText.textContent = 'Processing...';
        
        setTimeout(function() {
            form.submit(); // Submit the form after 3 seconds
        }, 3000);
    }
}


// function clearErrorMessage(id) {
//     document.getElementById(id).textContent = '';
// }

document.addEventListener("DOMContentLoaded", function() {
    let errorContainer = document.getElementById("swim-register-error-container");
    
    if (errorContainer) {
        let inputs = document.querySelectorAll("input, select, textarea");
        inputs.forEach(input => {
            input.addEventListener("focus", function() {
                errorContainer.style.display = "none";
            });
        });
    }
});



function fetchSwimmingDuration() {
    const ProgrammeID = document.getElementById("course_type").value;
    console.log('Selected Programme ID:', ProgrammeID);

    const durationSelect = document.getElementById("duration");
    // instructorSelect.innerHTML = '<option value="" disabled selected>Loading...</option>';

    fetch(`/get-swim-duration/${ProgrammeID}`)
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Swimming Duration Received:', data.duration);
            // instructorSelect.innerHTML = '<option value="" disabled selected>Select your instructor</option>';
            durationSelect.value = data.duration;
        })
        .catch(error => {
            console.error('Error fetching Swimming Durations: ', error);
            durationSelect.innerHTML = '<option value="" disabled selected>Error loading Swimming Durations</option>';
        });
}




function fetchLGAs() {
        const stateId = document.getElementById('stateoforigin').value;
        const selectedLGA = document.getElementById('selected-lga').value;
        console.log('Selected State ID:', stateId);
        // console.log(selectedLGA);

        const lgaSelect = document.getElementById('lga');
        lgaSelect.innerHTML = '<option value="" disabled selected>Loading...</option>';

        fetch(`/get-lgas/${stateId}/`)
            .then(response => {
                console.log('Response status:', response.status);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('LGAs received:', data.lgas);
                lgaSelect.innerHTML = '<option value="" disabled selected>Select your LGA</option>';


                data.lgas.forEach(lga => {
                    const option = document.createElement('option');
                    option.value = lga.id;
                    option.textContent = lga.lga;


                    // Pre-select previously chosen LGA
                    if (lga.lga.toString() === selectedLGA) {
                        option.selected = true;
                    }

                    lgaSelect.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Error fetching LGAs:', error);
                lgaSelect.innerHTML = '<option value="" disabled selected>Error loading LGAs</option>';
            });
    }



document.addEventListener("DOMContentLoaded", function () {
    const stateField = document.getElementById("stateoforigin");
    const selectedState = stateField.value;
    if (selectedState) {
        fetchLGAs();
    }
});