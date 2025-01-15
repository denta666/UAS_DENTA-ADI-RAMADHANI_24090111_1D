nim_list = []
nama_list = []

while True:
    nim = input('Masukan NIM: ')
    nama = input('Masukan Nama: ')

    nim_list.append(nim)
    nama_list.append(nama)

    for loop in range(1, 2):
        print(loop)
        if loop == 1:
            print('NIM:', nim)
            print('Nama:', nama)
            print('Selesai')

    lanjut = input('Apakah Anda ingin menambah data lagi? (y/n): ')
    if lanjut.lower() != 'y':
        break

print('Data yang sudah dimasukkan:')
for i in range(len(nim_list)):
    print(f'NIM: {nim_list[i]}, Nama: {nama_list[i]}')
