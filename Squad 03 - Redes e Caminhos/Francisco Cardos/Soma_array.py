def somar_com_tamanho_fixo():
    # 1. Perguntamos o tamanho do "array" (lista)
    resposta_tamanho = input("Quantos números você vai querer digitar? ")
    tamanho = int(resposta_tamanho)
    
    # Começamos a soma zerada
    soma_total = 0
    
    print(f"\nPerfeito! Agora digite os {tamanho} números, um por um:")
    print("-" * 30)
    
    # 2. O laço 'for' vai rodar exatamente o número de vezes definido no 'tamanho'
    for i in range(tamanho):
        # Pedimos o número (o 'i + 1' serve só para mostrar '1º número', '2º número' na tela)
        entrada = input(f"Digite o {i + 1}º número: ")
        numero = int(entrada)
        
        # 3. Aplicamos a sua regra (entre 1 e 1000)
        if numero >= 1 and numero <= 1000:
            soma_total = soma_total + numero
            print(f"-> {numero} guardado!")
        else:
            print(f"-> {numero} ignorado (fora do intervalo de 1 a 1000).")
            
    # 4. Mostramos o resultado final depois que o laço terminar
    print("-" * 30)
    print("A soma total dos números válidos é:", soma_total)

# Executa a função
somar_com_tamanho_fixo()
