# Função que verifica se é possível organizar as bolas
def organizingContainers(container):

    # Lista para armazenar a capacidade total de cada contêiner
    capacidades = []

    # Soma dos elementos de cada linha
    for linha in container:

        total = 0

        for valor in linha:
            total += valor

        capacidades.append(total)

    # Lista para armazenar a quantidade total de cada tipo de bola
    tipos = []

    n = len(container)

    # Soma dos elementos de cada coluna
    for coluna in range(n):

        total = 0

        for linha in range(n):
            total += container[linha][coluna]

        tipos.append(total)

    # Ordena as listas para comparar os valores
    capacidades.sort()
    tipos.sort()

    # Se as capacidades dos contêineres forem iguais às quantidades
    # dos tipos de bolas, é possível reorganizar
    if capacidades == tipos:
        return "Possible"

    return "Impossible"


# Número de consultas
q = int(input())

for _ in range(q):

    # Número de contêineres e tipos de bolas
    n = int(input())

    container = []

    # Leitura da matriz
    for _ in range(n):
        linha = list(map(int, input().split()))
        container.append(linha)

    print(organizingContainers(container))
