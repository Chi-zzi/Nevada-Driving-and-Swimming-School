document.addEventListener("DOMContentLoaded", function() {
    function isElementInViewport(el) {
        var rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    function checkFooterVisibility() {
        var footerContents = document.querySelectorAll(".footer-content, .footer-bottom");
        
        footerContents.forEach(function(content) {
            if (isElementInViewport(content)) {
                content.classList.add("show");
            }
        });
    }
    
    window.addEventListener("scroll", checkFooterVisibility);
    checkFooterVisibility();
});


document.addEventListener("DOMContentLoaded", function () {
    const subscribeButton = document.querySelector(".newsletter button");
    const emailInput = document.querySelector(".newsletter input");

    subscribeButton.addEventListener("click", function () {
        const email = emailInput.value.trim();

        if (!email) {
            alert("Please enter a valid email address.");
            return;
        }

        fetch("/subscribe/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()  // Include CSRF token for security
            },
            body: JSON.stringify({ email: email })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
                emailInput.value = ""; // Clear input on success
            } else if (data.error) {
                alert("Error: " + data.error);
            }
        })
        .catch(error => console.error("Error:", error));
    });

    // Function to get CSRF Token
    function getCSRFToken() {
        let csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]");
        return csrfToken ? csrfToken.value : "";
    }
});
