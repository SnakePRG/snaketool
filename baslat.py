import time
import webbrowser

def ortlm():
    snv1 = int(input("Birinci sınav sonucunu giriniz: "))
    snv2 = int(input("Birinci performans sonucunu giriniz: "))
    snv3 = int(input("İkinci sınav sonucunu giriniz: "))
    snv4 = int(input("İkinci performans sonucunu giriniz: "))

    sonuc = ((snv1+snv2+snv3+snv4)/4)

    print("Ortalamanız :", sonuc)
    time.sleep(2)
    exit()

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
1. Ortalama hesaplama
2. Hesap makinesi
3. SnakePRG web sitesi
4. SnakePRG github adresi
5. Python diğer program
İşlemleri görmek için 'işlemler' ya da '6' ya basın.
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
        print("Açılıyor...")
        webbrowser.open("https://eneserolsahin.wixsite.com/snakeprg")     

    elif islem == "4":
        print("Açılıyor...")
        webbrowser.open("https://github.com/snakeprg")     

    elif islem == "5": 
        print("Açılıyor...")
        webbrowser.open("https://github.com/SnakePRG/py-ornek/archive/refs/heads/main.zip")
        

    elif islem == "6" or islem == "islem" or islem == "işlem" or islem == "işlemler" or islem == "islemler":
        print("""
1. Ortalama hesaplama
2. Hesap makinesi
3. SnakePRG web sitesi
4. SnakePRG github web sitesi
5. Python diğer program
İşlemleri görmek için 'işlemler' ya da '6' ya basın.
Çıkmak için 'q' ya basın.
        """)
    
    else:
        print("Böyle bir işlem bulunmamakta, eğer eklenmesini istediğiniz bir işlem varsa '3' e basarak web sitemizden bize ulaşabilirsiniz.")
        time.sleep(2)
