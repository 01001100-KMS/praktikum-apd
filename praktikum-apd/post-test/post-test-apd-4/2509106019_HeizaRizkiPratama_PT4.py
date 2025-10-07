import os

os.system('cls' if os.name == 'nt' else 'clear')
print("=== TOKO AYAM DUGONG ===")

ulang = "y"
while ulang == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TOKO AYAM DUGONG ===")

    member_status = input("Apakah Anda member? (y/n): ").lower().strip()

    if member_status == "y":
        attempts = 3
        is_member = False

        while attempts > 0:
            user = input("Username: ").strip()
            password = input("Password: ").strip()

            if user == "" or password == "":
                print("Username dan Password tidak boleh kosong\n")
            elif user == "nabil" and password == "046":
                print("Login berhasil\n")
                is_member = True
                break
            else:
                attempts -= 1
                print(f"Login gagal, sisa percobaan: {attempts}\n")

        if not is_member:
            print("Gagal login 3 kali. Non-member\n")
    else:
        print("\nNon-Member\n")
        is_member = False

    keranjang = ""
    total_belanja = 0

    while True:
        print("\n=== MENU PRODUK ===")
        print("1. Ayam Fillet - Rp 120.000")
        print("2. Ayam        - Rp 80.000")
        print("3. Daging      - Rp 135.000")
        print("4. Checkout")

        pilih = input("Pilih menu (1/2/3/4): ").strip()

        if pilih == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== STRUK BELANJA ===")
            print(keranjang)
            print("----------------------")
            print(f"Total Harga Sebelum Diskon : Rp {total_belanja}")

            if is_member:
                diskon = int(total_belanja * 0.15)
                total = total_belanja - diskon
                print(f"Diskon 15%                 : Rp {diskon}")
                print(f"Total Bayar               : Rp {total}")
                print("----------------------")
                print("Terima kasih telah berbelanja sebagai Member\n")
            else:
                print(f"Total Bayar : Rp {total_belanja}")
                print("----------------------")
                print("Terima kasih telah berbelanja\n")
            break

        elif pilih in ["1", "2", "3"]:
            qty = input("Jumlah barang: ").strip()
            if qty == "" or not qty.isdigit():
                print("Input jumlah harus berupa angka\n")
                continue

            qty = int(qty)
            if pilih == "1":
                nama_produk = "Ayam Fillet"
                harga = 120000
            elif pilih == "2":
                nama_produk = "Ayam"
                harga = 80000
            else:
                nama_produk = "Daging"
                harga = 135000

            subtotal = harga * qty
            total_belanja += subtotal
            keranjang += f"{nama_produk} x{qty} = Rp {subtotal}\n"

            print(f"{nama_produk} berhasil ditambahkan ke keranjang")
            print(f"Total sementara: Rp {total_belanja}\n")

        else:
            print("Ulang bang, salah itu\n")

    ulang = input("Apakah ingin melakukan transaksi baru? (y/n): ").lower().strip()

os.system('cls' if os.name == 'nt' else 'clear')
print("\nTerima kasih telah berbelanja di Toko Ayam Dugong\n")