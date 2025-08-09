try:
    angka = int(input("Masukkan angka: "))
    hasil =  10/angka
    print("hasil 10/",angka,": ",hasil)

except ValueError:
    print(f"Nilai variabel salah!")

except TypeError:
    print(f"Tipe data variabel tidak cocok!")

except Exception:
    print(f"Terjadi kesalahan!")
