A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]


if (len(A) != len(B)):
    print('Matriks tidak bisa dijumlahkan')


AB = [[] for i in range(len(A))]

for a in range(0, len(A)):
    for b in range (0, len(A[a])):
        AB[a].append(A[a][b] + B[a][b])

print(AB)
