print('Program ini akan mengurutkan bilangan dari yang terbesar')

number = []
for i in range(3):
    print('Masukkan Angka ke ', i+1)
    number.append(int(input()))

number.sort(reverse=True)
print(number)
