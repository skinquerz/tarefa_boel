# separador de número primo

num = 200

for i in range(2, num+1):
    if all(i % j != 0 for j in range(2, i)):
        print(i, end=' ')