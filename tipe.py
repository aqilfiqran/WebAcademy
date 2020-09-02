aqil = budi = "20 tahun"

# index dimulai dari 0 bukan 1
nama = ['Aqil', 20, 'Mahasiswa']  # list
nama[0] = 'badri'
hari = ('senin', 'selasa', 'rabu', 'kamis',
        "jum'at", 'sabtu', 'minggu')  # tuple

# akhiri dari index akhir + 1
# print(mahasiswa[:2])  # 0 1
# mulai dari index awal
# print(mahasiswa[1:])  # 1 2 3 4

# print(mahasiswa[1:4])

# negatif index
# print(mahasiswa[:-2])

# dictionary = kamus -> bisa dicustom index
mahasiswa = {
    'nama': 'Aqil Fiqran',
    'umur': 20,
    'jurusan': 'Informatika',
    'bidang': 'Rekayasa Perangkat Lunak',
    'skill': [
        'php', 'javascript', 'perl', 'c', 'c++', 'python'
    ]
}

print(mahasiswa['skill'][:-1])
