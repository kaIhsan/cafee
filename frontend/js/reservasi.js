/**
 * reservasi.js - Skrip Halaman Reservasi
 * Menangani validasi formulir pemesanan tempat duduk/meja.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Mengambil elemen form reservasi (Anggap id-nya adalah 'form-reservasi')
    const formReservasi = document.getElementById('form-reservasi');

    if (formReservasi) {
        formReservasi.addEventListener('submit', (event) => {
            // Mencegah halaman reload (refresh) secara otomatis saat submit
            event.preventDefault();

            // Mengambil nilai dari inputan form
            const nama = document.getElementById('nama-pelanggan').value.trim();
            const tanggal = document.getElementById('tanggal-reservasi').value;
            const jumlahOrang = document.getElementById('jumlah-orang').value;

            // Validasi Sederhana
            // Penjelasan: Memastikan pengguna mengisi data dengan benar sebelum diproses.
            if (nama === "" || tanggal === "" || jumlahOrang === "") {
                alert("Gagal: Mohon lengkapi semua kolom reservasi!");
                return; // Hentikan proses jika ada yang kosong
            }

            if (jumlahOrang < 1) {
                alert("Gagal: Jumlah orang minimal adalah 1.");
                return;
            }

            // Jika semua validasi lolos, simulasikan sukses
            alert(`Berhasil! Meja atas nama ${nama} untuk ${jumlahOrang} orang pada tanggal ${tanggal} telah dikonfirmasi.`);
            
            // Kosongkan form kembali setelah sukses
            formReservasi.reset();
        });
    }
});