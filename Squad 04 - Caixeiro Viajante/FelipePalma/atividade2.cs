
def somasdados(ar):

    adicao = 0
    for element in ar:
        adicao += element
    return adicao


n = int(input().strip())
ar = list(map(int, input().strip().split()))


resultado1 = somasdados(ar)
print(resultado1)
