def register_user(users):
    print("== REGISTER USER ==")
    while True:
        username = input("Enter new username: ").strip()
        if username == "":
            print("Username cannot be empty.")
            continue
        # Cek apakah sudah ada
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
