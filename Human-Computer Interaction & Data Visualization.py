# Sesi 5: Membuat dashboard monitoring sederhana berbasis HTML
data_metrik = [
    {"nama": "Efisiensi Server", "nilai": 92, "status": "OPTIMAL", "warna": "#2ecc71"},
    {"nama": "Penggunaan Memori", "nilai": 78, "status": "WASPADA", "warna": "#f39c12"},
    {"nama": "Transaksi Gagal", "nilai": 14, "status": "KRITIS", "warna": "#e74c3c"},
    {"nama": "Akurasi Model", "nilai": 88, "status": "OPTIMAL", "warna": "#2ecc71"},
    {"nama": "Respons Antarmuka (ms)", "nilai": 95, "status": "OPTIMAL", "warna": "#2ecc71"}
]

kartu = ""
for metrik in data_metrik:
    kartu += f"""
    <section class="card" style="border-top-color:{metrik['warna']}">
      <h2>{metrik['nama']}</h2>
      <p class="nilai">{metrik['nilai']}</p>
      <span style="background:{metrik['warna']}" class="badge">{metrik['status']}</span>
    </section>
    """

html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dashboard Monitoring</title>
<style>
body {{font-family:Arial,sans-serif;background:#f2f5f9;color:#273444;padding:24px}}
.grid {{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px}}
.card {{background:white;padding:18px;border-radius:10px;border-top:5px solid;box-shadow:0 2px 8px #0001}}
.card h2 {{font-size:16px}}
.nilai {{font-size:32px;font-weight:bold;margin:14px 0}}
.badge {{color:white;padding:5px 10px;border-radius:14px;font-size:12px}}
button {{margin-top:22px;padding:10px 16px;border:0;border-radius:6px;background:#2463a6;color:white;cursor:pointer}}
#hasil {{display:none;background:#e5f2fb;padding:12px;margin-top:12px}}
</style>
</head>
<body>
<h1>Dashboard Monitoring Operasional</h1>
<p>Ringkasan kondisi beberapa indikator sistem.</p>
<div class="grid">{kartu}</div>
<button onclick="diagnostik()">Jalankan Diagnostik</button>
<div id="hasil"></div>
<script>
function diagnostik() {{
  const hasil = document.getElementById('hasil');
  hasil.style.display = 'block';
  hasil.textContent = 'Pemeriksaan selesai. Perhatian diperlukan pada indikator Transaksi Gagal.';
}}
</script>
</body>
</html>
"""

nama_file = "dashboard_imk.html"
with open(nama_file, "w", encoding="utf-8") as file:
    file.write(html)

print("Dashboard berhasil dibuat:", nama_file)
print("Buka file HTML tersebut melalui browser untuk melihat hasilnya.")
