import os
import sys

def register_user(users):
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
        exists = any(u[0] == username for u in users)
        if exists:
            print("Username already taken.")
            continue
        password = input("Enter password: ").strip()
        if password == "":
            print("Password cannot be empty.")
            continue
        users.append([username, password, "user"])
        print(f"User '{username}' registered successfully!")
        input("\nPress Enter to continue...")
        break
    return users

users = [["admin", "admin123", "admin"]]
characters = [
    [1, "Aegis", "Tank", 5, 80],
    [2, "Lumina", "Mage", 3, 45],
]

while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("=== MANAGEMENT DATA CHARACTER GAME ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose option: ").strip()

    if choice == "1":
        users = register_user(users)
        continue

    elif choice == "2":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("== LOGIN ==")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        logged_user = None
        for u in users:
            if u[0] == username and u[1] == password:
                logged_user = u
                break
        if logged_user is None:
            print("Invalid credentials.")
            input("\nPress Enter to continue...")
            continue
        print(f"Welcome, {logged_user[0]} ({logged_user[2]})")
        input("\nPress Enter to continue...")

        if logged_user[2] == "admin":
            while True:
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                print(f"== ADMIN MENU ({logged_user[0]}) ==")
                print("1. Create Character")
                print("2. Read Characters")
                print("3. Update Character")
                print("4. Delete Character")
                print("5. Register User")
                print("6. List Users")
                print("7. Logout")
                print("0. Exit")
                ch = input("Choose: ").strip()

                if ch == "1":
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
                    role = input("Role: ").strip()
                    level_str = input("Level (>=1): ").strip()
                    if not level_str.isdigit():
                        print("Level must be number.")
                        input("\nPress Enter to continue...")
                        continue
                    power_str = input("Power (0-100): ").strip()
                    if not power_str.isdigit():
                        print("Power must be number.")
                        input("\nPress Enter to continue...")
                        continue
                    power = int(power_str)
                    if power < 0 or power > 100:
                        print("Power out of range.")
                        input("\nPress Enter to continue...")
                        continue
                    new_id = max([c[0] for c in characters], default=0) + 1
                    characters.append([new_id, name, role, int(level_str), power])
                    print(f"Character '{name}' added.")
                    input("\nPress Enter to continue...")

                elif ch == "2":
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
                        for c in characters:
                            bar = "[" + "█" * int((c[4]/100)*20) + "-" * (20-int((c[4]/100)*20)) + "]"
                            print(f"{c[0]:<4} | {c[1]:<12} | {c[2]:<8} | {c[3]:<3} | {c[4]:<8} {bar}")
                    input("\nPress Enter to continue...")

                elif ch == "3":
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("== UPDATE CHARACTER ==")
                    id_str = input("Enter ID: ").strip()
                    if not id_str.isdigit():
                        print("Invalid ID.")
                        input("\nPress Enter to continue...")
                        continue
                    id_val = int(id_str)
                    target = next((c for c in characters if c[0] == id_val), None)
                    if target is None:
                        print("Not found.")
                        input("\nPress Enter to continue...")
                        continue
                    new_name = input(f"Name [{target[1]}]: ").strip()
                    new_role = input(f"Role [{target[2]}]: ").strip()
                    new_level = input(f"Level [{target[3]}]: ").strip()
                    new_power = input(f"Power [{target[4]}]: ").strip()
                    if new_name != "": target[1] = new_name
                    if new_role != "": target[2] = new_role
                    if new_level.isdigit(): target[3] = int(new_level)
                    if new_power.isdigit():
                        p = int(new_power)
                        if 0 <= p <= 100: target[4] = p
                    print("Updated.")
                    input("\nPress Enter to continue...")

                elif ch == "4":
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("== DELETE CHARACTER ==")
                    id_str = input("Enter ID: ").strip()
                    if not id_str.isdigit():
                        print("Invalid ID.")
                        input("\nPress Enter to continue...")
                        continue
                    id_val = int(id_str)
                    idx = next((i for i, c in enumerate(characters) if c[0] == id_val), -1)
                    if idx == -1:
                        print("Not found.")
                    else:
                        confirm = input(f"Delete {characters[idx][1]}? (y/n): ").lower()
                        if confirm == "y":
                            characters.pop(idx)
                            print("Deleted.")
                        else:
                            print("Aborted.")
                    input("\nPress Enter to continue...")

                elif ch == "5":
                    users = register_user(users)

                elif ch == "6":
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("== USERS ==")
                    for u in users:
                        print(f"- {u[0]} ({u[2]})")
                    input("\nPress Enter to continue...")

                elif ch == "7":
                    break

                elif ch == "0":
                    sys.exit(0)

                else:
                    print("Invalid.")
                    input("\nPress Enter to continue...")

        else:
            while True:
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                print(f"== USER MENU ({logged_user[0]}) ==")
                print("1. Read Characters")
                print("2. View Detail")
                print("3. Logout")
                print("0. Exit")
                ch = input("Choose: ").strip()

                if ch == "1":
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")
                    if len(characters) == 0:
                        print("No characters.")
                    else:
                        print(f"{'ID':<4} | {'Name':<12} | {'Role':<8} | {'Lvl':<3} | {'Power':<8}")
                        print("-"*45)
                        for c in characters:
                            bar = "[" + "█" * int((c[4]/100)*20) + "-" * (20-int((c[4]/100)*20)) + "]"
                            print(f"{c[0]:<4} | {c[1]:<12} | {c[2]:<8} | {c[3]:<3} | {c[4]:<8} {bar}")
                    input("\nPress Enter to continue...")

                elif ch == "2":
                    id_str = input("Enter ID: ").strip()
                    if not id_str.isdigit():
                        print("Invalid ID.")
                        input("\nPress Enter to continue...")
                        continue
                    id_val = int(id_str)
                    found = next((c for c in characters if c[0] == id_val), None)
                    if found is None:
                        print("Not found.")
                    else:
                        print(f"ID: {found[0]}")
                        print(f"Name: {found[1]}")
                        print(f"Role: {found[2]}")
                        print(f"Level: {found[3]}")
                        print(f"Power: {found[4]}")
                        bar = "[" + "█" * int((found[4]/100)*30) + "-" * (30-int((found[4]/100)*30)) + "]"
                        print("Visual:", bar)
                    input("\nPress Enter to continue...")

                elif ch == "3":
                    break

                elif ch == "0":
                    sys.exit(0)

                else:
                    print("Invalid.")
                    input("\nPress Enter to continue...")

    elif choice == "3":
        print("Goodbye!")
        sys.exit(0)

    else:
        print("Invalid option.")
        input("\nPress Enter to continue...")
