/**
 * main.js - Skrip Global
 * Berisi fungsi-fungsi yang dapat digunakan oleh seluruh halaman.
 */

// Fungsi untuk memuat komponen (seperti Navbar dan Footer) ke dalam halaman
// Penjelasan untuk pemula: Fungsi ini mengambil file HTML lain dan memasukkannya ke halaman saat ini.
const loadComponent = async (elementId, filePath) => {
    try {
        const element = document.getElementById(elementId);
        // Pastikan elemen tujuan ada di halaman
        if (element) {
            // Mengambil file HTML (karena kita di dalam pages/, kita mundur ke folder components/)
            const response = await fetch(`../components/${filePath}`);
            
            if (response.ok) {
                const html = await response.text();
                element.innerHTML = html; // Memasukkan isi HTML ke elemen
            } else {
                console.error(`Gagal memuat ${filePath}`);
            }
        }
    } catch (error) {
        console.error("Terjadi kesalahan jaringan:", error);
    }
};

// Jalankan saat seluruh dokumen HTML selesai dimuat (DOM Ready)
document.addEventListener('DOMContentLoaded', () => {
    // Memuat navbar ke elemen dengan id="navbar-container"
    loadComponent('navbar-container', 'navbar.html');
    // Memuat footer ke elemen dengan id="footer-container"
    loadComponent('footer-container', 'footer.html');
});