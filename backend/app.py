# backend/app.py
from flask import Flask, render_template, request, redirect, url_for
import logic

# Mengarahkan Flask ke folder frontend yang berada di luar direktori backend
app = Flask(__name__, 
            template_folder='../frontend', 
            static_folder='../frontend', 
            static_url_path='')

# Pastikan struktur tabel database siap saat aplikasi dinyalakan
try:
    logic.init_db()
except Exception as e:
    print(f"Peringatan: Gagal sinkronisasi database. Periksa MySQL Anda. Error: {e}")

# ========================================================
# ROUTING HALAMAN (RENDERING FRONTEND)
# ========================================================

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('pages/index.html')

@app.route('/login.html')
def login():
    return render_template('pages/login.html')

@app.route('/menu.html')
def menu():
    return render_template('pages/menu.html')

@app.route('/reservasi.html')
@app.route('/reservasi')
def reservasi():
    return render_template('pages/reservasi.html')

@app.route('/dashboard.html')
@app.route('/dashboard')
def dashboard():
    # Mengambil data asli dari MySQL melalui logic.py
    daftar_pesanan = logic.ambil_semua_reservasi()
    total_pesanan = len(daftar_pesanan)
    
    # Mengirimkan data dinamis ke Dashboard.html
    return render_template('pages/dashboard.html', 
                           pesanan_list=daftar_pesanan, 
                           total_pesanan=total_pesanan)

# ========================================================
# ROUTING AKSI (LOGIKA PROSES FORM)
# ========================================================

@app.route('/proses_pesan', methods=['POST'])
def proses_pesan():
    nama = request.form.get('nama_pelanggan')
    menu = request.form.get('pilihan_menu')
    jumlah = request.form.get('jumlah')
    
    # Eksekusi fungsi di logic.py
    sukses = logic.tambah_reservasi(nama, menu, jumlah)
    
    if sukses:
        return redirect(url_for('dashboard'))
    return "Gagal memproses reservasi", 400

if __name__ == '__main__':
    app.run(debug=True)