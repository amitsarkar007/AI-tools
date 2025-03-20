// Scroll to the top of the page
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Toggle dropdown menu visibility
function toggleDropdown() {{
    const menu = document.querySelector('#dropdown-menu');
    menu.classList.toggle('hidden');
}}

// Close dropdown if clicked outside
document.addEventListener('click', function(event) {{
    const menu = document.querySelector('#dropdown-menu');
    const button = document.querySelector('#dropdown-button');
    if (menu && !button.contains(event.target) && !menu.contains(event.target)) {{
      menu.classList.add('hidden');
    }}
}});