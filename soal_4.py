def jadwal_hari(hari):
    # Data jadwal disimpan dalam list of dict
    jadwal = [
        {"hari": "Senin", "mata_kuliah": "Algoritma", "jam": "08.00-10.00"},
        {"hari": "Selasa", "mata_kuliah": "Basis Data", "jam": "09.00-11.00"},
        {"hari": "Rabu", "mata_kuliah": "Pemrograman Web", "jam": "10.00-12.00"},
        {"hari": "Kamis", "mata_kuliah": "Jaringan Komputer", "jam": "08.00-10.00"},
        {"hari": "Jumat", "mata_kuliah": "Kecerdasan Buatan", "jam": "09.00-11.00"}
    ]

    # Mencari jadwal sesuai hari dengan mengecek satu per satu isi list
    for data in jadwal:
        if data["hari"].lower() == hari.lower():
            return f"Jadwal hari {hari}: {data['mata_kuliah']} ({data['jam']})"
    return f"Tidak ada jadwal pada hari {hari}"

# Contoh penggunaan
print(jadwal_hari("sabtu"))
