# nama kelas buat ada huruf kapital diawal
class Kelas:  # parent
    # method constructor
    def __init__(self, nama='unknown', umur=20):
        self.nama = nama
        self.umur = umur

    def display(self):
        print(f'umur {self.nama} ini adalah : {self.umur}')

    def berlari(self):
        print('lari lari lari')


class Mahasiswa(Kelas):  # child
    def __init__(self, nama='unknown', umur=20, jurusan="informatika"):
        self.jurusan = jurusan
        super().__init__(nama=nama, umur=umur)


    # pemanggilan objek
kls = Mahasiswa("Aqil Fiqran")
# penggunaan mutator
kls.umur = 10
# penggunaan accessor
print(kls.jurusan)

# pemanggilan fungsi class
kls.berlari()


# oop
# 1. inheritance
# 2. polimorfisme
# 3. encapsulation
# 4. abstract
