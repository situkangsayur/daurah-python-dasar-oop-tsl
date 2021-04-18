from abc import ABC

class BangunRuang3DSegitiga(ABC):

    def luas(self, alas  = None, tinggi = None):
        pass

    def volume(self,  panjang = None, lebar = None, tinggi = None):
        pass


class BangunRuang3DKotak(ABC):

    def luas(self, panjang = None, lebar = None):
        pass

    def volume(self, panjang = None, lebar = None, tinggi = None):
        pass


# implementation 

class Prisma(BangunRuang3DSegitiga):
    def luas(self, alas  = None, tinggi = None):
        return 0.5 * alas * tinggi

    def volume(self, panjang = None, lebar = None, tinggi = None):
        return 0.5*panjang* lebar * tinggi

class Limas(BangunRuang3DSegitiga):
    def luas(self, alas  = None, tinggi = None):
        return (1/2) * alas * tinggi

    def volume(self, panjang = None, lebar = None, tinggi = None):
        return (1/3) * panjang * lebar * tinggi




class Balok(BangunRuang3DKotak):

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self, panjang = None, lebar = None):
        return panjang*lebar

    def volume(self, panjang = None, lebar = None, tinggi = None):
        return panjang * lebar*tinggi
