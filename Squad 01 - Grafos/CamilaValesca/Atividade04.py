def organizingContainers(container):
    n = len(container)
    
    capacidades = [0] * n
    for i in range(n):
        soma_linha = 0
        for j in range(n):
            soma_linha += container[i][j]
        capacidades[i] = soma_linha

    quantidades_tipo = [0] * n
    for j in range(n):
        soma_coluna = 0
        for i in range(n):
            soma_coluna += container[i][j]
        quantidades_tipo[j] = soma_coluna

    visitado_tipo = [False] * n
    
    for i in range(n):
        achou_correspondente = False
        for j in range(n):
            if capacidades[i] == quantidades_tipo[j] and not visitado_tipo[j]:
                visitado_tipo[j] = True
                achou_correspondente = True
                break
        
        if not achou_correspondente:
            return "Impossible"
            
    return "Possible"
