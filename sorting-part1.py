print('Program ini akan mengurutkan bilangan dari yang terbesar')
jumlah_angka = 10

number = []
for i in range(10):
    print('Masukkan Angka ke ', i+1)
    number.append(int(input()))


#number.sort(reverse=True)
print(number)

# def bubble_sort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if list[j] < list[j+1] :
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list

# print(bubble_sort(number))
