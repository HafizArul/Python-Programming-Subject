#Input Identitas Diri Anda
print("Isikan identitas diri Anda")
'''Deklarasi Variabel'''
nama = input("- Masukkan nama : ")
nim = input("- Masukkan NIM : ")
jwbn_benar = int(input("- Masukkan jawaban yang benar : "))
matkul = input("- Masukkan mata kuliah : ")
nilai = jwbn_benar * 10
'''Hasil'''
if jwbn_benar <= 10:
    print("\nHasil :")
    print(f"Mahasiswa bernama {nama} dengan NIM {nim} mendapatkan nilai {nilai} dari mata kuliah {matkul}")
else:
    print("Input jawaban benar tidak valid!")
