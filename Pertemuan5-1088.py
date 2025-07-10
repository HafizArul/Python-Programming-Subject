buah = ['Tomat', 'Ceri', 'Durian', 'Jeruk']

# Menampilkan dengan semua item
print("- Menampilkan dengan semua item")
print(buah)

# Menampilkan dengan index
print("\n- Menampilkan dengan index")
print(buah[-3])
print(buah[2])

# Mengubah nilai dari sebuah List
print("\n- Mengubah nilai dari sebuah List")
buah[0:3] = 'Pisang', 'Anggur', 'Mangga'
print(buah)

# Menambah 1 nilai dari sebuah list di belakang
print("\n- Menambah 1 nilai dari sebuah list di belakang")
buah.append('Pir')
print(buah)
'''
# Menambah lebih dari 1 nilai dari sebuah list di belakang
print("\n- Menambah lebih dari 1 nilai dari sebuah list di belakang")
buah.append(['Apel', 'Buah Naga'])
print(buah)
'''
# Menambah 1 nilai dari sebuah list di index manapun
print("\n- Menambah 1 nilai dari sebuah list di index manapun")
buah.insert(2, 'Semangka') # dibaca: masukkan Semangka di index kedua dr depan
print(buah)

# Menambah item baru 1 atau lebih dengan "[]" tanpa membuat array baru di dalamnya
print("\n- Menambah item baru 1 atau lebih dengan '[]' tanpa membuat array baru di dalamnya")
buah.extend(['Melon', 'Lemon'])
print(buah)
del buah[-1]
print(buah)

# Mengurutkan data
print("\n- Mengurutkan data")
buah.sort()
for elemen in buah:
    print(elemen)

# TUPLE: Sama seperti List tp tidak bisa diubah, ditambah, dihapus
print("\nMembuat Tuple")
tuple_buah = ('Semangka', 'Pepaya', 'Buah naga')
print(tuple_buah)

# Menampilkan salah satu data tuple
print(tuple_buah[2])

# SET: Sama seperti List tp tidak bisa menyimpan data yang sama
print("\nMembuat Set")
buah.append('Jeruk')
print(buah)
set_buah = set(buah)
print(set_buah)
