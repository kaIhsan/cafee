-- ============================================
-- DATABASE: Galaxy Cafeshop
-- File: cafe.sql
-- ============================================

CREATE DATABASE IF NOT EXISTS galaxy_cafe;
USE galaxy_cafe;

-- --------------------------------------------
-- TABEL: users
-- --------------------------------------------
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('member', 'admin') DEFAULT 'member',
    poin INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- --------------------------------------------
-- TABEL: kategori_menu
-- --------------------------------------------
CREATE TABLE kategori_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_kategori VARCHAR(50) NOT NULL
);

INSERT INTO kategori_menu (nama_kategori) VALUES
('Makanan'),
('Minuman');

-- --------------------------------------------
-- TABEL: menu
-- (sesuai data di reservasi.js & reservasi.html)
-- --------------------------------------------
CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_menu VARCHAR(100) NOT NULL,
    kategori_id INT NOT NULL,
    harga INT NOT NULL,
    deskripsi TEXT,
    tersedia TINYINT(1) DEFAULT 1,
    FOREIGN KEY (kategori_id) REFERENCES kategori_menu(id)
);

INSERT INTO menu (nama_menu, kategori_id, harga, deskripsi) VALUES
-- Makanan
('Roti Bakar Cokelat Keju',  1, 15000, 'Roti bakar dengan topping cokelat dan keju'),
('Kentang Goreng Garing',    1, 20000, 'Kentang goreng crispy'),
('Nasi Goreng Bimasakti',    1, 30000, 'Nasi goreng khas Galaxy Cafe'),
('Spaghetti',                1, 35000, 'Spaghetti saus bolognese'),
-- Minuman
('Kopi Susu Gula Aren',      2, 20000, 'Kopi susu dengan gula aren pilihan'),
('Americano Iced',           2, 18000, 'Espresso dingin tanpa susu'),
('Matcha Latte Creamy',      2, 25000, 'Matcha premium dengan susu creamy'),
('Nebula Lychee Tea',        2, 15000, 'Teh lychee segar khas Galaxy Cafe');

-- --------------------------------------------
-- TABEL: reservasi
-- (primary key: id — dihubungkan ke dashboard)
-- --------------------------------------------
CREATE TABLE reservasi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_pesanan VARCHAR(20) UNIQUE NOT NULL,
    user_id INT,
    nama_pemesan VARCHAR(100) NOT NULL,
    menu_id INT NOT NULL,
    jumlah INT NOT NULL DEFAULT 1,
    total_harga INT NOT NULL,
    tanggal DATE NOT NULL,
    status ENUM('baru', 'diproses', 'selesai', 'dibatalkan') DEFAULT 'baru',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
    FOREIGN KEY (menu_id) REFERENCES menu(id)
);

-- Contoh data awal (sesuai dashboard.html)
INSERT INTO reservasi (kode_pesanan, nama_pemesan, menu_id, jumlah, total_harga, tanggal, status) VALUES
('#ORD-8821', 'Ajaraaa Aja',  3, 1, 35000, '2026-05-25', 'diproses'),
('#ORD-8790', 'Mba Nai Nai',  7, 1, 25000, '2026-05-22', 'selesai'),
('#ORD-8755', 'Aalfiraner',   8, 1, 18000, '2026-05-20', 'selesai'),
('#ORD-8740', 'Siq Irwaner',  3, 1, 30000, '2026-05-18', 'selesai');

-- --------------------------------------------
-- SAMPLE USER
-- --------------------------------------------
INSERT INTO users (nama, email, password, role, poin) VALUES
('Budi Selepet', 'budi@galaxycafe.id', 'hashed_password_here', 'member', 450),
('Admin Galaxy', 'admin@galaxycafe.id', 'hashed_password_here', 'admin', 0);