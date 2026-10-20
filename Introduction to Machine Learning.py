import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Sesi 4: Klasifikasi kelayakan pinjaman
np.random.seed(42)
jumlah_data = 400

df = pd.DataFrame({
    "pendapatan": np.random.uniform(3, 35, jumlah_data),
    "pinjaman": np.random.uniform(10, 150, jumlah_data),
    "skor_kredit": np.random.randint(300, 850, jumlah_data),
    "usia": np.random.randint(21, 60, jumlah_data),
    "rasio_utang": np.random.uniform(0.1, 0.7, jumlah_data)
})

skor = (
    (df["skor_kredit"] >= 600).astype(int) * 0.4
    + (df["pendapatan"] >= 7).astype(int) * 0.3
    + (df["rasio_utang"] <= 0.45).astype(int) * 0.3
)
df["status"] = (skor >= 0.6).astype(int)

kolom_fitur = ["pendapatan", "pinjaman", "skor_kredit", "usia", "rasio_utang"]
X, y = df[kolom_fitur], df["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=100, max_depth=6, random_state=42
)
model.fit(X_train, y_train)
prediksi = model.predict(X_test)

print("=== KLASIFIKASI PERSETUJUAN PINJAMAN ===")
print(f"Jumlah data: {len(df)}")
print(f"Data latih: {len(X_train)}")
print(f"Data uji: {len(X_test)}")
print("\nConfusion matrix:")
print(confusion_matrix(y_test, prediksi))
print("\nLaporan evaluasi:")
print(classification_report(
    y_test, prediksi,
    labels=[0, 1],
    target_names=["Ditolak", "Disetujui"],
    zero_division=0
))

nasabah_baru = pd.DataFrame([
    [12.5, 40, 720, 29, 0.25],
    [4.0, 80, 480, 23, 0.60]
], columns=kolom_fitur)

hasil = model.predict(nasabah_baru)
probabilitas = model.predict_proba(nasabah_baru)

for i, status in enumerate(hasil):
    label = "DISETUJUI" if status == 1 else "DITOLAK"
    print(f"Nasabah {i + 1}: {label} "
          f"(probabilitas disetujui {probabilitas[i][1] * 100:.1f}%)")
