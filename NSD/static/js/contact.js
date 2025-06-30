function handlecontactusFormSubmit(event) {
    event.preventDefault();

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    var spinner = document.querySelector('.contact-submit-spinner');
    var buttonText = document.querySelector('.contact-button-text');
    var form = document.getElementById('contact-us-form');

    // Check if all fields are filled
    if (name && email && message) {
            
        spinner.style.display = 'inline-block'; // Show spinner
        // buttonText.style.display = 'none'; 
        buttonText.textContent = 'Sending...';
        
        setTimeout(function() {

            spinner.style.display = 'none'; // Show spinner
            // buttonText.style.display = 'none'; 
            buttonText.textContent = 'SUBMIT';


            fetch("/contact-us/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()  // Include CSRF token for security
                },
                body: JSON.stringify({ name: name, 
                                        email: email,  
                                        message: message 
                                    })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);
                    form.reset(); // Clear input on success
                } else if (data.error) {
                    alert("Error: " + data.error);
                }
            })
            .catch(error => console.error("Error:", error));

            // form.submit(); // Submit the form after 3 seconds
        }, 3000);
    }

    // Function to get CSRF Token
    function getCSRFToken() {
        let csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]");
        return csrfToken ? csrfToken.value : "";
    }
}
