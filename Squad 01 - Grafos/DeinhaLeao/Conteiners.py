def validar_organizacao_conteiners(matriz, n):

    capacidade_container = []
    quantidade_tipo = []

    for linha in matriz:
        soma = 0

        for valor in linha:
            soma += valor

        capacidade_container.append(soma)

    for coluna in range(n):
        soma = 0

        for linha in range(n):
            soma += matriz[linha][coluna]

        quantidade_tipo.append(soma)

    capacidade_container.sort()
    quantidade_tipo.sort()

    if capacidade_container == quantidade_tipo:
        return "Possible"

    return "Impossible"


# ==================================================
# Programa Principal
# ==================================================

if __name__ == '__main__':
    print("************************************************")
    print("")
    print("Programa para controlar conteiners de bolas.")
    print("")
    print("************************************************")
    
    while True:        
        try:
            qtd_conteiners = int(input("Informe a quantidade de conteiners: "))
            qtd_cores = int(input("Informe a quantidade de cores que pode ter nos conteiners: "))
            matriz_conteiners = []
              
            if 1 >= qtd_conteiners or qtd_conteiners > 10:                
                print("Erro: a quantidade de conteiner deve estar entre 2 e 10 unidades.\n") 
            
            elif 1 >= qtd_cores or qtd_cores > 100:                
                print("Erro: a quantidade de conteiner deve estar entre 2 e 10 unidades.\n") 

            else:                
                for conteiner in range(qtd_conteiners):
                    print(f"Dados conteiner {conteiner + 1}: informe {qtd_cores} números separados por espaço:\n") 
                    
                    while True:
                        try:

                            valores = list(map(int, input().split()))

                            if len(valores) != qtd_cores:
                                print(f"Digite exatamente {qtd_cores} números separados por espaço.\n")
                            else:
                                matriz_conteiners.append(valores)
                                break
                        
                        except ValueError:                            
                            print("Erro: informe apenas números inteiros separados por espaço.")
                            continue

                resultado = validar_organizacao_conteiners(matriz_conteiners, qtd_cores)
                print(f"Resultado: {resultado}\n")

            print("")
            opcao = input("\nPressione ENTER para nova soma ou digite 'S' para sair: ").strip()

            if opcao.upper() == "S" or opcao == "\x1b":
                print("Fim do programa.")
                break

        except ValueError:
            print("Erro: informe apenas números inteiros.")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")

