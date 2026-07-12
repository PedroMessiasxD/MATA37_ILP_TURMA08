def OrganizandoContêiners(contêiner):
    x = len(contêiner)
    capacidades = []
    for y in range(x):
        soma_linha = 0
        for z in range(x):
            soma_linha += contêiner[y][z]
        capacidades.append(soma_linha)    
    quantidades_tipo = []
    for z in range(x):
        soma_coluna = 0
        for y in range(x):
            soma_coluna += contêiner[y][z]
        quantidades_tipo.append(soma_coluna)       
    usado = []
    for _ in range(x):
        usado.append(False)       
    match_count = 0
    for y in capacidades:
        for z in range(x):
            if not usado[z] and y == quantidades_tipo[z]:
                usado[z] = True
                match_count += 1
                break             
    if match_count == x:
        return "Possible"
    else:
        return "Impossible"
q = int(input("Digite a quantidade de consultas: "))
for _ in range(q):
    print("\n--- Nova Consulta ---")
    x = int(input("Digite o tamanho da matriz: "))  
    if not (1 <= x <= 100):
        print("Tamanho inválido! Deve estar entre 1 e 100.")
        for _ in range(x):
            input("Apenas dê Enter para ignorar esta linha: ")
        print("Impossible")
        continue     
    matriz_M = []
    print(f"Digite as linhas da matriz (separe os números por espaço):")
    for y in range(x):
        linha_str = input(f"Linha {y}: ").split()
        linha_inteiros = []
        for z in linha_str:
            linha_inteiros.append(int(z))
        matriz_M.append(linha_inteiros)  
    resultado = OrganizandoContêiners(matriz_M)
    print(OrganizandoContêiners(matriz_M))