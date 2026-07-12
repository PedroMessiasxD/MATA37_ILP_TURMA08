def organizingContainers(container):
    # Número de contêineres e tipos de bolas (matriz n x n)
    n = len(container)
    
    # Ssoma das linhas
    capacidade_conteineres = [sum(linha) for linha in container]
        
    # Soma das colunas
    total_tipos_bolas = [0] * n
    for i in range(n):
        for j in range(n):
            total_tipos_bolas[j] += container[i][j]
            
    capacidade_conteineres.sort()
    total_tipos_bolas.sort()
    
    if capacidade_conteineres == total_tipos_bolas:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    # Número de consultas (q)
    q = int(input().strip())

    # Itera sobre cada consulta
    for _ in range(q):
        # Lê o tamanho da matriz (n)
        n = int(input().strip())
        
        container = []
        
        # Lê as n linhas da matriz
        for _ in range(n):
            # Lê a linha, remove espaços em branco nas pontas e separa os números
            linha = list(map(int, input().rstrip().split()))
            container.append(linha)
            
        resultado = organizingContainers(container)
        print(resultado)