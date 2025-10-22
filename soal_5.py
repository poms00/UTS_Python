import os
import csv
import json
import logging

# Atur logging sederhana
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def jadwal_presensi():
    try:
        # 1) Buat folder data (jika belum ada)
        if not os.path.exists("data"):
            os.mkdir("data")
            logging.info("Folder 'data' berhasil dibuat.")
        else:
            logging.info("Folder 'data' sudah ada, lanjut...")

        # 2) Tulis file CSV
        with open("data/presensi.csv", "w", newline="", encoding="utf-8") as file_csv:
            tulis = csv.writer(file_csv)
            tulis.writerow(["nim", "nama", "hadir_uts"])
            tulis.writerow(["2310001", "Ali", 1])
            tulis.writerow(["2310002", "Budi", 0])
            tulis.writerow(["2310003", "Citra", 1])
        logging.info("Data presensi berhasil ditulis ke CSV.")

        # 3) Baca kembali CSV dan hitung ringkasan
        with open("data/presensi.csv", "r", encoding="utf-8") as file_csv:
            baca = csv.DictReader(file_csv)
            data = list(baca)

        total = len(data)
        hadir = sum(int(m["hadir_uts"]) for m in data)
        persentase = (hadir / total) * 100

        ringkasan = {
            "total_mahasiswa": total,
            "jumlah_hadir": hadir,
            "persentase_hadir": f"{persentase:.2f}%"
        }

        # Simpan ke JSON
        with open("data/ringkasan.json", "w", encoding="utf-8") as file_json:
            json.dump(ringkasan, file_json, indent=4)
        logging.info("Ringkasan berhasil disimpan ke JSON.")

        print("✅ Proses selesai, data berhasil diproses!")
        print(ringkasan)

    except Exception as e:
        logging.error("Terjadi kesalahan saat memproses data.")
        print("❌ Error:", e)

# Jalankan program
jadwal_presensi()
