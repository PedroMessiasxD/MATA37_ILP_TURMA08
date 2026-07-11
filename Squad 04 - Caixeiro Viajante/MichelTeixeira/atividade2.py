def soma_array(ar):
    soma = 0

    for i in range(len(ar)):
        soma = soma + ar[i]

    return soma


n = int(input())

while n <= 0:
    n = int(input())

entrada = input().split()

while len(entrada) != n:
    entrada = input().split()

ar = []
entrada_valida = False

while entrada_valida == False:
    ar = []
    entrada_valida = True

    for i in range(n):
        numero = int(entrada[i])

        if numero <= 0 or numero > 1000:
            entrada_valida = False

        ar.append(numero)

    if entrada_valida == False:
        entrada = input().split()

resultado = soma_array(ar)

print(resultado)