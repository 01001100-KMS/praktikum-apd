import os
import sys

# globar variabel
users = {
    "admin": {"password": "admin123", "role": "admin"}
}
characters = {
    1: {"name": "Aegis", "role": "Tank", "level": 5, "power": 80},
    2: {"name": "Lumina", "role": "Mage", "level": 3, "power": 45}
}
next_char_id = max(characters.keys(), default=0) + 1

# function without parameter
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input("\nTekan Enter untuk melanjutkan...")

# function with parameter
def add_user(username, password, role="user"):
    global users
    if username in users:
        return False
    users[username] = {"password": password, "role": role}
    return True


def add_character(name, role_c, level, power):
    global characters, next_char_id
    cid = next_char_id
    characters[cid] = {"name": name, "role": role_c, "level": level, "power": power}
    next_char_id += 1
    return cid

# procedure 2
def procedure_register_user():
    clear_screen()
    print("== REGISTER USER ==")
    while True:
        try:
            username = input("Masukkan username baru: ").strip()
            if username == "":
                print("Username tidak boleh kosong.")
                continue
            if username in users:
                print("Username sudah digunakan.")
                continue
            password = input("Masukkan password: ").strip()
            if password == "":
                print("Password tidak boleh kosong.")
                continue
            add_user(username, password)
            print(f"User '{username}' berhasil terdaftar!")
            pause()
            break
        except Exception as e:
            print("Terjadi kesalahan:", e)
            pause()
            break


def procedure_create_character():
    clear_screen()
    print("== CREATE CHARACTER ==")
    try:
        name = input("Nama karakter: ").strip()
        if name == "":
            print("Nama tidak boleh kosong.")
            pause()
            return
        role_c = input("Peran (role): ").strip()
        lvl = input("Level (>=1): ").strip()
        if not lvl.isdigit() or int(lvl) < 1:
            print("Level tidak valid.")
            pause()
            return
        power = input("Power (0-100): ").strip()
        if not power.isdigit() or not (0 <= int(power) <= 100):
            print("Power tidak valid.")
            pause()
            return
        cid = add_character(name, role_c, int(lvl), int(power))
        print(f"Karakter '{name}' berhasil ditambahkan dengan ID {cid}.")
        pause()
    except Exception as e:
        print("Kesalahan input:", e)
        pause()

# recursif function
def tampil_karakter_rekursif(id_list, idx=0):
    if idx >= len(id_list):
        return
    cid = id_list[idx]
    c = characters[cid]
    bar = "[" + "█" * int((c["power"]/100)*20) + "-" * (20-int((c["power"]/100)*20)) + "]"
    print(f"{cid:<4} | {c['name']:<12} | {c['role']:<10} | {c['level']:<3} | {c['power']:<3} {bar}")
    tampil_karakter_rekursif(id_list, idx + 1)

# parameter function
def boost_power(cid, percent):
    if cid not in characters:
        return False
    c = characters[cid]
    c["power"] += int(c["power"] * (percent / 100))
    if c["power"] > 100:
        c["power"] = 100
    return True

