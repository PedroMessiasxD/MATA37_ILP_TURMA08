from collections import Counter


def organizingContainers(container):
    n = len(container)


    capacidades_containers = []
    for i in range(n):
        soma = 0
        for j in range(n):
            soma += container[i][j]
        capacidades_containers.append(soma)


    quantidades_bolas = []
    for j in range(n):
        soma = 0
        for i in range(n):
            soma += container[i][j]
        quantidades_bolas.append(soma)


    if Counter(capacidades_containers) == Counter(quantidades_bolas):
        return "Possible"
    else:
        return "Impossible"



def main():
    q = int(input().strip())
    resultados = []

    for _ in range(q):
        n = int(input().strip())
        container = []

        for _ in range(n):
            linha = list(map(int, input().strip().split()))
            container.append(linha)

        resultados.append(organizingContainers(container))


    print("\n".join(resultados))


if __name__ == "__main__":
    main()
