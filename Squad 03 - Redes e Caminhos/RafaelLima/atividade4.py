def organizingContainers(containers):
    capacidade = sorted(sum(linha) for linha in containers)

    tipos = []
    n = len(containers)

    for coluna in range(n):
        total = 0
        for linha in range(n):
            total += containers[linha][coluna]
        tipos.append(total)

    tipos.sort()

    if capacidade == tipos:
        return "Possible"
    else:
        return "Impossible"


q = int(input())

for x in range(q):
    n = int(input())

    containers = []

    for x in range(n):
        linha = list(map(int, input().split()))
        containers.append(linha)

    print(organizingContainers(containers))