def letra_maior(w):
    letras = list(w)
    #Encontra a letra principal
    i = len(letras) - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    #Encontra o menor caractere maior que o principal
    j = len(letras) - 1

    while letras[j] <= letras[i]:
        j -= 1
    #Troca as letras
    letras[i], letras[j] = letras[j], letras[i]

    #Inverter a parte da direita
    esquerda = i + 1
    direita = len(letras) - 1

    while esquerda < direita:
        letras[esquerda], letras[direita] = letras[direita], letras[esquerda]
        esquerda += 1
        direita -= 1

    return "".join(letras)
numero = int(input())
for i in range(numero):
    palavra = input()
    print(letra_maior(palavra))