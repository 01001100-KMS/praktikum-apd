# # # # # # # # def perkenalan():
# # # # # # # #     print('mata kuliah')
# # # # # # # #     print('kalkulus')
# # # # # # # #     input('tekan enter untuk lanjut. . . . .')

# # # # # # # #     perkenalan()
# # # # # # # def perkalian():
# # # # # # #     x = 5 * 3
# # # # # # #     print(x)
# # # # # # #     perkalian()

# # # # # def perkenalan(nama):
# # # # #     print(f'halo {nama} selamat berbelanja')

# # # # # perkenalan('yoga')

# # # # def luasPersegiPanjang(panjang, lebar):
# # # #     luas = panjang * lebar
# # # #     print(f'luas dari persegi panjang adalah {luas}')
# # # #     luasPersegiPanjang(5,3)

# # def luasPersegi(sisi):
# #     luas = sisi * sisi
# #     return luas

# # def volume_persegi(sisi):
# #     volume = luasPersegi(sisi) * sisi
# #     print("Volume Persegi = ", volume)

# # luasPersegi(4)
# # volume_persegi(8)

# def faktorial(n): 
#     # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
#     # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
#     # Memanggil fungsi
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")

# Fungsi untuk menampilkan semua data
# film = []

# def show_data():
#     if len(film) <= 0:
#         print("Belum ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.pop(indeks)
#         print("Film berhasil dihapus!")

# # Fungsi untuk menampilkan menu
# def show_menu():
#     print("\n----------- MENU ----------")
#     print("[1] Show Data")
#     print("[2] Insert Data")
#     print("[3] Edit Data")
#     print("[4] Delete Data")
#     print("[5] Exit")

# # Loop utama
# while True:
#     show_menu()
#     menu = input("PILIH MENU > ")
#     print("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         print("Keluar dari program...")
#         break
#     else:
#         print("Salah pilih!")


# harga = input(input('masukkan harga'))
#     print(harga)

# try:
#     angka = int(input('masukkan angka'))

# try:
#     pass = input('Masukkan Password yang diinginkan:    ')
#     if len(pass) < 8:
#         raise ValueError('Password Minimal harus memiliki 8 character dan harus berupa angka')
# except ValueError as e:
#     print(e)
# else:
#     print(pass)

# try:
#     pas = int(input('Password yang diinginkan : '))
#     if len(pas) < 8:
#         raise ValueError('Password Minimal Memiliki 8 karakter dan wajib ada angka')
# except ValueError as e:
#     print(e)

user_input = input("Masukkan angka: ")

try:
    angka = int(user_input)
    if len(angka) < 8:
        print("Angka kurang dari 8.")
    else:
        print("Angka 8 atau lebih.")
except ValueError:
    print("Input bukan integer!")
