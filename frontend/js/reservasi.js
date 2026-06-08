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

/* ================= CART ================= */
let cart = [];

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