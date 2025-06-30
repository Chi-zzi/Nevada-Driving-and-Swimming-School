function toggleMenu() {
    let menu = document.querySelector(".nav-links");
    let menuIcon = document.querySelector(".menu-toggle i");

    menu.classList.toggle("active");
    menuIcon.classList.toggle("bi-list");
    menuIcon.classList.toggle("bi-x"); // Toggle between three-bar & cancel icon
}


document.querySelectorAll('.navbar-dropdown > .navbar-dropbtn').forEach(button => {
    button.addEventListener('click', function () {
        const parent = this.parentElement;
        parent.classList.toggle('active');
    });
});



// let currentIndex = 0;
//     const slides = document.querySelectorAll(".slide");
//     const totalSlides = slides.length;

//     function showSlide(index) {
//         slides.forEach((slide, i) => {
//             slide.style.display = i === index ? "block" : "none";
//         });
//     }

//     function nextSlide() {
//         currentIndex = (currentIndex + 1) % totalSlides;
//         showSlide(currentIndex);
//     }

//     function prevSlide() {
//         currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
//         showSlide(currentIndex);
//     }

//     // Auto-slide every 4 seconds
//     setInterval(nextSlide, 4000);
    
//     // Show first slide
//     showSlide(currentIndex);


document.addEventListener("DOMContentLoaded", function () {
    let slideIndex = 0;
    const slides = document.querySelectorAll(".slide");
    const totalSlides = slides.length;

    function showSlide(index) {
        // Ensure slideIndex is within bounds
        if (index >= totalSlides) slideIndex = 0;
        if (index < 0) slideIndex = totalSlides - 1;

        // Move the slider
        document.querySelector(".hero-slider").style.transform = `translateX(-${slideIndex * 100}vw)`;
    }

    function nextSlide() {
        slideIndex++;
        showSlide(slideIndex);
    }

    function prevSlide() {
        slideIndex--;
        showSlide(slideIndex);
    }

    function startSlider() {
        slideInterval = setInterval(nextSlide, 4000);
    }

    function stopSlider() {
        clearInterval(slideInterval);
    }

    // Auto-slide every 4 seconds
    startSlider();

    // // Auto-slide every 4 seconds
    // setInterval(() => {
    //     nextSlide();
    // }, 4000);

    // Attach to buttons
    document.querySelector(".next").addEventListener("click", nextSlide);
    document.querySelector(".prev").addEventListener("click", prevSlide);

    // Pause when hovering over content
    const heroContent = document.querySelector(".hero-content");
    heroContent.addEventListener("mouseenter", stopSlider);
    heroContent.addEventListener("mouseleave", startSlider);
});


document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });
});


// Read More Functionality of the About - Section on the Home Page
// document.addEventListener("DOMContentLoaded", function () {
//     const readMoreBtn = document.querySelector(".read-more-btn");
//     const hiddenText = document.querySelector(".hidden-text");

//     readMoreBtn.addEventListener("click", function () {
//         if (hiddenText.style.display === "none" || hiddenText.style.display === "") {
//             hiddenText.style.display = "inline";
//             readMoreBtn.textContent = "Read Less";
//         } else {
//             hiddenText.style.display = "none";
//             readMoreBtn.textContent = "Read More";
//         }
//     });
// });


// Fade In Animation of the About Section in the Home Page
document.addEventListener("DOMContentLoaded", function () {
    const aboutSection = document.querySelector(".about-section");

    function fadeInOnScroll() {
        const sectionPos = aboutSection.getBoundingClientRect().top;
        const screenPos = window.innerHeight / 1.3; // Adjust trigger point

        if (sectionPos < screenPos) {
            aboutSection.classList.add("fade-in");
        }
    }

    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll(); // Run once to check if already in view
});


// Read More animation for the about section in the Home Page
// document.addEventListener("DOMContentLoaded", function () {
//     const readMoreBtn = document.querySelector(".read-more-btn");
//     const hiddenText = document.querySelector(".hidden-text");
//     const aboutText = document.querySelector(".about-text");

//     readMoreBtn.addEventListener("click", function () {
//         if (hiddenText.style.maxHeight === "0px" || hiddenText.style.maxHeight === "") {
//             hiddenText.style.display = "block";
//             hiddenText.style.maxHeight = hiddenText.scrollHeight + "px"; // Expands smoothly
//             aboutText.style.maxHeight = aboutText.scrollHeight + hiddenText.scrollHeight + "px";
//             readMoreBtn.textContent = "Read Less";
//         } else {
//             hiddenText.style.maxHeight = "0px"; // Collapses smoothly
//             setTimeout(() => {
//                 hiddenText.style.display = "none";
//             }, 500); // Hides after transition ends
//             readMoreBtn.textContent = "Read More...";
//         }
//     });
// });

// Upper one still Also Okay, but because of the List a Paragraph put in place in the about our company content


