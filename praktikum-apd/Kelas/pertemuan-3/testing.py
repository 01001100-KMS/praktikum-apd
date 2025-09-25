# nilai = 70

# if nilai >= 75:
#     print("Nilai A")
# elif nilai > 65:
#     print("Nilai C")
# else:
#     print("Nilai B")

# suhu = 35

# if suhu >= 35:
#     print("Panas")
# if suhu >= 30:
#     print("Sauna")
# if suhu >= 20:
#     print("Normal")
# else:
#     print("Dingin")

# umur = int(input("Masukkan umur Anda: "))
# # misalnya, umur = 16
# # Percabangan
# if umur < 13:
# kategori = "Anak-anak"
# elif umur < 18:
# kategori = "Remaja"
# elif umur < 60:
# kategori = "Dewasa"
# else:
# kategori = "Lansia"
# # Menampilkan umur dan kategori
# print("Umur:", umur, "Kategori:", kategori)

# # Bentuk awal
# nilai = 70
# if nilai = 60:
# status = "Lulus"
# else:
# status = "Tidak Lulus"
# print(status)
# # output
# Lulus
# # Menggunakan Ternary Operator
# nilai = 70
# status = "Lulus" if nilai = 60 else "Tidak Lulus"
# print(status)
# # output
# Lulus

# tb = 157
#  if tb >= 145
#     print("Dizinkan")
# else
#     print("Tidak Dizinkan")

print("Kalkulator Bangun Ruang")
print("1. Kubus")
print("2. Balok")
print("3. Lingkaran")
pilih = int(input("Pilih bangun ruang (Angka): "))
if pilih == 1:
    sisi = float(input("Masukkan sisi (cm): "))
    volume = sisi * sisi * sisi
    luas = 6 * sisi * sisi
    print(f"Volume Kubus: {volume} cm^3")
    print(f"Luas Permukaan Kubus: {luas} cm^2")

elif pilih == 2:
    panjang = float(input("Masukkan panjang (cm): "))
    lebar = float(input("Masukkan lebar (cm): "))
    tinggi = float(input("Masukkan tinggi (cm): "))
    volume = panjang * lebar * tinggi
    luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    keliling = 4 * (panjang + lebar + tinggi)
    print(f"Volume Balok: {volume} cm^3")
    print(f"Luas Permukaan Balok: {luas} cm^2")
    print(f"Keliling Balok: {keliling} cm")

elif pilih == 3:
    jari_jari = float(input("Masukkan jari-jari (cm): "))
    phi = 3.14
    volume = (4/3) * phi * jari_jari**3
    luas = 4 * phi * jari_jari**2
    print(f"Volume Lingkaran: {volume} cm^3")
    print(f"Luas Permukaan Lingkaran: {luas} cm^2")

else:
    print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")