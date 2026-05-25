<<<<<<< HEAD
"""
logic.py — Lapisan logika bisnis Cafe Backend
Menyimpan data di memori (in-memory). 
Untuk produksi, ganti dengan database (SQLite / MySQL / PostgreSQL).
"""
 
from datetime import datetime
 
# ─────────────────────────────────────────
#  DATABASE SEMENTARA (IN-MEMORY)
# ─────────────────────────────────────────
 
_menu = [
    {"id": 1, "nama": "Kopi Hitam",       "kategori": "minuman", "harga": 15000, "deskripsi": "Kopi arabika murni tanpa gula",         "gambar": "kopi_hitam.jpg"},
    {"id": 2, "nama": "Cappuccino",        "kategori": "minuman", "harga": 25000, "deskripsi": "Espresso dengan susu dikukus dan busa",  "gambar": "cappuccino.jpg"},
    {"id": 3, "nama": "Matcha Latte",      "kategori": "minuman", "harga": 28000, "deskripsi": "Teh hijau Jepang dengan susu segar",     "gambar": "matcha.jpg"},
    {"id": 4, "nama": "Croissant",         "kategori": "makanan", "harga": 22000, "deskripsi": "Roti croissant mentega hangat",          "gambar": "croissant.jpg"},
    {"id": 5, "nama": "Sandwich Club",     "kategori": "makanan", "harga": 35000, "deskripsi": "Sandwich ayam dengan sayuran segar",     "gambar": "sandwich.jpg"},
    {"id": 6, "nama": "Cheesecake",        "kategori": "dessert", "harga": 30000, "deskripsi": "Cheesecake lembut dengan topping stroberi","gambar": "cheesecake.jpg"},
    {"id": 7, "nama": "Es Kopi Susu",      "kategori": "minuman", "harga": 22000, "deskripsi": "Kopi susu dingin khas Indonesia",        "gambar": "es_kopi_susu.jpg"},
    {"id": 8, "nama": "Nasi Goreng Cafe",  "kategori": "makanan", "harga": 40000, "deskripsi": "Nasi goreng spesial dengan telur mata sapi","gambar": "nasi_goreng.jpg"},
]
 
_reservasi = [
    {
        "id": 1, "nama": "Budi Santoso", "tanggal": "2025-06-01",
        "jam": "18:00", "jumlah_orang": 4,
        "telepon": "08123456789", "catatan": "Ulang tahun",
        "status": "dikonfirmasi",
        "dibuat_pada": "2025-05-25T10:00:00",
    },
]
 
_pesanan = []
 
# Counter ID
_menu_id_counter     = max(m["id"] for m in _menu) + 1
_reservasi_id_counter = max(r["id"] for r in _reservasi) + 1
_pesanan_id_counter  = 1
 
 
# ═════════════════════════════════════════
#  MENU
# ═════════════════════════════════════════
 
def get_all_menu():
    return list(_menu)
 
 
def get_menu_by_kategori(kategori: str):
    return [m for m in _menu if m["kategori"].lower() == kategori.lower()]
 
 
def get_menu_by_id(menu_id: int):
    return next((m for m in _menu if m["id"] == menu_id), None)
 
 
def tambah_menu(nama: str, kategori: str, harga: float, deskripsi: str, gambar: str = "") -> dict:
    global _menu_id_counter
    item = {
        "id":        _menu_id_counter,
        "nama":      nama,
        "kategori":  kategori,
        "harga":     harga,
        "deskripsi": deskripsi,
        "gambar":    gambar,
    }
    _menu.append(item)
    _menu_id_counter += 1
    return item
 
 
def hapus_menu(menu_id: int) -> bool:
    global _menu
    sebelum = len(_menu)
    _menu = [m for m in _menu if m["id"] != menu_id]
    return len(_menu) < sebelum
 
 
# ═════════════════════════════════════════
#  RESERVASI
# ═════════════════════════════════════════
 
def get_all_reservasi():
    return list(_reservasi)
 
 
def tambah_reservasi(nama: str, tanggal: str, jam: str,
                     jumlah_orang: int, telepon: str = "-", catatan: str = "") -> dict:
    global _reservasi_id_counter
    item = {
        "id":           _reservasi_id_counter,
        "nama":         nama,
        "tanggal":      tanggal,
        "jam":          jam,
        "jumlah_orang": jumlah_orang,
        "telepon":      telepon,
        "catatan":      catatan,
        "status":       "menunggu",
        "dibuat_pada":  datetime.now().isoformat(),
    }
    _reservasi.append(item)
    _reservasi_id_counter += 1
    return item
 
 
def hapus_reservasi(reservasi_id: int) -> bool:
    global _reservasi
    sebelum = len(_reservasi)
    _reservasi = [r for r in _reservasi if r["id"] != reservasi_id]
    return len(_reservasi) < sebelum
 
 
def update_status_reservasi(reservasi_id: int, status_baru: str):
    for r in _reservasi:
        if r["id"] == reservasi_id:
            r["status"] = status_baru
            return r
    return None
 
 
# ═════════════════════════════════════════
#  PESANAN
# ═════════════════════════════════════════
 
