def organizingContainers(containers):
    n = len(containers)

    capacidade = []
    tipos = []

    # Soma das linhas (capacidade dos contêineres)
    for i in range(n):
        soma = 0
        for j in range(n):
            soma += containers[i][j]
        capacidade.append(soma)

    # Soma das colunas (quantidade de cada tipo)
    for j in range(n):
        soma = 0
        for i in range(n):
            soma += containers[i][j]
        tipos.append(soma)

    # Ordenação manual (Selection Sort)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if capacidade[j] < capacidade[menor]:
                menor = j
        capacidade[i], capacidade[menor] = capacidade[menor], capacidade[i]

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if tipos[j] < tipos[menor]:
                menor = j
        tipos[i], tipos[menor] = tipos[menor], tipos[i]

    # Comparação das listas
    for i in range(n):
        if capacidade[i] != tipos[i]:
            return "Impossible"

    return "Possible"


# Exemplo de uso
containers = [
    [1, 1],
    [1, 1]
]

print(organizingContainers(containers))
