console.log('=== SCRIPT LOADED ===');

document.addEventListener('DOMContentLoaded', function() {
    console.log('=== DOM LOADED ===');
    
    // Test if elements exist
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');
    
    console.log('Hamburger element:', hamburger);
    console.log('Nav element:', nav);
    
    if (!hamburger) {
        console.error('ERROR: Hamburger button NOT FOUND!');
        return;
    }
    
    if (!nav) {
        console.error('ERROR: Nav element NOT FOUND!');
        return;
    }
    
    console.log('Both elements found successfully!');
    
    // Dropdown functionality
    const dropDownBtn = document.getElementById("dropDownBtn");
    
    if (dropDownBtn) {
        dropDownBtn.addEventListener('click', function(event) {
            console.log('Dropdown clicked');
            event.stopPropagation();
            const dropdown = document.getElementById("myDropdown");
            if (dropdown) {
                dropdown.classList.toggle("show");
            }
        });
    }
    
    // Close the dropdown menu if the user clicks outside of it
    window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    };
    
    // Hamburger menu functionality
    const body = document.body;
    
    // Create overlay element
    const overlay = document.createElement('div');
    overlay.className = 'overlay';
    body.appendChild(overlay);
    console.log('Overlay created');
    
    // Toggle menu
    hamburger.addEventListener('click', function(event) {
        console.log('=== HAMBURGER CLICKED ===');
        event.preventDefault();
        event.stopPropagation();
        
        hamburger.classList.toggle('active');
        nav.classList.toggle('active');
        overlay.classList.toggle('active');
        body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
        
        console.log('Hamburger classes:', hamburger.className);
        console.log('Nav classes:', nav.className);
        console.log('Overlay classes:', overlay.className);
    });
    
    console.log('Hamburger click listener added');
    
    // Close menu when clicking overlay
    overlay.addEventListener('click', function() {
        console.log('Overlay clicked');
        hamburger.classList.remove('active');
        nav.classList.remove('active');
        overlay.classList.remove('active');
        body.style.overflow = '';
    });
    
    // Close menu when clicking a link
    const navLinks = nav.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            console.log('Nav link clicked');
            hamburger.classList.remove('active');
            nav.classList.remove('active');
            overlay.classList.remove('active');
            body.style.overflow = '';
        });
    });
    
    console.log('=== SETUP COMPLETE ===');
});