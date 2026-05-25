

from flask import Flask, request, jsonify
import logic  # Mengimpor logika bisnis yang sudah dipisah

app = Flask(__name__)

# Endpoint 1: Menerima pesanan (Digunakan oleh form Reservasi)
@app.route('/api/pesan', methods=['POST'])
def terima_pesanan():
    # Menangkap data form (Bisa dari request.form atau request.json)
    nama = request.form.get('nama_pelanggan')
    menu = request.form.get('pilihan_menu')
    jumlah = request.form.get('jumlah')

    # Mengoper data ke logic.py untuk diproses
    hasil = logic.proses_pesanan_baru(nama, menu, jumlah)

    # Mengembalikan respons HTTP (JSON)
    if hasil['sukses']:
        return jsonify(hasil), 201  # 201 Created
    else:
        return jsonify(hasil), 400  # 400 Bad Request

# Endpoint 2: Mengirim data ke Dashboard (Digunakan oleh admin/user)
@app.route('/api/dashboard', methods=['GET'])
def kirim_data_dashboard():
    # Mengambil data dari logic.py
    data_pesanan = logic.ambil_semua_pesanan()
    
    respons = {
        "total_pesanan_hari_ini": len(data_pesanan),
        "daftar_pesanan": data_pesanan
    }
    
    return jsonify(respons), 200  # 200 OK

if __name__ == '__main__':
    # Berjalan di port 5000
    app.run(debug=True, port=5000)