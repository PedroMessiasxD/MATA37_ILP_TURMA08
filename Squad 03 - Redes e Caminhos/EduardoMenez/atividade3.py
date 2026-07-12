def SomaLex(w):
    palavras = []
    for letras in w:
        palavras.append(letras)
    n = len(palavras)
    x = n - 2
    while x >= 0 and palavras[x] >= palavras[x + 1]:
        x -= 1
    if x < 0:
        return "no answer"
    y = n - 1
    while palavras[y] <= palavras[x]:
        y -= 1
    pote = palavras[x]
    palavras[x] = palavras[y]
    palavras[y] = pote
    esquerda = x + 1
    direita = n - 1
    while esquerda < direita:
        pote = palavras[esquerda]
        palavras[esquerda] = palavras[direita]
        palavras[direita] = pote
        esquerda += 1
        direita -= 1
    palavra_final = ""
    for letras in palavras:
        palavra_final += letras
    return palavra_final
t = int(input("Quantos Testes?"))
for _ in range(t):
    w = input("Diga a palavra:")
    print(SomaLex(w))