# Mendefinisikan dictionary
mhs = {"1088": "Hafiz Arul",
          "1080": "Iqbal Asidig",
          "1086": "Atenk"}

# Menampilkan dictionary
print(mhs["1088"])

# Menambahkan data di dict.
mhs["1102"] = "Mahardika Putra Ramadhan"
print("- Data baru: ",mhs["1102"])

# Merubah data di dict.
mhs["1080"] = "Iqbal"
print(mhs["1080"])

# Menghapus data di dict.
del mhs["1088"]
print(mhs)

# Menghapus dict. dan semua datanya
del mhs
print(mhs) #menghasilkan error


# Latihan python
print("\nDaftar Platnomor")
platNomor = {"A":"Banten",
             "B":"Jakarta",
             "DK":"Denpasar",
             "BH":"Jambi",
             "BN":"Bangka Belitung"}
print(platNomor)
platNomor["DK"] = "Bali"
print(platNomor)