# atmin
def admin_menu(username):
    while True:
        try:
            clear_screen()
            print(f"== MENU ADMIN ({username}) ==")
            print("1. Tambah Karakter")
            print("2. Lihat Semua Karakter")
            print("3. Update Karakter")
            print("4. Hapus Karakter")
            print("5. Register User Baru")
            print("6. Lihat Semua User")
            print("7. Logout")
            print("0. Keluar")
            pilih = input("Pilih menu: ").strip()

            if pilih == "1":
                procedure_create_character()
            elif pilih == "2":
                clear_screen()
                print("== DAFTAR KARAKTER ==")
                if not characters:
                    print("Tidak ada data karakter.")
                else:
                    print(f"{'ID':<4} | {'Nama':<12} | {'Role':<10} | {'Lvl':<3} | {'Power'}")
                    print("-" * 60)
                    tampil_karakter_rekursif(sorted(characters.keys()))
                pause()
            elif pilih == "3":
                cid = input("Masukkan ID karakter: ").strip()
                if not cid.isdigit() or int(cid) not in characters:
                    print("ID tidak valid.")
                    pause()
                    continue
                cid = int(cid)
                c = characters[cid]
                new_name = input(f"Nama baru [{c['name']}]: ").strip()
                new_role = input(f"Role baru [{c['role']}]: ").strip()
                new_level = input(f"Level baru [{c['level']}]: ").strip()
                new_power = input(f"Power baru [{c['power']}]: ").strip()
                if new_name:
                    c["name"] = new_name
                if new_role:
                    c["role"] = new_role
                if new_level.isdigit():
                    c["level"] = int(new_level)
                if new_power.isdigit() and 0 <= int(new_power) <= 100:
                    c["power"] = int(new_power)
                print("Data karakter diperbarui!")
                pause()
            elif pilih == "4":
                cid = input("Masukkan ID karakter: ").strip()
                if not cid.isdigit() or int(cid) not in characters:
                    print("ID tidak valid.")
                    pause()
                    continue
                cid = int(cid)
                konfirmasi = input(f"Yakin ingin hapus {characters[cid]['name']}? (y/n): ").lower()
                if konfirmasi == "y":
                    del characters[cid]
                    print("Karakter dihapus.")
                else:
                    print("Dibatalkan.")
                pause()
            elif pilih == "5":
                procedure_register_user()
            elif pilih == "6":
                clear_screen()
                print("== DAFTAR USER ==")
                for u, info in users.items():
                    print(f"- {u} ({info['role']})")
                pause()
            elif pilih == "7":
                break
            elif pilih == "0":
                print("Sampai jumpa!")
                sys.exit(0)
            else:
                print("Pilihan tidak valid.")
                pause()
        except Exception as e:
            print("Terjadi kesalahan:", e)
            pause()

# new usr
def user_menu(username):
    while True:
        try:
            clear_screen()
            print(f"== MENU USER ({username}) ==")
            print("1. Lihat Semua Karakter")
            print("2. Detail Karakter")
            print("3. Logout")
            print("0. Keluar")
            pilih = input("Pilih menu: ").strip()

            if pilih == "1":
                clear_screen()
                print("== DAFTAR KARAKTER ==")
                if not characters:
                    print("Tidak ada karakter.")
                else:
                    print(f"{'ID':<4} | {'Nama':<12} | {'Role':<10} | {'Lvl':<3} | {'Power'}")
                    print("-" * 60)
                    tampil_karakter_rekursif(sorted(characters.keys()))
                pause()
            elif pilih == "2":
                cid = input("Masukkan ID karakter: ").strip()
                if not cid.isdigit() or int(cid) not in characters:
                    print("ID tidak valid.")
                    pause()
                    continue
                cid = int(cid)
                c = characters[cid]
                print(f"\nID: {cid}")
                print(f"Nama : {c['name']}")
                print(f"Role : {c['role']}")
                print(f"Level: {c['level']}")
                print(f"Power: {c['power']}")
                bar = "[" + "█" * int((c["power"]/100)*30) + "-" * (30-int((c["power"]/100)*30)) + "]"
                print("Visual:", bar)
                pause()
            elif pilih == "3":
                break
            elif pilih == "0":
                print("Sampai jumpa!")
                sys.exit(0)
            else:
                print("Pilihan tidak valid.")
                pause()
        except Exception as e:
            print("Terjadi kesalahan:", e)
            pause()

# main prog
def main():
    while True:
        try:
            clear_screen()
            print("=== SISTEM MANAGEMENT KARAKTER GAME ===")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            menu = input("Pilih menu: ").strip()

            if menu == "1":
                procedure_register_user()
            elif menu == "2":
                clear_screen()
                print("== LOGIN ==")
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                if username in users and users[username]["password"] == password:
                    role = users[username]["role"]
                    print(f"Selamat datang, {username} ({role})!")
                    pause()
                    if role == "admin":
                        admin_menu(username)
                    else:
                        user_menu(username)
                else:
                    print("Username atau password salah.")
                    pause()
            elif menu == "3":
                print("Terima kasih telah menggunakan program ini!")
                sys.exit(0)
            else:
                print("Pilihan tidak valid.")
                pause()
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh user.")
            sys.exit(0)
        except Exception as e:
            print("Terjadi kesalahan:", e)
            pause()


if __name__ == "__main__":
    main()
