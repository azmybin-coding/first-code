daftar_buku = ['Seven Habits', 'How To Be a Leader', 'Laskar Pelangi']
print("Tampilkan variabel daftar_buku")
print("daftar_buku")

print("\nProses dengan for in")
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[1])
print(daftar_buku[0])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList dinamis')
daftar_buku = (123, 'Iron Man 2', '300 Sparta')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nKembalikan data list ke awal')
daftar_buku = ['Seven Habits', 'How To Be a Leader', 'Laskar Pelangi']
print(daftar_buku)
print('\nTambahkan 1 buku baru')
daftar_buku.append('Bahasa Indonesia')
print(daftar_buku)

print('\nClear daftar_buku')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'How To Be a Leader', 'Laskar Pelangi']
daftar_buku[0] = 'Six Habits'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['Seven Habits', 'How To Be a Leader', 'Laskar Pelangi']
print('\nPop')
daftar_buku.pop(-1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How To Be a Leader', 'Laskar Pelangi']
del daftar_buku[0]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How To Be a Leader', 'Laskar Pelangi']
del daftar_buku[:]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])






