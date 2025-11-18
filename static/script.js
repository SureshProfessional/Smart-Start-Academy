// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar background change on scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
    }
});

// Animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    observer.observe(el);
});

// Carousel auto-play
document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('#featuresCarousel');
    if (carousel) {
        const carouselInstance = new bootstrap.Carousel(carousel, {
            interval: 5000,
            wrap: true,
            pause: 'hover'
        });
    }
});

// Form validation enhancement
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        const requiredFields = form.querySelectorAll('[required]');
        let isValid = true;

        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                field.classList.add('is-invalid');
                isValid = false;
            } else {
                field.classList.remove('is-invalid');
                field.classList.add('is-valid');
            }
        });

        if (!isValid) {
            e.preventDefault();
            // Show error message
            const errorDiv = document.createElement('div');
            errorDiv.className = 'alert alert-danger mt-3';
            errorDiv.textContent = 'Please fill in all required fields.';
            form.appendChild(errorDiv);
            setTimeout(() => errorDiv.remove(), 3000);
        }
    });
});

// Button ripple effect
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        ripple.className = 'ripple-effect';
        ripple.style.left = (e.offsetX - 10) + 'px';
        ripple.style.top = (e.offsetY - 10) + 'px';
        this.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);
    });
});

// Add ripple effect styles dynamically
const style = document.createElement('style');
style.textContent = `
    .ripple-effect {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }

    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }

    .btn {
        position: relative;
        overflow: hidden;
    }
`;
document.head.appendChild(style);

// Lazy loading for images
const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            observer.unobserve(img);
        }
    });
});

document.querySelectorAll('img[data-src]').forEach(img => {
    imageObserver.observe(img);
});

// Tooltip initialization
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});

// Progress bar animation
function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = width;
        }, 500);
    });
}

// Call animateProgressBars when stats section is visible
const statsSection = document.querySelector('.stats');
if (statsSection) {
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateProgressBars();
                statsObserver.unobserve(entry.target);
            }
        });
    });
    statsObserver.observe(statsSection);
}

// Dynamic year update in footer
document.addEventListener('DOMContentLoaded', function() {
    const yearElement = document.querySelector('.current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
});

// Search functionality (if search bar exists)
const searchInput = document.querySelector('#searchInput');
if (searchInput) {
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        const searchableItems = document.querySelectorAll('.searchable');

        searchableItems.forEach(item => {
            const text = item.textContent.toLowerCase();
            if (text.includes(query)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
}

// Theme toggle (if needed in future)
function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-theme');

    const themeIcon = document.querySelector('#themeToggle i');
    if (body.classList.contains('dark-theme')) {
        themeIcon.className = 'bi bi-sun';
        localStorage.setItem('theme', 'dark');
    } else {
        themeIcon.className = 'bi bi-moon';
        localStorage.setItem('theme', 'light');
    }
}

// Load saved theme
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
});

// Newsletter subscription
function subscribeNewsletter(email) {
    // Simulate API call
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (email.includes('@')) {
                resolve('Successfully subscribed!');
            } else {
                reject('Invalid email address');
            }
        }, 1000);
    });
}

document.querySelectorAll('.newsletter-form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = this.querySelector('input[type="email"]').value;
        const button = this.querySelector('button');
        const originalText = button.textContent;

        button.textContent = 'Subscribing...';
        button.disabled = true;

        subscribeNewsletter(email)
            .then(message => {
                button.textContent = 'Subscribed!';
                button.classList.remove('btn-primary');
                button.classList.add('btn-success');
                this.reset();
            })
            .catch(error => {
                button.textContent = 'Error';
                button.classList.add('btn-danger');
                setTimeout(() => {
                    button.textContent = originalText;
                    button.classList.remove('btn-danger');
                    button.disabled = false;
                }, 2000);
            });
    });
});
