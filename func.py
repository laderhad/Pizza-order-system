import pandas as pd
import uydl
pizza_tipi=pd.DataFrame({"ürün adı":["Eko Sucuklu Pizza","Margarita Pizza","Super Pizza","Pepporoni pizza","Gamer Pizza","Akdeniz Pizza","Greek Pizza"],"Fiyat":[72,74,75,72,76,75,67]  
,"Açıklama":["Uygun fiyatlı bir pizza çeşidi olup, sucuklu lezzetiyle öne çıkar.","İtalyan usulü bir pizza çeşididir ve domates sosu, mozzarella peyniri ve taze fesleğen ile hazırlanır.","İçerisinde birçok farklı malzeme bulunan, çeşitli tatları bir araya getiren bir pizza türüdür.","Amerikan tarzı bir pizza türüdür ve üzerinde bol miktarda pepperoni (sosis dilimleri) bulunur.","Özellikle gençlerin tercih ettiği bir pizza türüdür ve içeriğinde genellikle fast food tarzı malzemeler bulunur.","İçerisinde zeytin, feta peyniri, domates gibi Akdeniz mutfağına ait malzemelerin bulunduğu bir pizza çeşididir.","Yunan mutfağından esinlenerek hazırlanan bir pizza türüdür ve üzerinde genellikle zeytin, feta peyniri ve domates bulunur."]},index=[1,2,3,4,5,6,7])

soslar=pd.DataFrame({"ürün adı":["Marinara sosu","Alfredo sosu","Barbekü sosu","Pesto sosu","Ranch sosu","Buffalo sosu","Beyaz sos","Acı sos","Siyah zeytin sosu","Domates sosu"],"Fiyat":[0.5,0.5,1,1,0.5,0.25,0,0,0,0]},index=[1,2,3,4,5,6,7,8,9,10])

ek_malzeme=pd.DataFrame({"ürün adı":["Jambon","Mantar","Salam","Zeytin","Sosis","Acı biber","Yeşil biber","Kırmızı biber","Füme","Somon","Mozerella","Roka","Soğan","Mısır","Brokoli"],"Fiyat":[3,3,8,1,5,1,1,1,8,9,5,1,1,1,1]},index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

pizza_tipi.to_excel("pizzatipi.xlsx",index=True)
ek_malzeme.to_excel("ek_malz.xlsx",index=True)
soslar.to_excel("soslar.xlsx",index=True)



