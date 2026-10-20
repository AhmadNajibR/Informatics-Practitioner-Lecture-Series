import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sesi 6: Mengelompokkan kemungkinan penyebab deforestasi
np.random.seed(42)
jumlah_alert = 350

df = pd.DataFrame({
    "alert_id": [f"ALT-{2026001+i}" for i in range(jumlah_alert)],
    "ndvi_loss": np.random.uniform(0.20, 0.90, jumlah_alert),
    "nbr_loss": np.random.uniform(0.05, 0.80, jumlah_alert),
    "jarak_jalan_m": np.random.exponential(1200, jumlah_alert),
    "luas_klaster_ha": np.random.lognormal(2.0, 0.8, jumlah_alert)
})

def klasifikasi_penyebab(baris):
    if baris["nbr_loss"] > 0.52:
        return "Karhutla"
    if baris["luas_klaster_ha"] >= 20 and baris["jarak_jalan_m"] < 3000:
        return "Perkebunan"
    if baris["jarak_jalan_m"] <= 250:
        return "Infrastruktur Jalan"
    return "Perambahan Kecil"

df["penyebab"] = df.apply(klasifikasi_penyebab, axis=1)

fitur = ["ndvi_loss", "nbr_loss", "jarak_jalan_m", "luas_klaster_ha"]
X, y = df[fitur], df["penyebab"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
prediksi = model.predict(X_test)

print("=== ANALISIS PENYEBAB DEFORESTASI ===")
print(f"Jumlah peringatan: {len(df)}")
print(f"Jumlah data uji: {len(X_test)}")
print("\nLaporan evaluasi:")
print(classification_report(y_test, prediksi, zero_division=0))

alert_baru = pd.DataFrame([
    {"ndvi_loss": 0.78, "nbr_loss": 0.65, "jarak_jalan_m": 1400, "luas_klaster_ha": 12.5},
    {"ndvi_loss": 0.60, "nbr_loss": 0.18, "jarak_jalan_m": 1500, "luas_klaster_ha": 45.0},
    {"ndvi_loss": 0.45, "nbr_loss": 0.10, "jarak_jalan_m": 80, "luas_klaster_ha": 1.8}
])

hasil = model.predict(alert_baru)
keyakinan = model.predict_proba(alert_baru).max(axis=1)

print("\n=== PREDIKSI ALERT BARU ===")
for nomor, (penyebab, skor) in enumerate(zip(hasil, keyakinan), start=1):
    print(f"Alert {nomor}: {penyebab} (keyakinan model {skor * 100:.1f}%)")

print("\nCatatan: data dan label pada contoh ini merupakan simulasi pembelajaran.")
