from functions.dua_dimensi import luas_kotak, luas_persegi_panjang, luas_segitiga

from functions import Balok, Prisma, Limas, BangunRuang3DSegitiga
from functions.tiga_dimensi import  hitung_volume_3d_segitiga

class PrismaBaru(BangunRuang3DSegitiga):
    def luas(self, alas  = None, tinggi = None):
        return 0.5 * alas * tinggi

    def volume(self, panjang = None, lebar = None, tinggi = None):
        return 0.25*panjang* lebar * tinggi


if __name__ == '__main__':

    # print(luas_kotak(2))

    balok = Balok(2,3)
    prisma = Prisma()
    limas = Limas()

    print('prisma : ' + str(hitung_volume_3d_segitiga(prisma, 2,3,4)))
    print('limas : ' + str(hitung_volume_3d_segitiga(limas, 2,3,4)))

    prisma_baru = PrismaBaru()
    print('limas : ' + str(hitung_volume_3d_segitiga(prisma_baru, 2,3,4)))


    

