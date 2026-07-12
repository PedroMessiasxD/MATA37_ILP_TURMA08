def biggerIsGreater(w):
    letras = list(w)
    tamanho = len(letras)

    i = tamanho - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i = i - 1

    if i < 0:
        return "no answer"

    j = tamanho - 1
    while letras[j] <= letras[i]:
        j = j - 1

    aux = letras[i]
    letras[i] = letras[j]
    letras[j] = aux

    inicio = i + 1
    fim = tamanho - 1
    while inicio < fim:
        aux2 = letras[inicio]
        letras[inicio] = letras[fim]
        letras[fim] = aux2
        inicio = inicio + 1
        fim = fim - 1

    nova_palavra = ""
    for letra in letras:
        nova_palavra = nova_palavra + letra

    return nova_palavra
