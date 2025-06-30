function toggleSwimmingPaymentMethods(event) {
    event.preventDefault();

    const surname = document.getElementById('surname').value;
    const firstname = document.getElementById('firstname').value;
    const others = document.getElementById('others').value;
    const gender = document.getElementById('gender').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;
    const health = document.getElementById('health').value;
    const programme = document.getElementById('programme').value;
    const duration = document.getElementById('duration').value;
    const price = document.getElementById('price').value;

    // const choose_instructor = document.getElementById("instructor-payment").value;


    const spinner = document.querySelector('.swim-payment-spinner');
    const buttonText = document.querySelector('.swim-payment-button-text');
    const methods = document.getElementById("swim-payment-methods");
    const container = document.getElementById("swim-payment-container");

    if (surname && firstname && others && gender && phone && address && health && programme && duration && price) {
        spinner.style.display = 'inline-block';
        buttonText.textContent = 'Verifying...';

        setTimeout(() => {
            fetch('/swimming-payments/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // CSRF for Django
                },
                body: JSON.stringify({
                    // instructor: choose_instructor,
                    surname: surname,
                    firstname: firstname,
                    other_name: others,
                    gender: gender,
                    phone: phone,
                    address:address,
                    health: health,
                    programme: programme,
                    duration: duration,
                    price: price
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    buttonText.textContent = 'SEE PAYMENT DETAILS BELOW';
                    spinner.style.display = 'none';


                    // Smooth transition
                    container.classList.add("expanded");
                    methods.classList.add("show");
                    // methods.style.display = "flex";

                    
                    // Insert bank details
                    methods.innerHTML = `
                        <div class="swim-account-details">
                            <h3>Bank Payment Details</h3>
                            <p><strong>Account Name:</strong> NEVADA SWIM HUB</p>
                            <p><strong>Account Number:</strong> 0100373906</p>
                            <p><strong>Bank:</strong> Sterling Bank</p>
                            <p class="note">Please make your payment using the Account Details above and make sure you keep the Transaction Receipt.</p>
                        </div>
                        
                    `;


                } else {
                    buttonText.textContent = 'PAY';
                    spinner.style.display = 'none';
                    alert('Verification failed, Try again !');
                }
            });
        }, 3000);
    }
}

// CSRF token getter for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const trimmed = cookie.trim();
            if (trimmed.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(trimmed.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
