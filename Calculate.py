hesap_makinesi = 
'''
1-) Toplama işlemi
2-) Çikarma işlemi
3-) Çarpma işlemi
4-) Bölme işlemi 
işlem seçiniz 
'''
print(hesap_makinesi)
secim = str(input("işlem seçiniz: "))
sayi1 = int(input("sayı1 giriniz: "))
sayi2 = int(input("sayı2 giriniz: "))




if secim == "1":
    Toplama = sayi1 + sayi2
    print ("\n Toplama sonucunuz={} ".format(Toplama) )
    pass
elif secim == "2" :
    Çıkarma = sayi1 - sayi2
    print("\n Çıkarma sonucunuz={} ".format(Çıkarma))
    pass
elif secim == "3" :
    Çarpma = sayi1 * sayi2
    print("\n Çarpma sonucunuz={} ".format(Çarpma))
    pass
elif secim == "4" :
    Bölme = sayi1/sayi2
    print("\n Bölme sonucunuz={} ".format(Bölme))
    pass
else:
    print("Geçersiz işlem")