def get_all_pesanan():
    return list(_pesanan)
 
 
def tambah_pesanan(nama_pelanggan: str, meja: int, items: list):
    """
    items: [{"menu_id": int, "qty": int}, ...]
    Menghitung total harga otomatis dari data menu.
    """
    global _pesanan_id_counter
 
    detail_items = []
    total_harga  = 0
 
    for item in items:
        menu = get_menu_by_id(item["menu_id"])
        if menu is None:
            return None  # Menu tidak ditemukan
        qty      = item.get("qty", 1)
        subtotal = menu["harga"] * qty
        total_harga += subtotal
        detail_items.append({
            "menu_id":   menu["id"],
            "nama_menu": menu["nama"],
            "harga":     menu["harga"],
            "qty":       qty,
            "subtotal":  subtotal,
        })
 
    pesanan = {
        "id":             _pesanan_id_counter,
        "nama_pelanggan": nama_pelanggan,
        "meja":           meja,
        "items":          detail_items,
        "total_harga":    total_harga,
        "status":         "diproses",
        "dibuat_pada":    datetime.now().isoformat(),
    }
    _pesanan.append(pesanan)
    _pesanan_id_counter += 1
    return pesanan
 
 
def update_status_pesanan(pesanan_id: int, status_baru: str):
    for p in _pesanan:
        if p["id"] == pesanan_id:
            p["status"] = status_baru
            return p
    return None
 
 
# ═════════════════════════════════════════
#  DASHBOARD STATS
# ═════════════════════════════════════════
 
def get_dashboard_stats() -> dict:
    total_menu      = len(_menu)
    total_reservasi = len(_reservasi)
    total_pesanan   = len(_pesanan)
 
    # Hitung pendapatan dari pesanan yang selesai
    pendapatan = sum(
        p["total_harga"] for p in _pesanan if p["status"] == "selesai"
    )
 
    # Reservasi hari ini
    hari_ini = datetime.now().strftime("%Y-%m-%d")
    reservasi_hari_ini = sum(
        1 for r in _reservasi if r["tanggal"] == hari_ini
    )
 
    # Pesanan aktif (diproses / siap)
    pesanan_aktif = sum(
        1 for p in _pesanan if p["status"] in ("diproses", "siap")
    )
 
    # Kategori menu
    kategori_count = {}
    for m in _menu:
        k = m["kategori"]
        kategori_count[k] = kategori_count.get(k, 0) + 1
 
    return {
        "total_menu":          total_menu,
        "total_reservasi":     total_reservasi,
        "total_pesanan":       total_pesanan,
        "pendapatan_selesai":  pendapatan,
        "reservasi_hari_ini":  reservasi_hari_ini,
        "pesanan_aktif":       pesanan_aktif,
        "kategori_menu":       kategori_count,
    }
=======
# backend/logic.py
import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime

# Konfigurasi Database
db_config = {
    'host': 'localhost',
    'user': 'root',       # Sesuaikan dengan user MySQL Anda
    'password': '',       # Sesuaikan dengan password MySQL Anda
    'database': 'cafe_db'
}

def get_connection():
    """Membuat koneksi ke database MySQL."""
    return mysql.connector.connect(**db_config)

def init_db():
    """Inisialisasi tabel reservasi jika belum ada di database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservasi (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_pesanan VARCHAR(20) NOT NULL,
            nama_pelanggan VARCHAR(100) NOT NULL,
            pilihan_menu VARCHAR(100) NOT NULL,
            jumlah INT NOT NULL,
            total_harga INT NOT NULL,
            tanggal VARCHAR(50) NOT NULL,
            status VARCHAR(20) DEFAULT 'Diproses'
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def tambah_reservasi(nama, menu, jumlah):
    """Logika bisnis menghitung harga dan memasukkan data ke MySQL."""
    if not nama or not menu or not jumlah:
        return False
        
    id_pesanan = f"#ORD-{random.randint(8000, 8999)}"
    
    # Menentukan harga fiktif berdasarkan menu dari frontend
    harga_satuan = 20000 if "Kopi" in menu else 15000
    total_harga = harga_satuan * int(jumlah)
    
    # Format tanggal disesuaikan dengan format statis frontend ("25 Mei 2026")
    tanggal_sekarang = datetime.now().strftime("%d %b %Y")
    
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO reservasi (id_pesanan, nama_pelanggan, pilihan_menu, jumlah, total_harga, tanggal)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (id_pesanan, nama, menu, int(jumlah), total_harga, tanggal_sekarang))
    conn.commit()
    cursor.close()
    conn.close()
    return True

<<<<<<< HEAD
def ambil_semua_pesanan():
    """
    Fungsi untuk menarik data yang akan disajikan ke Dashboard.
    """
    return mock_database
>>>>>>> b2f13c8236396592e4a73a72a87335505ad27296
=======
def ambil_semua_reservasi():
    """Mengambil riwayat data pesanan untuk disajikan di Dashboard."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reservasi ORDER BY id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
>>>>>>> 8b25df1a6dc8142a68ef4f276ffde9c218277829
