document.addEventListener("DOMContentLoaded", function () {
    if (window.location.hash) {
        let courseSection = document.querySelector(window.location.hash);
        if (courseSection) {
            courseSection.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    }
});