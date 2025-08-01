document.addEventListener('DOMContentLoaded', function() {
    const nav = document.createElement('nav');
    nav.style.background = '#333';
    nav.style.padding = '10px';
    nav.style.marginBottom = '20px';
    
    const navLinks = [
        { text: 'Home', url: '/index.html' },
        { text: 'Upload', url: '/upload.html' },
        { text: 'Dashboard', url: '/dashboard.html' },
        { text: 'Profile', url: '/profile.html' },
        { text: 'Settings', url: '/settings.html' }
    ];
    
    navLinks.forEach(link => {
        const a = document.createElement('a');
        a.textContent = link.text;
        a.href = link.url;
        a.style.color = 'white';
        a.style.marginRight = '15px';
        a.style.textDecoration = 'none';
        nav.appendChild(a);
    });
    
    document.body.insertBefore(nav, document.body.firstChild);
});
