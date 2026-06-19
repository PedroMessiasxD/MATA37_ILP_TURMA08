def proxima_palavra(w):
    letras = list(w)
    
    # Encontrar o primeiro caractere que quebra a ordem crescente
    i = len(letras) - 1
    while i > 0 and letras[i - 1] >= letras[i]:
        i -= 1
        
    if i == 0:
        return "no answer"
        
    # Encontrar o menor caractere à direita maior que letras[i-1]
    j = len(letras) - 1
    while letras[j] <= letras[i - 1]:
        j -= 1
        
    # Trocar de lugar
    letras[i - 1], letras[j] = letras[j], letras[i - 1]
    
    # Inverter o resto da lista usando slicing e juntar em texto
    letras[i:] = letras[i:][::-1]
    
    return "".join(letras)

T = int(input())

# Roda o código T vezes
for _ in range(T):
    w = input().strip() # O .strip() garante que não venham espaços acidentais
    print(proxima_palavra(w))