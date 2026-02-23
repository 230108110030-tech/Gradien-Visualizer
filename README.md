# 📐 Gradien Visualizer — Media Pembelajaran Matematika

**Media Pembelajaran Interaktif · SMP Kelas VIII**  
Dibuat oleh: Yustika Berlian Cindy Aprillia  
Untuk: SMP Negeri 2 Lawang, Kelas VIII-H

---

## 🚀 Deploy ke Streamlit Cloud (GitHub)

### Langkah-langkah:

1. **Upload file ke GitHub**
   - Buat repository baru di GitHub
   - Upload file `app.py` dan `requirements.txt` ke repository

2. **Deploy di Streamlit Cloud**
   - Buka [share.streamlit.io](https://share.streamlit.io)
   - Login dengan akun GitHub
   - Klik **New app**
   - Pilih repository dan branch yang sesuai
   - Pastikan **Main file path** diisi: `app.py`
   - Klik **Deploy!**

3. **Selesai!** Aplikasimu akan berjalan online dalam beberapa menit.

---

## 💻 Menjalankan Secara Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ✨ Fitur Aplikasi

| Mode | Deskripsi |
|------|-----------|
| 📊 **Mode Visualizer** | Input koordinat dua titik, hitung gradien, tampilkan grafik, dan lihat langkah-langkah perhitungan |
| 🎯 **Mode Drill Practice** | Latihan soal interaktif dengan grafik acak, cek jawaban, dan skor otomatis |
| 📚 **Review Materi** | Ringkasan materi gradien garis lurus lengkap dengan rumus, contoh, dan tips |

---

## 📁 Struktur File

```
├── app.py              # Aplikasi utama Streamlit
├── requirements.txt    # Daftar dependensi Python
└── README.md           # Panduan ini
```
