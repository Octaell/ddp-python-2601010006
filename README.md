Set-Content -Path "README.MD" -Encoding UTF8 -Value @'
# 🐍 Latihan Dasar-Dasar Pemrograman — Pertemuan 6

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Selesai-22c55e?style=for-the-badge)
![Mata Kuliah](https://img.shields.io/badge/Mata%20Kuliah-DDP-f59e0b?style=for-the-badge)

</div>

---

## 👤 Identitas Mahasiswa

| Field     | Detail                       |
|-----------|------------------------------|
| **Nama**  | I Made Samuel Ulung Prasetya |
| **NIM**   | 2601010006                   |
| **Kelas** | SI PAGI1                     |

---

## 📁 Daftar Latihan

| No | File | Deskripsi |
|----|------|-----------|
| 1 | [`latihan1_biodata.py`](latihan1_biodata.py) | Menampilkan biodata diri menggunakan **f-string** |
| 2 | [`latihan2_persegi_panjang.py`](latihan2_persegi_panjang.py) | Menghitung **luas** dan **keliling** persegi panjang dari input pengguna |
| 3 | [`latihan3_konversi_suhu.py`](latihan3_konversi_suhu.py) | Mengkonversi suhu **Celsius → Fahrenheit & Kelvin** |
| 4 | [`latihan4_total_belanja.py`](latihan4_total_belanja.py) | Menghitung **total belanja** dengan PPN 11% |

---

## 🚀 Cara Menjalankan

> **Prasyarat:** Pastikan [Python 3.x](https://www.python.org/downloads/) sudah terinstall.
> Cek versi Python dengan: `python --version`

Buka **terminal / command prompt** di folder project ini, lalu jalankan salah satu perintah berikut:

---

### 1️⃣ Latihan 1 — Biodata (f-string)

```bash
python latihan1_biodata.py
```

**Contoh Output:**
```
Nama: Made Samuel
NIM: 2601010006
Prodi: Sistem Informasi
Hobi: baca komik dan main game
```

---

### 2️⃣ Latihan 2 — Persegi Panjang

```bash
python latihan2_persegi_panjang.py
```

**Contoh Input & Output:**
```
masukkan panjang: 5
masukkan lebar: 3
Luas: 15.0 m2
Keliling: 16.0 m
```

---

### 3️⃣ Latihan 3 — Konversi Suhu

```bash
python latihan3_konversi_suhu.py
```

**Contoh Input & Output:**
```
masukkan suhu celcius: 100
212.00°F dan 373.15°K
```

---

### 4️⃣ Latihan 4 — Total Belanja

```bash
python latihan4_total_belanja.py
```

**Contoh Input & Output:**
```
masukkan nama barang, harga satuan, jumlah (pisahkan pake koma :) Buku, 15000, 3
Subtotal = 45000 PPN= 4950.0 Total= 49950.0
```

> 💡 **Tips:** Input dipisahkan dengan **koma (,)**
> Format: `nama barang, harga satuan, jumlah`

---

## 🗂️ Struktur Folder

```
ddp-python/
│
├── 📄 README.md
├── 🐍 latihan1_biodata.py
├── 🐍 latihan2_persegi_panjang.py
├── 🐍 latihan3_konversi_suhu.py
└── 🐍 latihan4_total_belanja.py
```

---

<div align="center">
  <sub>✨ Dibuat dengan semangat belajar untuk mata kuliah Dasar-Dasar Pemrograman</sub>
</div>
'@
