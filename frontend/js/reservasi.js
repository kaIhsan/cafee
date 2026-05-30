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

    alert("Reservasi berhasil dibuat!");

    setTimeout(() => {
        window.location.href = "dashboard.html";
    }, 1000);
});