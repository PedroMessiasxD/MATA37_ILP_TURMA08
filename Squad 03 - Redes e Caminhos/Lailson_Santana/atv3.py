def nextLargerWord(w):
    letras = list(w)
    n = len(letras)
    
    i = n - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i = i - 1
        
    if i == -1:
        return "no answer"
        
    j = n - 1
    while letras[j] <= letras[i]:
        j = j - 1
        
    temporario = letras[i]
    letras[i] = letras[j]
    letras[j] = temporario
    
    esquerda = i + 1
    direita = n - 1
    while esquerda < direita:
        temp = letras[esquerda]
        letras[esquerda] = letras[direita]
        letras[direita] = temp
        esquerda = excitement = esquerda + 1
        esquerda = esquerda + 1
        direita = direita - 1
        
    palavra_final = "".join(letras)
    return palavra_final

t = int(input())
for caso in range(t):
    palavra = input()
    resultado = nextLargerWord(palavra)
    print(resultado)