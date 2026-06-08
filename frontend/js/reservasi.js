<<<<<<< HEAD
function ubahQty(id, perubahan) {
    let input = document.getElementById(id);
    let nilai = parseInt(input.value) + perubahan;
=======
/* ================= DATA MENU ================= */
const makanan = [
    {id:1, nama:"Nasi Ayam Teriyaki", harga:16000},
    {id:2, nama:"Nasi Cumi Cabe Ijo", harga:16000},
    {id:3, nama:"Nasi Nasi Tahu Balado", harga:16000},
    {id:4, nama:"Nasi Ayam Crispy Sambal Balado", harga:16000}
];

const minuman = [
    {id:5, nama:"Kopi", harga:12000},
    {id:6, nama:"Matcha", harga:25000},
    {id:7, nama:"Americano", harga:18000},
    {id:8, nama:"Lychee Tea", harga:15000}
];
>>>>>>> 8557e0f802d4a2f0a33812e1cfb10dec8f98ac3a

/* ================= CART ================= */
let cart = [];

<<<<<<< HEAD
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
=======
/* ================= RENDER MENU ================= */
function renderMenu(){
    document.getElementById("makanan").innerHTML =
    makanan.map(m => `
        <div class="card">
            <h4>${m.nama}</h4>
            <p>Rp ${m.harga.toLocaleString("id-ID")}</p>
            <button type="button" onclick="add(${m.id},'makanan')">+ Tambah</button>
        </div>
    `).join("");

    document.getElementById("minuman").innerHTML =
    minuman.map(m => `
        <div class="card">
            <h4>${m.nama}</h4>
            <p>Rp ${m.harga.toLocaleString("id-ID")}</p>
            <button type="button" onclick="add(${m.id},'minuman')">+ Tambah</button>
        </div>
    `).join("");
}


function add(id,type){

    let item =
        type === "makanan"
        ? makanan.find(m => m.id === id)
        : minuman.find(m => m.id === id);
>>>>>>> 8557e0f802d4a2f0a33812e1cfb10dec8f98ac3a

    let exist = cart.find(c => c.id === id);

    if(exist){
        exist.qty++;
    }else{
        cart.push({...item, qty:1});
    }

    renderCart();
}

/* ================= CART ================= */
function renderCart(){

    let total = 0;

    document.getElementById("cart").innerHTML =
    cart.map(c => {
        total += c.harga * c.qty;

        return `
        <div>
            ${c.nama} x${c.qty}
            <button onclick="removeItem(${c.id})">  X   </button>
        </div>
        `;
    }).join("");

    document.getElementById("total").innerText =
    "Rp " + total.toLocaleString("id-ID");
}

/* ================= REMOVE ================= */
function removeItem(id){
    cart = cart.filter(c => c.id !== id);
    renderCart();
}


document.getElementById("formReservasi").addEventListener("submit", function(e){
    e.preventDefault();

    const data = {
        id:"RES-"+Date.now(),

        nama:document.getElementById("nama").value,
        email:document.getElementById("email").value,
        telp:document.getElementById("telp").value,
        tanggal:document.getElementById("tanggal").value,
        jam:document.getElementById("jam").value,
        jumlah:document.getElementById("jumlah").value,
        catatan:document.getElementById("catatan").value,

        items:cart
    };

    let old = JSON.parse(localStorage.getItem("galaxy_reservasi") || "[]");
    old.push(data);

<<<<<<< HEAD
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
=======
    localStorage.setItem("galaxy_reservasi", JSON.stringify(old));

    alert("Reservasi berhasil!");

    cart = [];
    renderCart();

    window.location.href = "../pages/dashboard.html";
});

/* ================= TAB FUNCTION ================= */
function showTab(tab){

    // sembunyikan semua
    document.querySelectorAll(".tab-content")
    .forEach(el => el.classList.remove("active"));

    // reset button
    document.querySelectorAll(".tab")
    .forEach(el => el.classList.remove("active"));

    // tampilkan yang dipilih
    document.getElementById(tab).classList.add("active");

    // active button
    event.target.classList.add("active");
}

/* INIT */
renderMenu();
>>>>>>> 8557e0f802d4a2f0a33812e1cfb10dec8f98ac3a
