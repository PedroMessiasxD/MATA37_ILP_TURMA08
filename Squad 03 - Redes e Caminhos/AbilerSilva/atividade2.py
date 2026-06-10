lista = list(map(int, input().split()))
def soma():
    total = 0
    for numero in lista:
        total += numero
    print(total)
soma()