def proxima_palavra(w):
    n = len(w)

    # Procurar a posição que pode ser aumentada
    posicao = n - 2

    while posicao >= 0 and w[posicao] >= w[posicao + 1]:
        posicao -= 1

    if posicao < 0:
        return "no answer"

    pivo = w[posicao]

    # Procurar a menor letra maior que o pivô no lado direito
    indice_melhor = -1
    i = posicao + 1

    while i < n:
        if w[i] > pivo:
            if indice_melhor == -1 or w[i] < w[indice_melhor]:
                indice_melhor = i
        i += 1

    letra_escolhida = w[indice_melhor]

    # Contar as letras que ficarão depois da nova posição
    contagem = [0] * 26

    i = posicao + 1
    while i < n:
        letra_atual = w[i]
        indice = ord(letra_atual) - ord('a')
        contagem[indice] += 1
        i += 1

    # A letra escolhida sai do final e vai para a posição do pivô
    indice = ord(letra_escolhida) - ord('a')
    contagem[indice] -= 1

    # O pivô antigo entra no final da palavra
    indice = ord(pivo) - ord('a')
    contagem[indice] += 1

    # Montar a resposta
    resposta = ""

    # Copiar a parte antes do pivô
    i = 0
    while i < posicao:
        resposta += w[i]
        i += 1

    # Colocar a letra escolhida no lugar do pivô
    resposta += letra_escolhida

    # Montar o restante em ordem crescente usando a contagem
    letra_indice = 0

    while letra_indice < 26:
        quantidade = contagem[letra_indice]
        letra = chr(ord('a') + letra_indice)

        while quantidade > 0:
            resposta += letra
            quantidade -= 1

        letra_indice += 1

    return resposta


print("=== Atividade 3: Próxima Palavra Lexicográfica ===")
print()
print("Primeiro, digite a quantidade de palavras que serão testadas.")
print("Depois, digite uma palavra por linha.")
print()
print("Exemplo de entrada:")
print("5")
print("ab")
print("bb")
print("hefg")
print("dhck")
print("dkhc")
print()
print("Agora é sua vez.")
print()

entrada_t = input("Digite a quantidade de palavras: ")

while not entrada_t.isdigit():
    print("Erro: você deve digitar um número inteiro.")
    entrada_t = input("Digite a quantidade de palavras: ")

t = int(entrada_t)

contador = 1

while contador <= t:
    palavra = input("Digite a palavra " + str(contador) + ": ")

    resultado = proxima_palavra(palavra)

    print("Resultado:", resultado)
    print()

    contador += 1