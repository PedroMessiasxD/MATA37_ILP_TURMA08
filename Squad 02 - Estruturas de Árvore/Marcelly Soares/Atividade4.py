def organizingContainers(containers):
    n = len(containers)

    capacidade = []
    tipos = []

    # Soma da capacidade dos contêineres
    for i in range(n):
        soma = 0
        for j in range(n):
            soma = soma + containers[i][j]
        capacidade.append(soma)

    # Soma da quantidade de cada tipo
    for j in range(n):
        soma = 0
        for i in range(n):
            soma = soma + containers[i][j]
        tipos.append(soma)

    # Ordenação da capacidade
    for i in range(n):
        for j in range(0, n - i - 1):
            if capacidade[j] > capacidade[j + 1]:
                temp = capacidade[j]
                capacidade[j] = capacidade[j + 1]
                capacidade[j + 1] = temp

    # Ordenação dos tipos
    for i in range(n):
        for j in range(0, n - i - 1):
            if tipos[j] > tipos[j + 1]:
                temp = tipos[j]
                tipos[j] = tipos[j + 1]
                tipos[j + 1] = temp

    # Comparação
    for i in range(n):
        if capacidade[i] != tipos[i]:
            return "Impossible"

    return "Possible"


# Teste 1
containers = [
    [1, 1],
    [1, 1]
]

print(organizingContainers(containers))  # Possible


# Teste 2
containers = [
    [0, 2],
    [1, 1]
]

print(organizingContainers(containers))  # Impossible