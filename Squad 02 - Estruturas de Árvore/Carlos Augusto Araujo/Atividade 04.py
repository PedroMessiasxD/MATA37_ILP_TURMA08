def organizingContainers(container):
    capacidades = [sum(linha) for linha in container]
    
    n = len(container)
    tipos = [sum(container[i][j] for i in range(n)) for j in range(n)]
    
    capacidades.sort()
    tipos.sort()
    
    return "Possible" if capacidades == tipos else "Impossible"

q = int(input())
for _ in range(q):
    n = int(input())
    container = []
    for _ in range(n):
        container.append(list(map(int, input().split())))
    print(organizingContainers(container))