sisi_pertama = int(input("Masukkan sisi pertama :"))
sisi_kedua = int (input("Masukkan sisi kedua: "))
sisi_ketiga = int(input("Masukkan sisi ketiga : "))

if sisi_pertama == sisi_kedua or sisi_kedua == sisi_ketiga or sisi_ketiga == sisi_pertama:
    print ("Segitiga sama kaki ")
elif sisi_pertama == sisi_kedua == sisi_ketiga:
    print ("Segitiga sama sisi")
elif sisi_pertama**2 + sisi_kedua**2 == sisi_ketiga**2 or sisi_kedua**2 + sisi_ketiga**2 == sisi_pertama**2 or sisi_ketiga**2 + sisi_pertama**2 == sisi_kedua**2:
    print("Segitiga siku-siku.")
else :
    print("segitiga sembarang")
