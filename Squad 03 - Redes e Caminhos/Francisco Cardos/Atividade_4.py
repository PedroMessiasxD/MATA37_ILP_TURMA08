# Função para resolver o problema de organizar as bolas
def verificar_containers(matriz):
    n = len(matriz)
    
    # Criando listas vazias preenchidas com zero para guardar as somas
    capacidades = [0] * n
    totais_tipo = [0] * n
    
    # Somando as linhas e as colunas da matriz
    for i in range(n):
        for j in range(n):
            capacidades[i] = capacidades[i] + matriz[i][j]
            totais_tipo[j] = totais_tipo[j] + matriz[i][j]
            
    # Ordenando a lista de capacidades com Bubble Sort
    for i in range(n):
        for j in range(n - 1):
            if capacidades[j] > capacidades[j + 1]:
                aux = capacidades[j]
                capacidades[j] = capacidades[j + 1]
                capacidades[j + 1] = aux
                
    # Ordenando a lista de totais por tipo com Bubble Sort
    for i in range(n):
        for j in range(n - 1):
            if totais_tipo[j] > totais_tipo[j + 1]:
                aux = totais_tipo[j]
                totais_tipo[j] = totais_tipo[j + 1]
                totais_tipo[j + 1] = aux
                
    # Comparando se as duas listas ficaram exatamente iguais
    for i in range(n):
        if capacidades[i] != totais_tipo[i]:
            return "Impossible"
            
    return "Possible"


# --- PARTE PRINCIPAL DO PROGRAMA (LEITURA DOS DADOS) ---

q = int(input("Quantidade de testes: "))

for t in range(q):
    n = int(input("\nTamanho da matriz (N): "))
    
    matriz = []
    print(f"Digite as {n} linhas da matriz:")
    
    for i in range(n):
        linha_texto = input()
        
        # O split quebra o texto nos espaços, e o int() converte cada pedaço em número
        numeros = []
        for pedaco in linha_texto.split():
            numeros.append(int(pedaco))
            
        matriz.append(numeros)
        
    resultado = verificar_containers(matriz)
    print("Resultado:", resultado)
