import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Sesi 1: Analisis data risiko piutang
np.random.seed(42)
jumlah_data = 250

df = pd.DataFrame({
    "invoice_id": [f"INV-{1000+i}" for i in range(jumlah_data)],
    "total_belanja": np.random.uniform(5, 120, jumlah_data),
    "diskon_persen": np.random.choice([0, 5, 10, 15, 25], jumlah_data),
    "lama_langganan_bulan": np.random.randint(1, 48, jumlah_data),
    "riwayat_telat_kali": np.random.poisson(1.3, jumlah_data)
})

# Simulasi nilai yang kosong
df.loc[12:18, "total_belanja"] = np.nan
df.loc[45:50, "lama_langganan_bulan"] = np.nan

# Nilai kosong diisi dengan median
for kolom in ["total_belanja", "lama_langganan_bulan"]:
    df[kolom] = df[kolom].fillna(df[kolom].median())

# Membuat label risiko berdasarkan aturan simulasi
skor_risiko = (
    (df["riwayat_telat_kali"] > 2).astype(int) * 0.4
    + (df["diskon_persen"] >= 15).astype(int) * 0.4
    + (df["lama_langganan_bulan"] < 6).astype(int) * 0.2
)
df["status_macet"] = (skor_risiko > 0.4).astype(int)

print("=== ANALISIS DESKRIPTIF ===")
jumlah_macet = int(df["status_macet"].sum())
print(f"Jumlah faktur: {len(df)}")
print(f"Faktur berisiko: {jumlah_macet} ({jumlah_macet / len(df) * 100:.2f}%)")
print(f"Rata-rata belanja: Rp {df['total_belanja'].mean():.2f} juta")

print("\n=== ANALISIS BERDASARKAN DISKON ===")
tabel = pd.crosstab(df["diskon_persen"], df["status_macet"], normalize="index") * 100
print(tabel.round(1).rename(columns={0: "Lancar (%)", 1: "Macet (%)"}))

# Melatih model prediksi sederhana
fitur = ["total_belanja", "diskon_persen",
         "lama_langganan_bulan", "riwayat_telat_kali"]
X = df[fitur]
y = df["status_macet"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
prediksi = model.predict(X_test)

print("\n=== EVALUASI MODEL ===")
print(classification_report(
    y_test, prediksi, labels=[0, 1],
    target_names=["Lancar", "Macet"], zero_division=0
))

def rekomendasi(probabilitas):
    if probabilitas >= 0.65:
        return "Pembayaran tunai di muka"
    if probabilitas >= 0.35:
        return "Plafon terbatas dan pemeriksaan tambahan"
    return "Termin kredit normal"

hasil = X_test.copy()
hasil["risiko_macet"] = model.predict_proba(X_test)[:, 1]
hasil["rekomendasi"] = hasil["risiko_macet"].apply(rekomendasi)

print("\n=== CONTOH REKOMENDASI ===")
print(hasil[["risiko_macet", "rekomendasi"]].head().to_string())
