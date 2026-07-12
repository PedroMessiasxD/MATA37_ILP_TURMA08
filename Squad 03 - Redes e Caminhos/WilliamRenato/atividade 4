def organizingContainers(container):
    a = []
    b = []
    
    tamanho = 0
    for x in container:
        tamanho += 1
        
    i = 0
    while i < tamanho:
        a.append(0)
        b.append(0)
        i += 1
        
    for x in range(tamanho):
        for y in range(tamanho):
            a[x] = a[x] + container[x][y]
            
    for x in range(tamanho):
        for y in range(tamanho):
            b[y] = b[y] + container[x][y]
            
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if a[j] > a[j + 1]:
                aux = a[j]
                a[j] = a[j + 1]
                a[j + 1] = aux
                
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if b[j] > b[j + 1]:
                aux = b[j]
                b[j] = b[j + 1]
                b[j + 1] = aux
                
    resultado_final = True
    for idx in range(tamanho):
        if a[idx] != b[idx]:
            resultado_final = False
            
    if resultado_final == True:
        return "Possible"
    else:
        return "Impossible"
