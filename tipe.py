aqil = budi = "20 tahun"

# index dimulai dari 0 bukan 1
nama = ['Aqil', 20, 'Mahasiswa']  # list
nama[0] = 'badri'
mahasiswa = ('aqil', 'budi', 'badri', 'prinanda',
             'putra', 'tes', 'belajar')  # tuple

# akhiri dari index akhir + 1
print(mahasiswa[:2])  # 0 1
# mulai dari index awal
print(mahasiswa[1:])  # 1 2 3 4

print(mahasiswa[1:4])

# negatif index
print(mahasiswa[:-2])
