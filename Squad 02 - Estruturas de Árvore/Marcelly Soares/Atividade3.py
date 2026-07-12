def biggerIsGreater(w):
    lista = list(w)

    # Procura da direita para a esquerda
    i = len(lista) - 2
    while i >= 0 and lista[i] >= lista[i + 1]:
        i -= 1

    # Se não encontrou, não existe resposta
    if i == -1:
        return "no answer"

    # Procura a menor letra maior que lista[i]
    j = len(lista) - 1
    while lista[j] <= lista[i]:
        j -= 1

    # Troca as letras
    lista[i], lista[j] = lista[j], lista[i]

    # Inverte a parte da direita
    esquerda = lista[:i + 1]
    direita = lista[i + 1:]
    direita.reverse()

    # Junta tudo
    resultado = esquerda + direita

    return "".join(resultado)


# Testes
print(biggerIsGreater("ab"))    # ba
print(biggerIsGreater("bb"))    # no answer
print(biggerIsGreater("hefg"))  # hegf
print(biggerIsGreater("dhck"))  # dhkc
print(biggerIsGreater("dkhc"))  # hcdk