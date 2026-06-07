function ubahQty(id, perubahan) {
    let input = document.getElementById(id);
    if (!input) return;

    let nilai = (parseInt(input.value) || 0) + perubahan;

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
        (parseInt(document.getElementById('roti').value) || 0) * harga.roti +
        (parseInt(document.getElementById('fries').value) || 0) * harga.fries +
        (parseInt(document.getElementById('nasgor').value) || 0) * harga.nasgor +
        (parseInt(document.getElementById('spaghetti').value) || 0) * harga.spaghetti +
        (parseInt(document.getElementById('kopi').value) || 0) * harga.kopi +
        (parseInt(document.getElementById('americano').value) || 0) * harga.americano +
        (parseInt(document.getElementById('matcha').value) || 0) * harga.matcha +
        (parseInt(document.getElementById('lychee').value) || 0) * harga.lychee;

    document.getElementById('totalHarga').innerText =
        "Rp " + total.toLocaleString('id-ID');
}


document.getElementById("formReservasi").addEventListener("submit", function (e) {
    e.preventDefault();

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

    alert("Reservasi berhasil dibuat!");

    // Redirect ke dashboard HANYA di sini
    setTimeout(() => {
        window.location.href = "dashboard.html";
    }, 1000);
});