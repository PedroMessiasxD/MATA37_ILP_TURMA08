def proxima_palavra(w):
    
    s = list(w)
    n = len(s)

     
    i = n - 2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1

    # Se não existe, não há resposta
    if i < 0:
        return "no answer"

     
    j = n - 1
    while s[j] <= s[i]:
        j -= 1

    # 3. Trocar s[i] e s[j]
    s[i], s[j] = s[j], s[i]

     
    esquerda = i + 1
    direita = n - 1
    while esquerda < direita:
        s[esquerda], s[direita] = s[direita], s[esquerda]
        esquerda += 1
        direita -= 1

    return ''.join(s)


 
T = int(input().strip())
for _ in range(T):
    w = input().strip()
    print(proxima_palavra(w))
