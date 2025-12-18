/* -----------------------------------------
   Smooth Scroll for In-page Links
------------------------------------------ */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', e => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (!target) return;

            e.preventDefault();
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        });
    });
}


/* -----------------------------------------
   Navbar Scroll Behavior
------------------------------------------ */
function initNavbarScroll() {
    const navbar = document.querySelector('.main-navbar');
    if (!navbar) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 10) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });
}


/* -----------------------------------------
   Password Toggle
------------------------------------------ */
function initPasswordToggle() {
    document.querySelectorAll(".password-toggle").forEach(icon => {
        icon.addEventListener("click", () => {
            const input = document.getElementById(icon.dataset.target);
            if (!input) return;

            if (input.type === "password") {
                input.type = "text";
                icon.classList.remove("bi-eye-slash");
                icon.classList.add("bi-eye");
            } else {
                input.type = "password";
                icon.classList.remove("bi-eye");
                icon.classList.add("bi-eye-slash");
            }
        });
    });
}


/* -----------------------------------------
   Profile Photo Upload Preview + Remove
------------------------------------------ */
function initImageUpload() {
    const uploadInput = document.querySelector("input[type='file'][name='school_image']");
    const preview = document.getElementById("photoPreview");
    const removeBtn = document.getElementById("removePhotoBtn");

    if (uploadInput && preview) {
        uploadInput.addEventListener("change", e => {
            const file = e.target.files[0];
            if (file) {
                preview.src = URL.createObjectURL(file);
            }
        });
    }

    if (removeBtn && uploadInput && preview) {
        removeBtn.addEventListener("click", () => {
            preview.src = "https://via.placeholder.com/150?text=No+Image";
            uploadInput.value = "";
        });
    }
}


/* -----------------------------------------
   Active Navbar Highlight
------------------------------------------ */
function initActiveNavbar() {
    const currentURL = window.location.href;

    document.querySelectorAll(".nav-link").forEach(link => {
        if (link.href === currentURL) {
            link.classList.add("active");
        }
    });
}


/* -----------------------------------------
   Initialize All Scripts
------------------------------------------ */
document.addEventListener("DOMContentLoaded", () => {
    initSmoothScroll();
    initNavbarScroll();
    initPasswordToggle();
    initImageUpload();
    initActiveNavbar();
});

$(document).ready(function() {

    $('.crm-date').datepicker({
        format: 'dd-mm-yyyy', // ⭐ Display format
        autoclose: true,
        todayHighlight: true,
        clearBtn: true,
        orientation: "bottom",
        defaultViewDate: new Date() // Calendar opens at today
    }).datepicker('setDate', new Date()); // ⭐ Default today set

});