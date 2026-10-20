# Dokumentasi Praktikum Seminar Informatika (Sesi 1–6)

Repositori ini berisi kumpulan program Python yang dikembangkan berdasarkan studi kasus dari enam sesi seminar Informatika. Pembahasan mencakup pengolahan data, pemrosesan paralel, sistem informasi geografis, pembelajaran mesin, interaksi manusia dan komputer, serta pemanfaatan AI untuk mengidentifikasi penyebab deforestasi.

---

### Sesi 1: Make Sense of Data with Analysis and AI

- **Narasumber:** Andria Arisal, S.T., M.Eng. (Pusat Riset Sains Data dan Informasi – BRIN)
- **Studi Kasus:** Analisis Risiko Piutang dan Penentuan Strategi Penanganan Kredit

**Penjelasan dan Implementasi:**

- **Pengolahan Data:** Menyiapkan dataset transaksi dengan memeriksa nilai yang tidak lengkap dan menggantinya menggunakan median agar data dapat diproses lebih lanjut.
- **Analisis Bisnis:** Menggunakan analisis deskriptif untuk melihat kondisi piutang, analisis diagnostik untuk mengamati pola risiko berdasarkan diskon, serta analisis prediktif untuk memperkirakan kemungkinan gagal bayar.
- **Pemodelan dan Rekomendasi:** Menerapkan algoritma *Logistic Regression* untuk mengklasifikasikan risiko piutang. Hasil probabilitas model kemudian digunakan sebagai dasar simulasi rekomendasi kebijakan kredit.

---

### Sesi 2: Bridging Global Infrastructure to Address Local Challenges with HPC

- **Narasumber:** Asst. Prof. Dr. Worawan Diaz Carbalo (Thammasat University, Thailand)
- **Studi Kasus:** Pemodelan Penyebaran Polusi Udara PM2.5 dengan Pemrosesan Paralel

**Penjelasan dan Implementasi:**

- **Simulasi Polusi:** Membentuk grid dua dimensi yang menggambarkan persebaran konsentrasi polutan pada suatu wilayah. Perubahan konsentrasi dihitung secara berulang menggunakan pendekatan numerik.
- **Pembagian Proses:** Memanfaatkan modul `multiprocessing` untuk membagi area perhitungan menjadi beberapa bagian yang dapat dikerjakan oleh sejumlah proses secara bersamaan.
- **Pengukuran Kinerja:** Membandingkan waktu penyelesaian metode sekuensial dengan metode paralel. Perbandingan ini digunakan untuk mengetahui percepatan komputasi yang diperoleh dari pembagian beban kerja.

---

### Sesi 3: Career and Competition in Industrial Era with GIS

- **Narasumber:** Widi Primadepa, S.Kom. (Asset Management GIS Analyst di City Care Property, Selandia Baru)
- **Studi Kasus:** Pemantauan Kondisi Aset Infrastruktur Berdasarkan Informasi Geografis

**Penjelasan dan Implementasi:**

- **Pengelolaan Data Aset:** Menyimpan informasi setiap aset, seperti identitas, jenis, koordinat, usia, dan kondisi fisiknya dalam struktur data Python.
- **Perhitungan Spasial:** Menggunakan rumus *Haversine* untuk memperkirakan jarak antara lokasi aset dan pusat zona bahaya. Hasilnya digunakan untuk menentukan aset yang berada dalam jangkauan wilayah berisiko.
- **Penilaian dan Ekspor:** Menggabungkan usia aset, ukuran kerusakan, dan jarak dari zona bahaya untuk menentukan prioritas pemeriksaan. Data hasil pengolahan kemudian disusun dalam format GeoJSON agar dapat digunakan oleh perangkat lunak GIS.

---

### Sesi 4: Introduction to Machine Learning

- **Narasumber:** Dr. Taniza binti Tajuddin (Universiti Teknologi MARA / UiTM, Malaysia)
- **Studi Kasus:** Prediksi Kelayakan Pinjaman Menggunakan Algoritma Random Forest

**Penjelasan dan Implementasi:**

- **Persiapan Dataset:** Membuat data simulasi pemohon pinjaman yang mencakup pendapatan, jumlah pinjaman, skor kredit, usia, dan rasio utang. Data tersebut digunakan sebagai masukan dalam proses pembelajaran model.
- **Pelatihan Model:** Memisahkan dataset menjadi data latih sebesar 80% dan data pengujian sebesar 20%. Selanjutnya, algoritma *Random Forest Classifier* digunakan untuk mempelajari pola yang berkaitan dengan status persetujuan pinjaman.
- **Pengujian Prediksi:** Mengevaluasi hasil klasifikasi menggunakan *Confusion Matrix*, *Precision*, *Recall*, dan *F1-Score*. Model yang telah dilatih juga dicoba pada data pemohon baru untuk memperlihatkan hasil prediksi dan probabilitas persetujuannya.

---

### Sesi 5: Human-Computer Interaction & Data Visualization

- **Narasumber:** Dr. Arafat Febriandirza (Kepala Kelompok Riset IMK & Visualisasi – BRIN)
- **Studi Kasus:** Pembuatan Dashboard Pemantauan Kinerja Sistem dengan Antarmuka Interaktif

**Penjelasan dan Implementasi:**

- **Penyajian Informasi:** Menampilkan beberapa indikator operasional dalam bentuk kartu agar pengguna dapat membaca nilai dan kondisi setiap metrik dengan lebih mudah.
- **Penerapan Prinsip Visual:** Menggunakan perbedaan warna untuk membedakan kondisi optimal, waspada, dan kritis. Pengelompokan informasi dalam kartu juga membantu menjaga tampilan tetap teratur dan mudah dipindai.
- **Interaksi Pengguna:** Membuat tombol diagnostik menggunakan JavaScript yang menampilkan pesan setelah ditekan. Fitur ini menjadi contoh penerapan *affordance*, visibilitas fungsi, dan umpan balik sistem dalam sebuah antarmuka.

---

### Sesi 6: Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

- **Narasumber:** Dr. Bart Slagter (Laboratory of Geo-Information Science & Remote Sensing)
- **Studi Kasus:** Identifikasi Faktor Penyebab Deforestasi Menggunakan Data Satelit dan Machine Learning

**Penjelasan dan Implementasi:**

- **Pembentukan Data:** Menyusun dataset simulasi yang memuat perubahan indeks vegetasi NDVI, perubahan indeks kebakaran NBR, jarak lokasi dari jalan, dan luas area yang mengalami pembukaan tutupan lahan.
- **Pengelompokan Penyebab:** Menentukan label awal berdasarkan aturan tertentu untuk membedakan kemungkinan kebakaran hutan dan lahan, perkebunan, pembangunan infrastruktur jalan, serta perambahan skala kecil.
- **Klasifikasi dengan AI:** Melatih model *Random Forest Classifier* menggunakan fitur yang tersedia. Kinerja model diperiksa melalui laporan klasifikasi, kemudian model digunakan untuk memperkirakan kategori penyebab pada sejumlah peringatan baru.

---

## Catatan

Seluruh program dalam repositori ini merupakan implementasi pembelajaran menggunakan data simulasi. Hasil perhitungan dan prediksi digunakan untuk memahami konsep serta alur kerja setiap bidang, bukan sebagai pengganti analisis lapangan atau sistem operasional yang telah tervalidasi.
