#Input
nama = input("Masukkan nama Anda : ") #default nya input() adalah str
print(nama)

ipk = float(input("Masukkan IPK Anda : "))
print(ipk)

#Menyambungkan variabel nama dan ipk
sambungkan = str("{nama} memiliki IPK {ipk}")
print(sambungkan)
print("Sama aja kayak gini :")
print(nama, "memiliki IPK", ipk)

#Operator, Percabangan, dan Perulangan
sks = int(input("\nMasukkan jumlah SKS : "))
spp_var = 50000
hitung = sks *spp_var
print(f"\n{nama} mamiliki ipk {ipk}, \nHarus membayar spp sebesar Rp. {hitung}")

print(hitung >= spp_var)
if hitung >= spp_var :
    i = 0
    for i in range(10):
        print(i, "Jumlah SKS valid")
        i = i+1
else :
    print("\nJumlah SKS tidak valid")
