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

def ambil_semua_reservasi():
    """Mengambil riwayat data pesanan untuk disajikan di Dashboard."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reservasi ORDER BY id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data