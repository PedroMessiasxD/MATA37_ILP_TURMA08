def proxima_maior_palavra(w):
    
    letras = []
    for caractere in w:
        letras.append(caractere)
        
    n = len(letras)
    
    
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1
        
   
    if i == -1:
        return "no answer"
        
    
    j = n - 1
    while letras[j] <= letras[i]:
        j -= 1
        
    
    temp = letras[i]
    letras[i] = letras[j]
    letras[j] = temp
    
    esquerda = i + 1
    direita = n - 1
    while esquerda < direita:
        temp = letras[esquerda]
        letras[esquerda] = letras[direita]
        letras[direita] = temp
        esquerda += 1
        direita -= 1
        

    resultado = ""
    for caractere in letras:
        resultado += caractere
        
    return resultado

casos_teste = ["ab", "bb", "hefg", "dhck", "dkhc"]

print("Resultados:")
for palavra in casos_teste:
    print(f"{palavra} -> {proxima_maior_palavra(palavra)}")