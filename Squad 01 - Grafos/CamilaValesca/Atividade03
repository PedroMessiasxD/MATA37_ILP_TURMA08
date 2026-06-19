def proxima_maior_palavra(w):
    letras = list(w)
    n = len(letras)
    
    # 1. Encontrar o ponto de quebra
    i = n - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1
        
    if i == -1:
        return "no answer"
        
    # 2. Encontrar o substituto
    j = n - 1
    while letras[j] <= letras[i]:
        j -= 1
        
    # 3. Trocar
    temp = letras[i]
    letras[i] = letras[j]
    letras[j] = temp
    
    # 4. Inverter o sufixo
    esquerda = i + 1
    direita = n - 1
    while esquerda < direita:
        temp = letras[esquerda]
        letras[esquerda] = letras[direita]
        letras[direita] = temp
        esquerda += 1
        direita -= 1
        
    # Reconstruir a string manualmente
    palavra_final = ""
    for char in letras:
        palavra_final += char
        
    return palavra_final


print("=== Gerador de Próxima Palavra Lexicográfica ===")

t_input = input("Digite a quantidade de palavras que deseja testar: ")
t = int(t_input)

for k in range(t):
    palavra = input(f"Digite a palavra {k + 1}: ").strip()
    resultado = proxima_maior_palavra(palavra)
    print(f"Resultado: {resultado}")
    print("-" * 30)
