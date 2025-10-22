def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung biaya kirim berdasarkan kota, berat, dan asuransi."""
    
    # Tarif dasar untuk setiap kota
    tarif_dasar = {
        "Jakarta": 10000,
        "Bandung": 12000,
        "Surabaya": 15000
    }

    # Jika kota tidak ada dalam daftar tarif
    if kota not in tarif_dasar:
        return "Kota tidak tersedia."

    # Hitung ongkir berdasarkan rumus
    ongkir = tarif_dasar[kota] + 2000 * berat_kg

    # Jika ada asuransi, tambah 3000
    if asuransi == True:
        ongkir = ongkir + 3000

    # Kembalikan hasil
    return ongkir


# Contoh pemanggilan fungsi
print(hitung_ongkir(2, "Jakarta"))          # Tanpa asuransi
print(hitung_ongkir(3, "Surabaya", True))   # Dengan asuransi
print(hitung_ongkir(1, "Yogyakarta"))     # Kota tidak tersedia
