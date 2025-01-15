import numpy as np


mahasiswa = np.array(['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'])
algoritma_dan_struktur_data = np.array([90, 50, 80])
matematika_numerik = np.array([80, 60, 70])

for i in range(len(mahasiswa)):
    print(f'{mahasiswa[i]}:')
    print(f'Nilai Algoritma dan Struktur Data: {algoritma_dan_struktur_data[i]}')
    print(f'Nilai MTK Numerik: {matematika_numerik[i]}')
    print()
