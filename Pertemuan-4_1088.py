#List dengan satu tipe data
numA = [1, 2, 3, 4, 5, 6]
print("List dengan satu tipe data:")
for n in range(3):
    print(numA[n])
'''Memanggil semua variabel List'''
print(numA)

# List dengan banyak tipe data
numB = [1, 2, 'Tiga', "Empat", 5.0, 6, "Tujuh"]
print("\nList dengan banyak tipe data:")
for i in range(4):
    print(numB[i])

# Slicing
print("\nSlicing")
'''Mengambil data kedua dengan index'''
print(numA[1])
'''Mengambil data 2 angka pertama'''
print(numA[:2]) #dibaca: dari index 0 sampai sblm index 2
'''Mengambil data 2 angka terakhir'''
print(numA[-2:]) #dibaca: dari index -2 sampai -1 (index 2 terakhir sampai index terakhir)
'''Mengambil data 3 angka dari urutan terakhir dengan lompatan 2 angka'''
print(numA[-1::-2])#dibaca: dari index -1 dengan lompatan 2 angka ke belakang
'''Mengambil semua data dengan lompatan 2 angka dari depan'''
print(numA[::2])
print(numA[1:5:2])#dibaca: dari index 1 sampai sblm index 5 dgn lompatan 2 angka
'''Mengambil dari index ke-3 pertama sampai sblm index ke-5'''
print(numA[3:5])

