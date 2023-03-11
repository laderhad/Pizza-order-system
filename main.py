import pandas as pd
from uydl import *
import time

import datetime 


a = pd.read_excel('urunler.xlsx', index_col='index')
pizza_list = []

for index, row in a.iterrows():
    aizza = Pizza(row['ürün adı'], row['Fiyat'])
    setattr(aizza, 'index', index)
    globals()[index] = aizza
    pizza_list.append(aizza)
    
    
df=pd.read_excel("pizzatipi.xlsx",index_col="index")
pizza_aciklamalari=[]
for index ,row in df.iterrows():
    aciklama=pizza(row["ürün adı"],row["Fiyat"],row["Açıklama"])
    setattr(aciklama,"index",index)
    globals()[index]=aciklama
    pizza_aciklamalari.append(aciklama)
    




    
    

siparisler = [] 
print("----------------sipariş zamanı----------------") 
while True:
    print(a.iloc[0:7])
    y = input("Eğer pizzalarımız hakkında daha detaylı bilgi almak isterseniz m'ye, istemiyorsanız q'ya basınız:")
    if y == "m":
        print(a.iloc[0:7])
        while True:
            pizzadi = str(input("Bilgi almak istediğiniz pizzanın indeksini girin(döngüden çıkmak için x'e basın):"))
            if pizzadi == "x":
                break
            else:
                print(globals()[pizzadi].get_describe())
        
    elif y == "q":
        break
    else:
        print("Doğru index girin")
        
    
soslar = []
ek_malzeme=[]        
while True:
    print(a.iloc[0:7])
    i = str(input("Lütfen sipariş vermek için bir pizza indeksi seçin (urun1 gibi) (Çıkış yapmak için 'q' ya basın): "))
    if i == "q":
         break
    else:
        pizzafiyati = globals()[i].get_cost()
        
        while True:
            print(a.iloc[7:17])
            y = str(input("Pizzanıza istediğiniz sos nedir? Index girin (seçtiğinizde q'ya basın): "))
            if y == "q":
                break
            else:
                soslar.append(y)
                pizzasosfiyati = globals()[y].get_cost()
                print(a.iloc[17:])
        while True:
            
            print(a.iloc[17:])
            z = str(input("Pizzanıza istediğiniz ek malzemeler nedir? Index girin (seçtiğinizde q'ya basın): "))
            if z == "q":
                break
            else:
                ek_malzeme.append(z)
                ekmalzemefiyati = globals()[z].get_cost()
        
        siparisler.append((globals()[i], [globals()[sid] for sid in soslar], [globals()[eid] for eid in ek_malzeme]))



siparislistesi=[]    
toplam_fiyat = 0
for i, siparis in enumerate(siparisler):
    fiyat = siparis[0].get_cost() 
    for sos in siparis[1]:
        fiyat += sos.get_cost()
    for ek_malzeme in siparis[2]:
        fiyat += ek_malzeme.get_cost()
    toplam_fiyat += fiyat
    print(f"\nSipariş {i+1}:")
    print(f"Pizza: {siparis[0].urunadi}")
    print(f"Pizzanın sosları:{[sos.urunadi for sos in siparis[1]]}")
    print(f"Pizzanın ek malzemeleri:{[malzeme.urunadi for malzeme in siparis[2]]}")
    print(f"Siparişinizin fiyatı: {fiyat} TL")
    siparislistesi.append((f"Sipariş {i+1}:",f"Pizza: {siparis[0].urunadi}",f"Pizzanın sosları:{[sos.urunadi for sos in siparis[1]]}",f"Pizzanın ek malzemeleri:{[malzeme.urunadi for malzeme in siparis[2]]}"))

    
    


print(f"\nToplam ödenecek tutar: {toplam_fiyat} TL")
        
    

print("kullanıcı sayfasına yönlendiriliyorsunuzz....")
time.sleep(4)
adsoyad=input(str("Adınız ve soyisminiz:"))
    

    

    
    
print("adres sayfasına yönlendiriliyorsunuzz....")
time.sleep(3)
ilce=str(input("Yaşadığınız ilce:"))
mahalle=str(input("Yaşadığınız mahalle:"))
sokak=input("Sokak:")
no=input("Ev ve daire:")
adresbilgileri=[ilce,mahalle,sokak,no]
    
print("Ödeme sayfasına gönderiliyorsunuz...")
time.sleep(2)
while True:
    kartnumarasi = input("Kart numaranızı herhangi bir boşluk olmadan yazınız:")
    if len(kartnumarasi) != 16:
        print("Lütfen doğru bir kart numarası yazın")
    else:
        break

while True:
    kartintarihiayi = input("Kartın son kullanım ayı:")
    if len(kartintarihiayi) != 2:
        print("2 basamaklı olması gerekiyor")
    else:
        break

while True:
    kartintarihiyili = input("Kartın son kullanım yılının son 2 hanesi:")
    if len(kartintarihiyili) != 2:
        print("2 basamaklı olması gerekiyor")
    else:
        break

while True:
    cvc = input("Kartın güvenlik kodu:")
    if len(cvc) != 3:
        print("3 basamaklı olması gerekiyor")
    else:
        break
while True:
    confirmation = input("Siparişi onaylıyor musunuz? (E/H): ")
    if confirmation.upper() == "E":
        print("Siparişiniz başarıyla alındı!")
        break
    elif confirmation.upper() == "H":
        print("Siparişiniz iptal edildi!")
        siparisler = []  
        soslar = []  
        ek_malzeme = []  
        break
    else:
        print("Lütfen geçerli bir seçenek seçin (E/H):") 

kartbilgileri = [kartnumarasi, kartintarihiayi, kartintarihiyili, cvc]
bilgiler = pd.DataFrame({"siparişler": [(siparislistesi)], "adres bilgileri": [adresbilgileri], "kart bilgileri":[kartbilgileri]}, index=[adsoyad])

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
filename =f"{date_string}-{adsoyad}_siparis.xlsx"
with pd.ExcelWriter(filename) as writer:
    bilgiler.to_excel(writer, index=True)


print("Siparişiniz oluşturuldu..")
print("Bizi tercih ettiğiniz için teşekkür ederiz")
           
                
    
        
    
    
    
    
    
    
