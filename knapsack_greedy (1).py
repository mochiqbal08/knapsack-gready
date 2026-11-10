
barang = [
    {"nama": "A", "berat": 10, "nilai": 60},
    {"nama": "B", "berat": 5, "nilai": 50},
    {"nama": "C", "berat": 8, "nilai": 64},
    {"nama": "D", "berat": 4, "nilai": 40}
]

kapasitas = 20

barang.sort(
    key=lambda item: item["nilai"] / item["berat"],
    reverse=True
)

total_nilai = 0

print("Barang yang dipilih:")

for item in barang:
    if kapasitas <= 0:
        break

    # Ambil seluruh barang jika masih muat,
    # jika tidak, ambil sebagian sesuai kapasitas tersisa.
    if item["berat"] <= kapasitas:
        berat_diambil = item["berat"]
    else:
        berat_diambil = kapasitas

    nilai_didapat = (berat_diambil / item["berat"]) * item["nilai"]
    total_nilai += nilai_didapat
    kapasitas -= berat_diambil

    print(
        item["nama"],
        "- berat:", berat_diambil,
        "kg, nilai:", round(nilai_didapat, 2)
    )

print("Total nilai maksimum:", round(total_nilai, 2))
