def biggerIsGreater(w):
    aaaa = list(w)
    
    tamanho = 0
    for c in aaaa:
        tamanho += 1
        
    i = tamanho - 2
    while i >= 0 and aaaa[i] >= aaaa[i + 1]:
        i = i - 1
        
    if i == -1:
        flag = "no answer"
        return flag
        
    j = tamanho - 1
    while aaaa[j] <= aaaa[i]:
        j = j - 1
        
    aux = aaaa[i]
    aaaa[i] = aaaa[j]
    aaaa[j] = aux
    
    inicio = i + 1
    for x in range(inicio, tamanho):
        for y in range(inicio, tamanho - 1):
            if aaaa[y] > aaaa[y + 1]:
                temp = aaaa[y]
                aaaa[y] = aaaa[y + 1]
                aaaa[y + 1] = temp
                
    bbb = ""
    for char in aaaa:
        bbb = bbb + char
        
    return bbb
