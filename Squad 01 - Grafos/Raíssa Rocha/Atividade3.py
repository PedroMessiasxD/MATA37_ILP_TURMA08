def palavra(p):
    letras = list(p)
    n = len(letras)

    i = n - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1

    if i < 0:
        return "no answer"

    j = n - 1
    while letras[j] <= letras[i]:
        j -= 1

    temp = letras[i]
    letras[i] = letras[j]
    letras[j] = temp

    inicio = i + 1

    for x in range(inicio, n):
        for y in range(inicio, n - 1):
            if letras[y] > letras[y + 1]:
                temp = letras[y]
                letras[y] = letras[y + 1]
                letras[y + 1] = temp

    resultado = ""
    for letra in letras:
        resultado += letra

    return resultado


T = int(input())

for _ in range(T):
    p = input()
    print(palavra(p))
