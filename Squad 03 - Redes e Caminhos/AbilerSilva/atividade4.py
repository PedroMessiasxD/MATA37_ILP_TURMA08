def organizingContainers(containers):
    n = len(containers)
    capacidades = []
    # Soma cada linha
    for i in range(n):
        soma_linha = 0
        for j in range(n):
            soma_linha += containers[i][j]
        capacidades.append(soma_linha)
    tipos = []
    # Soma cada coluna
    for j in range(n):
        soma_coluna = 0
        for i in range(n):
            soma_coluna += containers[i][j]
        tipos.append(soma_coluna)
    # Ordena para comparar
    capacidades.sort()
    tipos.sort()
    if capacidades == tipos:
        return "Possible"
    return "Impossible"
q = int(input())
for i in range(q):
    n = int(input())
    containers = []
    for _ in range(n):
        linha = list(map(int, input().split()))
        containers.append(linha)
    print(organizingContainers(containers))