


PENULTIMA_POSICAO = -2

def permuta_lexografica(palavra):
    
    letras = list(palavra)
    tamanho = len(letras)
    indice = tamanho + PENULTIMA_POSICAO

    while indice >= 0:

        if letras[indice] < letras[indice + 1]:
            break

        indice -= 1
    
    if indice < 0:
        return "no answer"

    troca = tamanho - 1

    while letras[troca] <= letras[indice]:
        troca -= 1

   
    letras[indice], letras[troca] = letras[troca], letras[indice]  
    parte_esquerda = letras[:indice + 1]
    parte_direita = letras[indice + 1:]
    parte_direita = ordenar(parte_direita)
    resultado = "".join(parte_esquerda + parte_direita)

    return resultado

def ordenar(lista):

    for i in range(len(lista)):

        indice_menor = i

        for j in range(i + 1, len(lista)):

            if lista[j] < lista[indice_menor]:
                indice_menor = j

        lista[i], lista[indice_menor] = (
            lista[indice_menor],
            lista[i]
        )

    return lista


if __name__ == '__main__':
    print("************************************************")
    print("")
    print("Programa para determinar a ordem lexicográfica de uma palavra.")
    print("")
    print("************************************************")
    
    while True:
        palavra = ""
        try:

            palavra = input("Informe uma palavra com tamanho entre 2 e 100000 caracteres: ")
            tamanho_palavra = len(palavra)
  
            if 2 > tamanho_palavra or tamanho_palavra > 100000:                
                print("Erro: informe uma palavra com tamanho entre 2 e 100000 caracteres.\n")                

            elif not palavra.isalpha():
                print("Erro: a palavra deve conter apenas letras.\n")

            else:
                palavra = palavra.lower()

                resultado = permuta_lexografica(palavra)

                print(f"Resultado: {resultado}\n")

            print("")
            opcao = input("\nPressione ENTER para nova soma ou digite 'S' para sair: ").strip()

            if opcao.upper() == "S" or opcao == "\x1b":
                print("Fim do programa.")
                break

        except ValueError:
            print("Erro: digite apenas palavras com tamanho entre 2 e 100000 caracteres.\n")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")


