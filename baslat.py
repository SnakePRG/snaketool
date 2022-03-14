import time
import webbrowser
import random



def sifreol():
    import random
 
 
    def rastgele_sifre_uret(uzunluk):
        harfler = 'abcdefghiABCDEFGHI123467890!_-*!_-*!_-*!_-*'
        sonuc = ''.join(random.choice(harfler) for i in range(uzunluk))
        return sonuc
 
    print("Şifreniz :",rastgele_sifre_uret(8))
 

def ortlm():
    snv1 = int(input("Birinci sınav sonucunu giriniz: "))
    snv2 = int(input("Birinci performans sonucunu giriniz: "))
    snv3 = int(input("İkinci sınav sonucunu giriniz: "))
    snv4 = int(input("İkinci performans sonucunu giriniz: "))

    sonuc = ((snv1+snv2+snv3+snv4)/4)

    print("Ortalamanız :", sonuc)
    

def hspmak():
    sy1 = int(input("Birinci sayıyı girin :"))
    sy2 = int(input("İkinci sayıyı girin :"))
    time.sleep(1)
    _islem = input("Yapmak istediğiniz matematiksel işlemi girin(+,-,*,/)")

    if _islem == "+":
        print(sy1+sy2)
    elif _islem == "-":
        print(sy1-sy2)
    elif _islem == "*":
        print(sy1*sy2)
    elif _islem == "/":
        print(sy1/sy2)
    else:
        print("Böyle bir işlem yok")


print("""
  _____             _        _____  _____   _____ 
 / ____|           | |      |  __ \|  __ \ / ____|
| (___  _ __   __ _| | _____| |__) | |__) | |  __ 
 \___ \| '_ \ / _` | |/ / _ \  ___/|  _  /| | |_ |
 ____) | | | | (_| |   <  __/ |    | | \ \| |__| |
|_____/|_| |_|\__,_|_|\_\___|_|    |_|  \_\\_____|
1. Ortalama hesaplama
2. Hesap makinesi
3. Şifre oluşturucu
4. SnakePRG web sitesi
5. SnakePRG github adresi
6. Python diğer program 
İşlemleri görmek için 'işlemler' ya da '7' ya basın.
Çıkmak için 'q' ya basın.
""")


while True:
    islem = input("İşlemi seçiniz :")

    if islem == "q":
        print("Program sonlandırılıyor...")
        break

    elif islem == "1":
        ortlm()

    elif islem == "2":
        hspmak()

    elif islem == "3":
        sifreol()

    elif islem == "4":
        print("Açılıyor...")
        webbrowser.open("https://eneserolsahin.wixsite.com/snakeprg")     

    elif islem == "5":
        print("Açılıyor...")
        webbrowser.open("https://github.com/snakeprg")     

    elif islem == "6": 
        print("Açılıyor...")
        webbrowser.open("https://github.com/SnakePRG/py-ornek/archive/refs/heads/main.zip")
        

    elif islem == "7" or islem == "islem" or islem == "işlem" or islem == "işlemler" or islem == "islemler":
        print("""
1. Ortalama hesaplama
2. Hesap makinesi
3. Şifre oluşturucu
4. SnakePRG web sitesi
5. SnakePRG github adresi
6. Python diğer program 
İşlemleri görmek için 'işlemler' ya da '7' ya basın.
Çıkmak için 'q' ya basın.
        """)
    
    else:
        print("Böyle bir işlem bulunmamakta, eğer eklenmesini istediğiniz bir işlem varsa '4' e basarak web sitemizden bize ulaşabilirsiniz.")
        time.sleep(2)
