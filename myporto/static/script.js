// Inisialisasi AOS (Animate On Scroll)
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1000, // Durasi animasi 1 detik
        once: false,    // Animasi dimainkan setiap kali di-scroll (up dan down)
        mirror: true,   // Memainkan animasi saat scroll ke atas
        offset: 100     // Jarak trigger
    });
});