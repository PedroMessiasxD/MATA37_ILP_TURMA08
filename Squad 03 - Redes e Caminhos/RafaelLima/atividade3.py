def ordemlex(w):
    letras = list(w)
    n = len(letras)

    i = n - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"

    j = n - 1
    while letras[j] <= letras[i]:
        j -= 1

    letras[i], letras[j] = letras[j], letras[i]

    esquerda = i + 1
    direita = n - 1

    while esquerda < direita:
        letras[esquerda], letras[direita] = letras[direita], letras[esquerda]
        esquerda += 1
        direita -= 1

    return "".join(letras)

t = int(input())

for _ in range(t):
    w = input()
    print(ordemlex(w))