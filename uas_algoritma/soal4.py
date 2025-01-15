class buah:
    def __init__(self,nama,warna,rasa):
        
        self.warna = warna
        self.nama = nama
        self.rasa = rasa
        
    def setwarna(self,item):
            self.warna = item
        
    def information(self):
            print( f"buah saya : {self.nama} berwarna :{self.warna} ber rasa :{self.rasa}")

buah1 = buah("mangga","Putih","manis")
buah2 = buah("melon","Hijau","manis")

buah1.setwarna("Merah")
buah2.setwarna("Biru")

buah1.information()
buah2.information()
