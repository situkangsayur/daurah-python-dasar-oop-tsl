from . import BangunRuang3DSegitiga, Limas, Prisma

def hitung_volume_3d_segitiga(bangun: BangunRuang3DSegitiga, panjang, lebar, tinggi):
    return bangun.volume(panjang, lebar, tinggi)


# dependency inversion
def hitung_volume_limas(bangun: Limas, panjang, lebar, tinggi):
    return bangun.volume(panjang, lebar, tinggi)

def hitung_volume_prisma(bangun: Prisma, panjang, lebar, tinggi):
    return bangun.volume(panjang, lebar, tinggi)
