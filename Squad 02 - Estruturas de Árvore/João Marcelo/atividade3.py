def proxima_palavra(w):
    letras = list(w)
    n = len(letras)

    # Encontra a primeira posição da direita para a esquerda
    i = n - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1

    # Não existe palavra maior
    if i == -1:
        return "no answer"

    # Encontra o menor caractere maior que letras[i]
    j = n - 1
    while letras[j] <= letras[i]:
        j -= 1

    # Troca os caracteres
    letras[i], letras[j] = letras[j], letras[i]

    # Inverte a parte final
    esquerda = i + 1
    direita = n - 1

    while esquerda < direita:
        letras[esquerda], letras[direita] = letras[direita], letras[esquerda]
        esquerda += 1
        direita -= 1

    return "".join(letras)


# Exemplos de uso
print(proxima_palavra("ab"))
print(proxima_palavra("bb"))
print(proxima_palavra("hefg"))
print(proxima_palavra("dhck"))
print(proxima_palavra("dkhc"))
