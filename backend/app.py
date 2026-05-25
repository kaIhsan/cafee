from flask import Flask, request, jsonify
from flask_cors import CORS
from logic import (
    get_all_menu,
    get_menu_by_kategori,
    tambah_menu,
    hapus_menu,
    get_all_reservasi,
    tambah_reservasi,
    hapus_reservasi,
    update_status_reservasi,
    get_dashboard_stats,
    get_all_pesanan,
    tambah_pesanan,
    update_status_pesanan,
)
 
app = Flask(__name__)
CORS(app)  # Mengizinkan request dari frontend (HTML/JS)
 
# ─────────────────────────────────────────
#  ROOT
# ─────────────────────────────────────────
@app.route("/")
def index():
    return jsonify({"message": "API Cafe Backend aktif ✓", "versi": "1.0"})
 
 
# ═════════════════════════════════════════
#  MENU
# ═════════════════════════════════════════
 
@app.route("/api/menu", methods=["GET"])
def api_get_menu():
    """Ambil semua menu atau filter berdasarkan kategori."""
    kategori = request.args.get("kategori")        # ?kategori=minuman
    if kategori:
        data = get_menu_by_kategori(kategori)
    else:
        data = get_all_menu()
    return jsonify({"status": "ok", "data": data})
 
 
@app.route("/api/menu", methods=["POST"])
def api_tambah_menu():
    """Tambah item menu baru."""
    body = request.get_json()
    required = ["nama", "kategori", "harga", "deskripsi"]
    for field in required:
        if field not in body:
            return jsonify({"status": "error", "pesan": f"Field '{field}' wajib diisi"}), 400
 
    item = tambah_menu(
        nama=body["nama"],
        kategori=body["kategori"],
        harga=body["harga"],
        deskripsi=body["deskripsi"],
        gambar=body.get("gambar", ""),
    )
    return jsonify({"status": "ok", "pesan": "Menu berhasil ditambahkan", "data": item}), 201
 
 
@app.route("/api/menu/<int:menu_id>", methods=["DELETE"])
def api_hapus_menu(menu_id):
    """Hapus item menu berdasarkan ID."""
    hasil = hapus_menu(menu_id)
    if hasil:
        return jsonify({"status": "ok", "pesan": "Menu berhasil dihapus"})
    return jsonify({"status": "error", "pesan": "Menu tidak ditemukan"}), 404
 
 
# ═════════════════════════════════════════
#  RESERVASI
# ═════════════════════════════════════════
 
@app.route("/api/reservasi", methods=["GET"])
def api_get_reservasi():
    """Ambil semua data reservasi."""
    return jsonify({"status": "ok", "data": get_all_reservasi()})
 
 
@app.route("/api/reservasi", methods=["POST"])
def api_tambah_reservasi():
    """Buat reservasi baru."""
    body = request.get_json()
    required = ["nama", "tanggal", "jam", "jumlah_orang"]
    for field in required:
        if field not in body:
            return jsonify({"status": "error", "pesan": f"Field '{field}' wajib diisi"}), 400
 
    reservasi = tambah_reservasi(
        nama=body["nama"],
        tanggal=body["tanggal"],
        jam=body["jam"],
        jumlah_orang=body["jumlah_orang"],
        telepon=body.get("telepon", "-"),
        catatan=body.get("catatan", ""),
    )
    return jsonify({"status": "ok", "pesan": "Reservasi berhasil dibuat", "data": reservasi}), 201
 
 
@app.route("/api/reservasi/<int:reservasi_id>", methods=["DELETE"])
def api_hapus_reservasi(reservasi_id):
    """Batalkan / hapus reservasi."""
    hasil = hapus_reservasi(reservasi_id)
    if hasil:
        return jsonify({"status": "ok", "pesan": "Reservasi berhasil dihapus"})
    return jsonify({"status": "error", "pesan": "Reservasi tidak ditemukan"}), 404
 
 
@app.route("/api/reservasi/<int:reservasi_id>/status", methods=["PATCH"])
def api_update_status_reservasi(reservasi_id):
    """Update status reservasi: menunggu | dikonfirmasi | selesai | dibatalkan."""
    body = request.get_json()
    status_baru = body.get("status")
    valid = ["menunggu", "dikonfirmasi", "selesai", "dibatalkan"]
    if status_baru not in valid:
        return jsonify({"status": "error", "pesan": f"Status harus salah satu dari: {valid}"}), 400
 
    hasil = update_status_reservasi(reservasi_id, status_baru)
    if hasil:
        return jsonify({"status": "ok", "pesan": f"Status diperbarui menjadi '{status_baru}'", "data": hasil})
    return jsonify({"status": "error", "pesan": "Reservasi tidak ditemukan"}), 404
 
 
# ═════════════════════════════════════════
#  PESANAN
# ═════════════════════════════════════════
 
@app.route("/api/pesanan", methods=["GET"])
def api_get_pesanan():
    """Ambil semua pesanan."""
    return jsonify({"status": "ok", "data": get_all_pesanan()})
 
 
@app.route("/api/pesanan", methods=["POST"])
def api_tambah_pesanan():
    """
    Buat pesanan baru.
    Body: { "nama_pelanggan": str, "meja": int, "items": [{"menu_id": int, "qty": int}] }
    """
    body = request.get_json()
    required = ["nama_pelanggan", "meja", "items"]
    for field in required:
        if field not in body:
            return jsonify({"status": "error", "pesan": f"Field '{field}' wajib diisi"}), 400
 
    pesanan = tambah_pesanan(
        nama_pelanggan=body["nama_pelanggan"],
        meja=body["meja"],
        items=body["items"],
    )
    if pesanan is None:
        return jsonify({"status": "error", "pesan": "Satu atau lebih menu tidak ditemukan"}), 400
 
    return jsonify({"status": "ok", "pesan": "Pesanan berhasil dibuat", "data": pesanan}), 201
 
 
@app.route("/api/pesanan/<int:pesanan_id>/status", methods=["PATCH"])
def api_update_status_pesanan(pesanan_id):
    """Update status pesanan: diproses | siap | selesai."""
    body = request.get_json()
    status_baru = body.get("status")
    valid = ["diproses", "siap", "selesai"]
    if status_baru not in valid:
        return jsonify({"status": "error", "pesan": f"Status harus salah satu dari: {valid}"}), 400
 
    hasil = update_status_pesanan(pesanan_id, status_baru)
    if hasil:
        return jsonify({"status": "ok", "pesan": f"Status pesanan diperbarui", "data": hasil})
    return jsonify({"status": "error", "pesan": "Pesanan tidak ditemukan"}), 404
 
 
# ═════════════════════════════════════════
#  DASHBOARD
# ═════════════════════════════════════════
 
@app.route("/api/dashboard", methods=["GET"])
def api_dashboard():
    """Statistik ringkasan untuk halaman dashboard."""
    return jsonify({"status": "ok", "data": get_dashboard_stats()})
 
 
# ─────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)