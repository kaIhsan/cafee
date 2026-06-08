function ubahQty(id, perubahan) {
    let input = document.getElementById(id);
    let nilai = parseInt(input.value) + perubahan;

    if (nilai < 0) nilai = 0;

    input.value = nilai;
    hitungTotal();
}

function hitungTotal() {

    const harga = {
        roti: 15000,
        fries: 20000,
        nasgor: 30000,
        spaghetti: 35000,

        kopi: 20000,
        americano: 18000,
        matcha: 25000,
        lychee: 15000
    };

    let total =
        (document.getElementById('roti').value * harga.roti) +
        (document.getElementById('fries').value * harga.fries) +
        (document.getElementById('nasgor').value * harga.nasgor) +
        (document.getElementById('spaghetti').value * harga.spaghetti) +
        (document.getElementById('kopi').value * harga.kopi) +
        (document.getElementById('americano').value * harga.americano) +
        (document.getElementById('matcha').value * harga.matcha) +
        (document.getElementById('lychee').value * harga.lychee);

    document.getElementById('totalHarga').innerText =
        "Rp " + total.toLocaleString('id-ID');
}

document.getElementById("formReservasi").addEventListener("submit", function(e){
    e.preventDefault();

<<<<<<< HEAD
=======
    const nama = document.getElementById('nama').value;

    const harga = {
        roti: 15000,
        fries: 20000,
        nasgor: 30000,
        spaghetti: 35000,
        kopi: 20000,
        americano: 18000,
        matcha: 25000,
        lychee: 15000
    };

    const items = [
        { id: 'roti', name: 'Roti' },
        { id: 'fries', name: 'Fries' },
        { id: 'nasgor', name: 'Nasi Goreng' },
        { id: 'spaghetti', name: 'Spaghetti' },
        { id: 'kopi', name: 'Kopi' },
        { id: 'americano', name: 'Americano' },
        { id: 'matcha', name: 'Matcha' },
        { id: 'lychee', name: 'Lychee' }
    ];

    let total = 0;
    let detail = [];

    items.forEach(item => {
        const qty = parseInt(document.getElementById(item.id).value) || 0;
        if (qty > 0) {
            total += qty * harga[item.id];
            detail.push(`${item.name} x${qty}`);
        }
    });

    const id = 'ID-' + Math.floor(1000 + Math.random() * 9000);

    const order = {
        id: id,
        nama: nama,
        tanggal: new Date().toLocaleDateString('id-ID'),
        total: total,
        status: 'process',
        label: 'Diproses',
        menu: detail.join(', ')
    };

    const old = JSON.parse(localStorage.getItem('galaxy_orders') || '[]');
    old.unshift(order);
    localStorage.setItem('galaxy_orders', JSON.stringify(old));

>>>>>>> c97d53aeb11992cf66757347ded7cfe161287ff3
    alert("Reservasi berhasil dibuat!");

    setTimeout(() => {
        window.location.href = "dashboard.html";
    }, 1000);
});

function validasiInputPelanggan() {
  const nama = document.getElementById('nama').value.trim();
  const menu = document.querySelector('[name="pilihan_menu"]').value;
  const jumlah = parseInt(document.querySelector('[name="jumlah"]').value);

  if (!nama || !jumlah) return false;

  const PRICES = { 'Kopi Susu Gula Aren': 20000, 'Americano Iced': 18000, ... };
  const id = '#ORD-' + (Date.now() % 100000);
  const total = (PRICES[menu] || 0) * jumlah;

  const orders = JSON.parse(localStorage.getItem('galaxy_orders') || '[]');
  orders.unshift({ id, nama, menu, jumlah, total,
    tanggal: new Date().toLocaleDateString('id-ID'), status: 'new', label: 'Baru' });
  localStorage.setItem('galaxy_orders', JSON.stringify(orders));
  return true; // lanjut submit
}