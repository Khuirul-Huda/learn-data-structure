from prettytable import PrettyTable

jumlah_char = int(input('Masukkan jumlah karakter: '))
chars = []
kalkulasi = {} #dictionary


for i in range(0, jumlah_char):
    chars.append(input('Masukkan karakter ke-' + str(i+1) + ': '))


for i in chars:
    if i not in kalkulasi:
        kalkulasi[i] = 1
    else:
        kalkulasi[i] += 1

print(kalkulasi)
table = PrettyTable(['Karakter', 'Frekuensi'])

for i in kalkulasi:
    table.add_row([i, kalkulasi[i]])

print(table)