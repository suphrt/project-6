#вывод матрицы
A = [...]
with open("matrix.txt", "r", encoding="utf-8") as fin:
    lines = fin.readlines()
    for line in lines:
        s = line.strip()
        if s:
            row = list(map(int, input.split()))
            A.append
    n = len(A)
    m = len(A[0])
    for row in A[1:]:
        assert m == len(row)
