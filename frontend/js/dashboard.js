document.addEventListener('DOMContentLoaded', () => {

    // Konfirmasi Logout
    const logoutBtn = document.querySelector('.logout a');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (confirm("Apakah Anda yakin ingin keluar?")) {
                window.location.href = "login.html";
            }
        });
    }

    // Sapaan dinamis berdasarkan waktu
    const headerTitle = document.querySelector('.topbar h1');
    if (headerTitle) {
        const jam = new Date().getHours();
        let sapaan = "Selamat Datang";
        if (jam < 12) sapaan = "Selamat Pagi";
        else if (jam < 15) sapaan = "Selamat Siang";
        else if (jam < 18) sapaan = "Selamat Sore";
        else sapaan = "Selamat Malam";
        headerTitle.innerText = `${sapaan} Kembali, Budi! 👋`;
    }

});