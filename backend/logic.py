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