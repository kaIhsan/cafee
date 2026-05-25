/**
 * menu.js - Skrip Halaman Menu
 * Menangani tampilan data katalog minuman dan makanan.
 */

// Data menu (simulasi database sederhana)
// Penjelasan: Menyimpan data menu dalam format Array agar mudah dikelola dan ditampilkan.
const dataMenu = [
    { id: 1, nama: "Caramel Macchiato", kategori: "Kopi", harga: 45000 },
    { id: 2, nama: "Iced Matcha Latte", kategori: "Non-Kopi", harga: 40000 },
    { id: 3, nama: "Butter Croissant", kategori: "Makanan", harga: 25000 },
    { id: 4, nama: "Americano Hot", kategori: "Kopi", harga: 30000 }
];

// Fungsi untuk menampilkan menu ke HTML
const tampilkanMenu = (kategoriFilter = "Semua") => {
    // Anggap kita punya elemen <div id="menu-container"> di menu.html
    const container = document.getElementById('menu-container');
    if (!container) return; // Jika tidak ada di halaman ini, hentikan fungsi

    container.innerHTML = ""; // Bersihkan kontainer sebelum diisi ulang

    // Filter menu berdasarkan kategori
    const menuDisaring = dataMenu.filter(item => {
        if (kategoriFilter === "Semua") return true;
        return item.kategori === kategoriFilter;
    });

    // Looping data dan buat elemen HTML (Card Menu)
    menuDisaring.forEach(item => {
        // Format harga ke Rupiah
        const hargaRupiah = new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR' }).format(item.harga);
        
        // Template literal untuk membuat struktur HTML secara dinamis
        const menuCard = `
            <div class="menu-card">
                <h3>${item.nama}</h3>
                <span class="kategori">${item.kategori}</span>
                <p class="harga">${hargaRupiah}</p>
                <button onclick="pesanItem('${item.nama}')" class="btn-pesan">Pesan</button>
            </div>
        `;
        container.innerHTML += menuCard;
    });
};

// Fungsi ketika tombol pesan diklik
const pesanItem = (namaItem) => {
    alert(`${namaItem} telah ditambahkan ke keranjang pesanan Anda!`);
};

// Tampilkan semua menu saat halaman pertama kali dimuat
document.addEventListener('DOMContentLoaded', () => {
    tampilkanMenu("Semua");
});