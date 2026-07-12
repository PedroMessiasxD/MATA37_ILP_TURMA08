def ordenar(lista):
    arr = list(lista)
    tamanho = len(arr)
    for i in range(tamanho):
        for j in range(tamanho - 1):
            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
    return arr


def organizingContainers(container):
    n = len(container)
    somas_linhas = []
    somas_colunas = [0] * n

    for i in range(n):
        soma_linha = 0
        for j in range(n):
            valor = container[i][j]
            soma_linha = soma_linha + valor
            somas_colunas[j] = somas_colunas[j] + valor
        somas_linhas.append(soma_linha)

    somas_linhas = ordenar(somas_linhas)
    somas_colunas = ordenar(somas_colunas)

    for k in range(n):
        if somas_linhas[k] != somas_colunas[k]:
            return "Impossible"

    return "Possible"
