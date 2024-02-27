
from prettytable import PrettyTable

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
nama_mahasiswa = []
rata_rata_mk = []



for i in range(0, jumlah_mahasiswa):
    nama_mahasiswa.append(input('Masukkan nama mahasiswa ke-' + str((i + 1)) + ': '))
    jumlah_mk = int(input('Masukkan Jumlah MK: '))
    nilai_mk = 0

    for i in range(0, jumlah_mk):
        nilai_mk += int(input('Masukkan nilai MK ke-' + str(i+1) + '  ' ))
    
    rata_rata_individu = nilai_mk / jumlah_mk
    rata_rata_mk.append(rata_rata_individu)

table = PrettyTable(["Nama", "Rata-rata"])

for i in range(0, jumlah_mahasiswa):
    table.add_row([nama_mahasiswa[i], rata_rata_mk[i]])

print(table)

