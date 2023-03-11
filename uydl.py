import pandas as pd

class Pizza():
    def __init__(self, urunadi, fiyat):
        self.urunadi = urunadi
        self.fiyat = fiyat
        
    def get_cost(self):
        return self.fiyat
    

    
class pizza(Pizza):
    def __init__(self, urunadi, fiyat, aciklama):
        super().__init__(urunadi, fiyat)
        self.aciklama = aciklama
        
    def get_describe(self):
        print(f"İsmi {self.urunadi} olan ürünümüz {self.aciklama} ve fiyatı {self.fiyat} TL'dir.")
        


