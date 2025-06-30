function togglePaymentMethods(event) {
    event.preventDefault();

    const names = document.getElementById('names').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;
    const location_detail = document.getElementById('location_detail').value;
    const course_type = document.getElementById('course_type').value;
    const duration = document.getElementById('duration').value;
    const price = document.getElementById('price').value;

    // const choose_instructor = document.getElementById("instructor-payment").value;


    const spinner = document.querySelector('.payment-spinner');
    const buttonText = document.querySelector('.payment-button-text');
    const methods = document.getElementById("payment-methods");
    const container = document.getElementById("payment-container");

    if (names && email && phone && address && location_detail && course_type && duration && price) {
        spinner.style.display = 'inline-block';
        buttonText.textContent = 'Verifying...';

        setTimeout(() => {
            fetch('/payments/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // CSRF for Django
                },
                body: JSON.stringify({
                    // instructor: choose_instructor,
                    names: names,
                    email: email,
                    phone: phone,
                    address: address,
                    location_detail: location_detail,
                    course_type: course_type,
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
                        <div class="account-details">
                            <h3>Bank Payment Details</h3>
                            <p><strong>Account Name:</strong> NEVADA DRIVING SCHOOL</p>
                            <p><strong>Account Number:</strong> 1210917375</p>
                            <p><strong>Bank:</strong> Zenith Bank</p>
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
