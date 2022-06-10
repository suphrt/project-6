#ввод матрицы в файл
A = [...]
with open("matrix.txt", "w", encoding="utf-8") as file:
    for row in A:
        print(" ".join([str(x) for x in row]))