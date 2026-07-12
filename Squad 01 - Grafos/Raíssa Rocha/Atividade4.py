# Programa para organizar contêineres de bolas
# Ideia: somar cada linha e cada coluna, ordenar e comparar

q = int(input())

for consulta in range(q):
    n = int(input())
    
    # lendo a matriz
    matriz = []
    for i in range(n):
        linha = input().split()
    
        linha_numeros = []
        for valor in linha:
            linha_numeros.append(int(valor))
        matriz.append(linha_numeros)
    
    
    soma_linhas = []
    for i in range(n):
        soma = 0
        for j in range(n):
            soma = soma + matriz[i][j]
        soma_linhas.append(soma)
    
    
    soma_colunas = []
    for j in range(n):
        soma = 0
        for i in range(n):
            soma = soma + matriz[i][j]
        soma_colunas.append(soma)
    
    
    # ordenando soma_linhas
    for i in range(n):
        for j in range(n - 1):
            if soma_linhas[j] > soma_linhas[j + 1]:
                # troca de posição
                aux = soma_linhas[j]
                soma_linhas[j] = soma_linhas[j + 1]
                soma_linhas[j + 1] = aux
    
   
    for i in range(n):
        for j in range(n - 1):
            if soma_colunas[j] > soma_colunas[j + 1]:
                # troca de posição
                aux = soma_colunas[j]
                soma_colunas[j] = soma_colunas[j + 1]
                soma_colunas[j + 1] = aux
    
    
    igual = True
    for i in range(n):
        if soma_linhas[i] != soma_colunas[i]:
            igual = False
    
    # imprimindo o resultado
    if igual == True:
        print("Possible")
    else:
        print("Impossible")
