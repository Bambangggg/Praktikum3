import math as mtk
a = int(input("masukkan angka A :"))
b = int(input("Masukkan angka B :"))
c = int(input("Masukkan angka C :"))

if a == 0 :
    print("ini merupakan bukan dari persamaan kuadrat karena A = 0")

else :
    diskriminan = b**2 - (4 * a * c)
    print(f" diskriminan dari persamaan kuadrat dari {a}x^2 + {b}x + {c} =", diskriminan)

    if diskriminan == 0:
        print("Ini merupakan akar yang sama")
        print("maka akarnya ialah :",(-b + mtk.sqrt((b**2) - (4*a*c))) / 2*a)
    elif diskriminan > 0:
        print("ini merupakan akar real / berbeda")
        print("maka akarnya ialah :",(-b + mtk.sqrt((b**2) - (4*a*c))) / 2*a)
    else:
        print("ini merupakan tidak punya akar, karena diskriminan < 0")
        