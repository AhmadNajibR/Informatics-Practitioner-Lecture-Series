import math
import json

# Sesi 3: Analisis aset dan jarak dari zona bahaya
aset = [
    {"id": "AST-001", "nama": "Jembatan Muara", "tipe": "Jembatan",
     "lat": -3.785, "lon": 102.260, "umur": 14, "retak": 5.2},
    {"id": "AST-002", "nama": "Gorong-gorong Sentral", "tipe": "Drainase",
     "lat": -3.790, "lon": 102.265, "umur": 4, "retak": 0.8},
    {"id": "AST-003", "nama": "Tiang Fiber Optik A1", "tipe": "Utilitas",
     "lat": -3.782, "lon": 102.258, "umur": 9, "retak": 3.1},
    {"id": "AST-004", "nama": "Pipa Distribusi Utama", "tipe": "Air Bersih",
     "lat": -3.801, "lon": 102.272, "umur": 22, "retak": 8.7},
    {"id": "AST-005", "nama": "Lampu Jalan Protokol", "tipe": "Penerangan",
     "lat": -3.788, "lon": 102.261, "umur": 2, "retak": 0.0},
    {"id": "AST-006", "nama": "Tanggul Penahan Banjir", "tipe": "Drainase",
     "lat": -3.805, "lon": 102.278, "umur": 18, "retak": 6.5}
]

zona = {"lat": -3.800, "lon": 102.270, "radius_m": 800}

def jarak_meter(lat1, lon1, lat2, lon2):
    radius_bumi = 6_371_000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lam = math.radians(lon2 - lon1)
    a = (math.sin(delta_phi / 2) ** 2
         + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lam / 2) ** 2)
    return radius_bumi * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

aset_prioritas = []

for item in aset:
    jarak = jarak_meter(item["lat"], item["lon"], zona["lat"], zona["lon"])
    item["jarak_zona_m"] = round(jarak, 2)
    dekat_zona = jarak <= zona["radius_m"]
    skor = item["umur"] * 0.4 + item["retak"] * 0.6

    if skor > 7 or dekat_zona:
        item["status"] = "PERLU INSPEKSI"
        aset_prioritas.append(item)
    elif skor > 4:
        item["status"] = "PEMELIHARAAN TERJADWAL"
    else:
        item["status"] = "KONDISI BAIK"

print("=== LAPORAN MANAJEMEN ASET GIS ===")
print(f"Jumlah aset: {len(aset)}")
print(f"Aset prioritas inspeksi: {len(aset_prioritas)}")
for item in aset:
    print(f"{item['id']} | {item['nama']} | "
          f"{item['jarak_zona_m']} m | {item['status']}")

geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [item["lon"], item["lat"]]
            },
            "properties": {
                "id": item["id"],
                "nama": item["nama"],
                "tipe": item["tipe"],
                "status": item["status"]
            }
        } for item in aset
    ]
}

with open("aset_gis.geojson", "w", encoding="utf-8") as file:
    json.dump(geojson, file, indent=2, ensure_ascii=False)

print("Data spasial disimpan ke aset_gis.geojson")
