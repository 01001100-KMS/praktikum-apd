print("SELAMAT DATANG")
member = input("Apakah Anda member? (ya/tidak): ").lower() == "ya"

if member:
    user = input("Username: ")
    password = input("Password: ")
    login = True if (user == "nabil" and password == "046") else False
    
    if login:
        print("\nMENU PRODUK")
        print("1. Ayam Fillet - Rp 120.000")
        print("2. Ayam - Rp 80.000")
        print("3. Daging - Rp 135.000")

        pilih = input("Pilih produk (1/2/3): ")
        qty = int(input("Jumlah barang: "))

        if pilih == "1": 
            harga = 120000 * qty
        elif pilih == "2":
            harga = 80000 * qty
        elif pilih == "3":
            harga = 135000 * qty
        else:
            harga = 0

        diskon = int(harga * 0.15)
        total = harga - diskon

        print("\nSTRUK BELANJA MEMBER")
        print(f"Harga sebelum diskon : Rp {harga}")
        print(f"Diskon 15%           : Rp {diskon}")
        print(f"Total bayar          : Rp {total}")
    else:
        print("Login gagal!")
else:
    print("\nMENU PRODUK")
    print("1. Ayam Fillet - Rp 120.000")
    print("2. Ayam - Rp 80.000")
    print("3. Daging - Rp 135.000")

    pilih = input("Pilih produk (1/2/3): ")
    qty = int(input("Jumlah barang: "))

    if pilih == "1":
        harga = 120000 * qty
    elif pilih == "2":
        harga = 80000 * qty
    elif pilih == "3":
        harga = 135000 * qty
    else:
        harga = 0

    print("\nSTRUK BELANJA NON-MEMBER")
    print(f"Total bayar : Rp {harga}")