import time
import numpy as np
from multiprocessing import Pool, cpu_count

# Sesi 2: Simulasi penyebaran polusi pada sebuah grid
UKURAN_GRID = 300
JUMLAH_ITERASI = 50
KOEF_DIFUSI = 0.1

def buat_grid(ukuran):
    grid = np.zeros((ukuran, ukuran), dtype=float)
    grid[ukuran // 4, ukuran // 4] = 250
    grid[ukuran // 2, ukuran // 2] = 400
    grid[3 * ukuran // 4, 3 * ukuran // 4] = 180
    return grid

def hitung_bagian(data):
    bagian, atas, bawah, alpha = data
    gabungan = np.vstack([atas, bagian, bawah])
    tengah = gabungan[1:-1]
    laplacian = (
        gabungan[:-2] + gabungan[2:]
        + np.roll(tengah, 1, axis=1)
        + np.roll(tengah, -1, axis=1)
        - 4 * tengah
    )
    return tengah + alpha * laplacian

def proses_paralel(grid, iterasi, alpha, pekerja):
    hasil = grid.copy()
    ukuran = hasil.shape[0]
    batas = np.linspace(0, ukuran, pekerja + 1, dtype=int)

    with Pool(processes=pekerja) as pool:
        for _ in range(iterasi):
            tugas = []
            for i in range(pekerja):
                awal, akhir = batas[i], batas[i + 1]
                atas = hasil[awal - 1:awal] if awal > 0 else hasil[0:1]
                bawah = hasil[akhir:akhir + 1] if akhir < ukuran else hasil[-1:]
                tugas.append((hasil[awal:akhir], atas, bawah, alpha))
            hasil = np.vstack(pool.map(hitung_bagian, tugas))
    return hasil

def proses_sekuensial(grid, iterasi, alpha):
    hasil = grid.copy()
    for _ in range(iterasi):
        laplacian = (
            np.roll(hasil, 1, axis=0) + np.roll(hasil, -1, axis=0)
            + np.roll(hasil, 1, axis=1) + np.roll(hasil, -1, axis=1)
            - 4 * hasil
        )
        hasil = hasil + alpha * laplacian
    return hasil

if __name__ == "__main__":
    grid_awal = buat_grid(UKURAN_GRID)
    jumlah_pekerja = max(1, min(4, cpu_count()))

    mulai = time.perf_counter()
    hasil_serial = proses_sekuensial(grid_awal, JUMLAH_ITERASI, KOEF_DIFUSI)
    waktu_serial = time.perf_counter() - mulai

    mulai = time.perf_counter()
    hasil_paralel = proses_paralel(
        grid_awal, JUMLAH_ITERASI, KOEF_DIFUSI, jumlah_pekerja
    )
    waktu_paralel = time.perf_counter() - mulai

    print("=== SIMULASI HPC POLUSI PM2.5 ===")
    print(f"Ukuran grid: {UKURAN_GRID} x {UKURAN_GRID}")
    print(f"Iterasi: {JUMLAH_ITERASI}")
    print(f"Waktu sekuensial: {waktu_serial:.3f} detik")
    print(f"Waktu paralel ({jumlah_pekerja} pekerja): {waktu_paralel:.3f} detik")
    if waktu_paralel > 0:
        print(f"Perbandingan waktu: {waktu_serial / waktu_paralel:.2f}x")
    print(f"Rata-rata hasil grid: {np.mean(hasil_paralel):.2f}")
    print(f"Nilai maksimum: {np.max(hasil_paralel):.2f}")
