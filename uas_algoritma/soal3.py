class Antrian:
    def _init_(self):
        self.antrian_restorean = []

    
    def enqueue(self, pesenan):
        self.antrian_restorean.append(pesenan)
        print(f"Pesenan '{pesenan}' telah ditambahkan ke dalam antrian pesenan.")

    
    def dequeue(self):
        if len(self.antrian_restorean) > 0:
            pesenan = self.antrian_restorean.pop(0)
            print(f"Pesenan '{pesenan}' telah dihapus dari dalam antrian pesenan.")
            return pesenan
        else:
            print("tidak ada antiran .")
            return