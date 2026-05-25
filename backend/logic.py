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

# Simulasi database menggunakan list (In-Memory Data)
mock_database = []

def proses_pesanan_baru(nama, menu, jumlah):
    """
    Fungsi untuk memvalidasi dan memproses pesanan baru.
    """
    # Validasi dasar
    if not nama or not menu or not jumlah:
        return {"sukses": False, "pesan": "Data pesanan tidak lengkap."}
    
    try:
        jumlah_int = int(jumlah)
        if jumlah_int <= 0:
            raise ValueError
    except ValueError:
        return {"sukses": False, "pesan": "Jumlah harus berupa angka positif."}

    # Logika bisnis: Generate ID dan Hitung Harga (Simulasi)
    id_pesanan = f"#ORD-{len(mock_database) + 8000}"
    harga_satuan = 20000 if "Kopi" in menu else 15000
    total_harga = harga_satuan * jumlah_int

    data_pesanan = {
        "id_pesanan": id_pesanan,
        "nama": nama,
        "menu": menu,
        "jumlah": jumlah_int,
        "total_harga": total_harga,
        "status": "Diproses"
    }

    # Simpan ke memori sementara
    mock_database.append(data_pesanan)
    
    return {"sukses": True, "pesan": "Pesanan berhasil dibuat.", "data": data_pesanan}

def ambil_semua_pesanan():
    """
    Fungsi untuk menarik data yang akan disajikan ke Dashboard.
    """
    return mock_database
>>>>>>> b2f13c8236396592e4a73a72a87335505ad27296
