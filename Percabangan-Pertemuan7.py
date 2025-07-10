nomor = input("Masukkan input 1/2/3: ")
# Input nomor kendaraan dan asalnya
platnomor = {}
key = input("Masukkan key: ")
val = input("Masukkan value: ")
if nomor == '1':
    platnomor[key] = val
    print(platnomor[key])
elif nomor == '2':
    platnomor[key] = val
    print(platnomor[key])
elif nomor == '3':
    platnomor[key] = val
    print(platnomor[key])
else:
    print("Input salah!")

# Tampilkan semua nomor kendaraan dan asalnya
print(platnomor)
