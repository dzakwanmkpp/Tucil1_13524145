# Queens Puzzle Solver

Tugas Kecil 1 Strategi Algoritma 2024/2025
Penyelesaian Queens Puzzle dengan Algoritma Brute Force.

## Deskripsi Program

Program ini adalah solver untuk permainan "Queens Puzzle" (variasi dari N-Queens dengan tambahan aturan region warna). Tujuan permainan adalah menempatkan N ratu (queens) pada papan N×N sehingga memenuhi aturan berikut:
1. Tidak ada dua ratu dalam satu baris.
2. Tidak ada dua ratu dalam satu kolom.
3. Tidak ada dua ratu yang bersentuhan secara diagonal (tetangga).
4. Tidak ada dua ratu yang berada dalam region warna yang sama.

Program ini diimplementasikan menggunakan bahasa Python dengan algoritma Brute Force untuk mengecek setiap kemungkinan konfigurasi penempatan ratu hingga ditemukan solusi yang valid.

## Requirements

- Python 3.x (disarankan versi 3.8 ke atas)
- Library `tkinter` (biasanya sudah terinstall otomatis bersama Python) untuk menjalankan mode GUI.
- Sistem Operasi: Windows / Linux / macOS

## Cara Kompilasi

Program ini ditulis dalam bahasa Python yang bersifat *interpreted* (dijalankan per baris oleh interpreter), sehingga **tidak memerlukan proses kompilasi** menjadi file `.exe` atau binary terlebih dahulu. Source code dapat langsung dieksekusi.

## Cara Menjalankan Program

Pastikan Anda berada di direktori utama proyek (root folder) atau di dalam folder `src`.

### 1. Mode CLI (Command Line Interface)
Gunakan mode ini untuk menjalankan program lewat terminal.
Jalankan perintah berikut:
```bash
python src/main.py
```
Program akan meminta input:
- Nama file test case (misal: `testcase.txt`). Pastikan file berada di folder `test/` atau satu folder dengan program.
- Pilihan mode: **Langsung Solusi** (cepat) atau **Live Condition** (dengan animasi visualisasi proses).

### 2. Mode GUI (Graphical User Interface)
Gunakan mode ini untuk tampilan visual yang lebih interaktif.
Jalankan perintah berikut:
```bash
python src/gui.py
```
Fitur GUI:
- **Pilih File**: Membuka file explorer untuk memilih test case.
- **Solve**: Menjalankan algoritma pencarian solusi.
- **Skip**: Melewati animasi agar langsung menampilkan hasil akhir.
- **Simpan**: Menyimpan solusi board ke dalam file `.txt`.
- **Delay**: Mengatur kecepatan animasi pencarian.

## Struktur Folder

- `src/` : Berisi source code utama (`main.py`, `solver.py`, `gui.py`).
- `test/`: Berisi contoh file test case input (`.txt`).
- `doc/` : Dokumen laporan Tugas Kecil 1 Strategi Algoritma.
- `bin/` : Folder binary (kosong karena Python tidak butuh binary).

## Identitas Pembuat

**Dzakwan Muhammad Khairan P. P.**

NIM: 13524145

Program Studi Teknik Informatika

Institut Teknologi Bandung


