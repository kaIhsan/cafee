/**
 * dashboard.js - Skrip Halaman Dashboard
 * Menangani interaksi pada panel dasbor pengguna/admin.
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Logika Konfirmasi Logout
    // Penjelasan: Mencegah pengguna keluar tanpa sengaja dengan memberikan peringatan.
    const logoutBtn = document.querySelector('.logout-btn a');
    
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (event) => {
            // Mencegah link langsung berpindah halaman
            event.preventDefault(); 
            
            // Tampilkan kotak dialog konfirmasi
            const konfirmasi = confirm("Apakah Anda yakin ingin keluar dari akun?");
            
            if (konfirmasi) {
                // Jika klik 'OK', arahkan ke halaman login
                window.location.href = "login.html";
            }
            // Jika batal, tidak terjadi apa-apa
        });
    }

    // 2. Efek sapaan dinamis berdasarkan waktu (Pagi/Siang/Sore/Malam)
    const headerTitle = document.querySelector('.header-top h1');
    if (headerTitle) {
        const jam = new Date().getHours();
        let sapaan = "Selamat Datang";

        if (jam < 12) sapaan = "Selamat Pagi";
        else if (jam < 15) sapaan = "Selamat Siang";
        else if (jam < 18) sapaan = "Selamat Sore";
        else sapaan = "Selamat Malam";

        // Mengubah teks h1 menjadi sapaan dinamis
        headerTitle.innerText = `${sapaan} Kembali, Penikmat Kopi!`;
    }
});