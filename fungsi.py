def sayHi():
    print('Haii')


def sayHello():
    return "hello"


# fungsi parameter
def panggilNama(nama='unknown', umur=0):
    # print('hai ', nama)
    print(f'hai {nama} yang berumur {umur}')


# sayHi()

# print(sayHello())

panggilNama("Aqil", 20)


def kasihNilai():
    return 20


# saat memanggil kasihNilai() == 20
nama = kasihNilai()
# nama = 20

print(nama)


def mahasiswa(nama='unknown', umur=20):
    print(f'nama: {nama}\numur : {umur}')


# method == fungsi
# polimorfisme
mahasiswa()
mahasiswa('Aqil')
mahasiswa('Aqil', 22)