// Read More animation for the about section in the Home Page
document.addEventListener("DOMContentLoaded", function () {
  const readMoreBtn = document.querySelector(".read-more-btn");
  const hiddenText = document.querySelector(".hidden-text");

  // Ensure hidden-text starts collapsed
  hiddenText.style.maxHeight = "0px";
  hiddenText.setAttribute("aria-expanded", "false");

  readMoreBtn.addEventListener("click", function () {
    // If currently collapsed (maxHeight = 0), expand
    if (hiddenText.getAttribute("aria-expanded") === "false") {
      // 1) set max-height to its scrollHeight so it animates open
      hiddenText.style.maxHeight = hiddenText.scrollHeight + "px";
      // 2) mark it expanded
      hiddenText.setAttribute("aria-expanded", "true");
      readMoreBtn.textContent = "Read Less";

    } else {
      // collapse it
      hiddenText.style.maxHeight = "0px";
      hiddenText.setAttribute("aria-expanded", "false");
      readMoreBtn.textContent = "Read More...";
    }
  });
});




// Appearing Animation of the Course Section in the Home Page
document.addEventListener("DOMContentLoaded", function () {
    let courseSection = document.querySelector(".course-section");

    let observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    courseSection.classList.add("visible");
                    observer.unobserve(courseSection); // Stop observing once it appears
                }
            });
        },
        { threshold: 0.1 } // Trigger when 10% of the section is visible
    );

    observer.observe(courseSection);
});



// Appearing Animation of the Swimming Course Section in the Home Page
document.addEventListener("DOMContentLoaded", function () {
    let courseSection = document.querySelector(".swimming-course-section");

    let observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    courseSection.classList.add("visible");
                    observer.unobserve(courseSection); // Stop observing once it appears
                }
            });
        },
        { threshold: 0.1 } // Trigger when 10% of the section is visible
    );

    observer.observe(courseSection);
});




// document.addEventListener("DOMContentLoaded", function() {
//     const slides = document.querySelectorAll(".carousel-item");
//     let currentIndex = 0;

//     function showSlide(index) {
//         slides.forEach((slide, i) => {
//             slide.style.display = i === index ? "block" : "none";
//         });
//     }

//     function nextSlide() {
//         currentIndex = (currentIndex + 1) % slides.length;
//         showSlide(currentIndex);
//     }

//     showSlide(currentIndex);
//     setInterval(nextSlide, 3000);
// });





// Appointement Section
function handleappointmentFormSubmit(event) {
    event.preventDefault();

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var programme = document.getElementById('programme').value;
    var state = document.getElementById('state').value;
    var country = document.getElementById('country').value;
    var message = document.getElementById('message').value;

    var spinner = document.querySelector('.appoint-spinner');
    var buttonText = document.querySelector('.appoint-button-text');
    var form = document.getElementById('appointment-form');

    // Check if all fields are filled
    if (name && email && phone && programme && state && country && message) {
            
        spinner.style.display = 'inline-block'; // Show spinner
        // buttonText.style.display = 'none'; 
        buttonText.textContent = 'Submitting...';
        
        setTimeout(function() {

            spinner.style.display = 'none'; // Show spinner
            // buttonText.style.display = 'none'; 
            buttonText.textContent = 'Submit';


            fetch("/home/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()  // Include CSRF token for security
                },
                body: JSON.stringify({ name: name, 
                                        email: email,  
                                        phone: phone, 
                                        programme: programme, 
                                        state: state, 
                                        country: country, 
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


// Appearing Animation of the Appointement Section in the Home Page
document.addEventListener("DOMContentLoaded", function () {
    let courseSection = document.querySelector(".consultation-container");

    let observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    courseSection.classList.add("visible");
                    observer.unobserve(courseSection); // Stop observing once it appears
                }
            });
        },
        { threshold: 0.1 } // Trigger when 10% of the section is visible
    );

    observer.observe(courseSection);
});



// Feedback Carousel for the Client Testimonial section
document.addEventListener("DOMContentLoaded", function() {
    const carouselInner = document.querySelector(".feedback-carousel-inner");
    const slides = document.querySelectorAll(".feedback-carousel-item");
    let currentIndex = 0;

    function showSlide(index) {
        const offset = -index * 100; // Move left by 100% of each slide width
        carouselInner.style.transform = `translateX(${offset}%)`;
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    showSlide(currentIndex);
    setInterval(nextSlide, 3000); // Slide every 3 seconds
});


// Fade In Animation of the Feedback Section in the Home Page
document.addEventListener("DOMContentLoaded", function () {
    const aboutSection = document.querySelector(".feedback-container");

    function fadeInOnScroll() {
        const sectionPos = aboutSection.getBoundingClientRect().top;
        const screenPos = window.innerHeight / 1.3; // Adjust trigger point

        if (sectionPos < screenPos) {
            aboutSection.classList.add("fade-in");
        }
    }

    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll(); // Run once to check if already in view
});





// Fade In Animation of the Certification Section in the Home Page
document.addEventListener("DOMContentLoaded", function () {
    const aboutSection = document.querySelector(".certifications-container");

    function fadeInOnScroll() {
        const sectionPos = aboutSection.getBoundingClientRect().top;
        const screenPos = window.innerHeight / 1.3; // Adjust trigger point

        if (sectionPos < screenPos) {
            aboutSection.classList.add("fade-in");
        }
    }

    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll(); // Run once to check if already in view
});
