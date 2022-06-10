def Gauss(A):
    for k in range(len(A) - 1):
        B = A.copy()
        for i in range(len(A)):
            assert B[i] is A[i]
            for j in range(len(A)):
                if(i <= k):
                    A[i][j] = B[i][j]
                elif(i > k and j > k):
                    A[i][j] = round(B[i][j] - (B[i][k] / B[k][k]) * B[k][j])
                elif(i > k and j <= k):
                    A[i][j] = 0
    return A

matrix = [[2, 1, 3], [4, 1, 7], [3, 2, 4]]
z = int(input())
cnt = 0
cnt = len([x for x in matrix if sum(x)/len(x) < z])
print(cnt)
M = Gauss(matrix)
for row in M:
    print(" ".join([str(x) for x in row if x!=0]))