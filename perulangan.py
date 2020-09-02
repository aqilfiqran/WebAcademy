fruits = ['semangka', 'pepaya', 'durian']

# print(fruits)

# perulangan iterable -> butuh list
for fruit in fruits[:2]:
    print(fruit, end=' ')

# range
for angka in range(1, 11):
    # semua angka yang habis dibagi 2 adalah angka genap
    if angka % 2 == 0:
        print(angka)

# modulo == sisa bagi
# 10 % 3 = 1

# perulangan range advanced
for angka in range(1, 11, 2):
    print(angka)

mahasiswa = {
    'nama': 'Aqil',
    'umur': '20 Tahun'
}

# mhs akan mengambi key
for mhs in mahasiswa:
    print(mahasiswa[mhs])
