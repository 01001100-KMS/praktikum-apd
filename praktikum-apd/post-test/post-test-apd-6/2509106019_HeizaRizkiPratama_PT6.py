import os
import sys

users = {
    "admin": {"password": "admin123", "role": "admin"}
}

characters = {
    1: {"name": "Aegis", "role": "Tank", "level": 5, "power": 80},
    2: {"name": "Lumina", "role": "Mage", "level": 3, "power": 45}
}

# main prog

while True:
    # Clear layar
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("=== MANAGEMENT DATA CHARACTER GAME ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    menu = input("Choose option: ").strip()

    # regist pros
    if menu == "1":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("== REGISTER USER ==")
        while True:
            username = input("Enter new username: ").strip()
            if username == "":
                print("Username cannot be empty.")
                continue
            if username in users:
                print("Username already taken.")
                continue
            password = input("Enter password: ").strip()
            if password == "":
                print("Password cannot be empty.")
                continue
            users[username] = {"password": password, "role": "user"}
            print(f"User '{username}' registered successfully!")
            input("\nPress Enter to continue...")
            break

    # login
    elif menu == "2":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("== LOGIN ==")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Welcome, {username} ({role})")
            input("\nPress Enter to continue...")

            # if admin 
            if role == "admin":
                while True:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print(f"== ADMIN MENU ({username}) ==")
                    print("1. Create Character")
                    print("2. Read Characters")
                    print("3. Update Character")
                    print("4. Delete Character")
                    print("5. Register User")
                    print("6. List Users")
                    print("7. Logout")
                    print("0. Exit")
                    admin_choice = input("Choose: ").strip()

                    # create
                    if admin_choice == "1":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("== CREATE CHARACTER ==")
                        name = input("Name: ").strip()
                        if name == "":
                            print("Name cannot be empty.")
                            input("\nPress Enter to continue...")
                            continue
                        role_c = input("Role: ").strip()
                        lvl = input("Level (>=1): ").strip()
                        if not lvl.isdigit() or int(lvl) < 1:
                            print("Invalid level.")
                            input("\nPress Enter to continue...")
                            continue
                        power = input("Power (0-100): ").strip()
                        if not power.isdigit() or not (0 <= int(power) <= 100):
                            print("Invalid power.")
                            input("\nPress Enter to continue...")
                            continue
                        new_id = max(characters.keys(), default=0) + 1
                        characters[new_id] = {"name": name, "role": role_c, "level": int(lvl), "power": int(power)}
                        print(f"Character '{name}' added.")
                        input("\nPress Enter to continue...")

                    # read
                    elif admin_choice == "2":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("== CHARACTERS ==")
                        if len(characters) == 0:
                            print("No data.")
                        else:
                            print(f"{'ID':<4} | {'Name':<12} | {'Role':<8} | {'Lvl':<3} | {'Power':<8}")
                            print("-"*45)
                            for cid, c in characters.items():
                                bar = "[" + "█" * int((c["power"]/100)*20) + "-" * (20-int((c["power"]/100)*20)) + "]"
                                print(f"{cid:<4} | {c['name']:<12} | {c['role']:<8} | {c['level']:<3} | {c['power']:<8} {bar}")
                        input("\nPress Enter to continue...")

                    # upt
                    elif admin_choice == "3":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("== UPDATE CHARACTER ==")
                        cid = input("Enter ID: ").strip()
                        if not cid.isdigit() or int(cid) not in characters:
                            print("Invalid ID.")
                            input("\nPress Enter to continue...")
                            continue
                        cid = int(cid)
                        c = characters[cid]
                        new_name = input(f"Name [{c['name']}]: ").strip()
                        new_role = input(f"Role [{c['role']}]: ").strip()
                        new_level = input(f"Level [{c['level']}]: ").strip()
                        new_power = input(f"Power [{c['power']}]: ").strip()
                        if new_name != "": c["name"] = new_name
                        if new_role != "": c["role"] = new_role
                        if new_level.isdigit(): c["level"] = int(new_level)
                        if new_power.isdigit() and 0 <= int(new_power) <= 100: c["power"] = int(new_power)
                        print("Updated successfully.")
                        input("\nPress Enter to continue...")

                    # del
                    elif admin_choice == "4":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("== DELETE CHARACTER ==")
                        cid = input("Enter ID: ").strip()
                        if not cid.isdigit() or int(cid) not in characters:
                            print("Invalid ID.")
                            input("\nPress Enter to continue...")
                            continue
                        cid = int(cid)
                        confirm = input(f"Delete {characters[cid]['name']}? (y/n): ").lower()
                        if confirm == "y":
                            del characters[cid]
                            print("Deleted.")
                        else:
                            print("Aborted.")
                        input("\nPress Enter to continue...")

                    # reg usr (admin)
                    elif admin_choice == "5":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("== REGISTER USER ==")
                        while True:
                            new_user = input("Enter new username: ").strip()
                            if new_user == "":
                                print("Username cannot be empty.")
                                continue
                            if new_user in users:
                                print("Username already taken.")
                                continue
                            new_pass = input("Enter password: ").strip()
                            if new_pass == "":
                                print("Password cannot be empty.")
                                continue
                            users[new_user] = {"password": new_pass, "role": "user"}
                            print(f"User '{new_user}' registered successfully!")
                            input("\nPress Enter to continue...")
                            break

                    # users list
                    elif admin_choice == "6":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("== USERS ==")
                        for u, info in users.items():
                            print(f"- {u} ({info['role']})")
                        input("\nPress Enter to continue...")

                    elif admin_choice == "7":
                        break

                    elif admin_choice == "0":
                        sys.exit(0)

                    else:
                        print("Invalid choice.")
                        input("\nPress Enter to continue...")

            # user 
            else:
                while True:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print(f"== USER MENU ({username}) ==")
                    print("1. Read Characters")
                    print("2. View Detail")
                    print("3. Logout")
                    print("0. Exit")
                    choice = input("Choose: ").strip()

                    if choice == "1":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("== CHARACTERS ==")
                        if len(characters) == 0:
                            print("No data.")
                        else:
                            print(f"{'ID':<4} | {'Name':<12} | {'Role':<8} | {'Lvl':<3} | {'Power':<8}")
                            print("-"*45)
                            for cid, c in characters.items():
                                bar = "[" + "█" * int((c["power"]/100)*20) + "-" * (20-int((c["power"]/100)*20)) + "]"
                                print(f"{cid:<4} | {c['name']:<12} | {c['role']:<8} | {c['level']:<3} | {c['power']:<8} {bar}")
                        input("\nPress Enter to continue...")

                    elif choice == "2":
                        cid = input("Enter ID: ").strip()
                        if not cid.isdigit() or int(cid) not in characters:
                            print("Invalid ID.")
                            input("\nPress Enter to continue...")
                            continue
                        cid = int(cid)
                        c = characters[cid]
                        print(f"ID: {cid}")
                        print(f"Name: {c['name']}")
                        print(f"Role: {c['role']}")
                        print(f"Level: {c['level']}")
                        print(f"Power: {c['power']}")
                        bar = "[" + "█" * int((c["power"]/100)*30) + "-" * (30-int((c["power"]/100)*30)) + "]"
                        print("Visual:", bar)
                        input("\nPress Enter to continue...")

                    elif choice == "3":
                        break

                    elif choice == "0":
                        sys.exit(0)

                    else:
                        print("Invalid choice.")
                        input("\nPress Enter to continue...")

        else:
            print("Invalid credentials.")
            input("\nPress Enter to continue...")

    elif menu == "3":
        print("Goodbye!")
        sys.exit(0)

    else:
        print("Invalid option.")
        input("\nPress Enter to continue...")
