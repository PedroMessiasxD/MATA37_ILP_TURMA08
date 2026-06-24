def palavra_nova(w):

    letras = list(w)
    n = len(letras)

    # Encontrar o pivô
    pivo_idx = -1

    for i in range(n - 2, -1, -1):
        if letras[i] < letras[i + 1]:
            pivo_idx = i
            break

    # Não existe palavra maior
    if pivo_idx == -1:
        return "no answer"

    # Parte da palavra após o pivô
    cauda = letras[pivo_idx + 1:]

    # Encontrar letras maiores que o pivô
    candidatos = [
        letra for letra in cauda
        if letra > letras[pivo_idx]
    ]

    # Escolher a menor delas
    letra_escolhida = min(candidatos)

    # Descobrir sua posição na cauda
    idx_na_cauda = len(cauda) - 1 - cauda[::-1].index(letra_escolhida)

    # Remover da cauda
    cauda.pop(idx_na_cauda)

    # Adicionar o pivô
    cauda.append(letras[pivo_idx])

    # Ordenar para obter a menor resposta possível
    cauda.sort()

    # Montar a nova palavra
    inicio = letras[:pivo_idx]

    resultado = inicio + [letra_escolhida] + cauda

    return "".join(resultado)
