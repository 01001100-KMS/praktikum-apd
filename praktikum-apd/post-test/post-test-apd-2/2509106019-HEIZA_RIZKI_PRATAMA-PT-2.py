nama = input("Masukkan Nama Pasien: ")
tinggi = float(input("Masukkan Tinggi Badan (cm): "))
beratBadan = float(input("Masukkan Berat Badan (kg): "))

beratIdeal = (tinggi - 100)
isKelebihan = beratBadan > beratIdeal

statusList = ["Ideal", "Big Chungus"]
status = statusList[int(isKelebihan)]

def row_formatting(label, value):
    return f"| {label:<18}: {value:<57}|"

print("-" * 80)
print(f"|{'HASIL CEK BERAT BADAN':^78}|")
print("-" * 80)
print(row_formatting("Nama Pasien", nama))
print(row_formatting("Tinggi Badan", f"{tinggi:.0f} cm"))
print(row_formatting("Berat Badan", f"{beratBadan:.0f} kg"))
print(row_formatting("Berat Ideal", f"{beratIdeal:.0f} kg"))
print(row_formatting("Status", status))
print("-" * 80)

# Ps: saya di suruh kerja paksa padahal belum jam-1 T T