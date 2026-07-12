# Função que recebe um array e devolve a soma dos elementos
def soma_array(ar):

    # A gente cria uma variável para guardar o resultado da soma.
    # Começa em 0 porque ainda não somamos nada.
    soma = 0

    # O for percorre o array inteiro.
    # A cada repetição, o numero recebe um valor do array.
    for numero in ar:

        # Pegamos o valor que já estava acumulado
        # e adicionamos o número atual.
        soma = soma + numero

    # Depois que o for termina
    # retornamos o valor final acumulado.
    return soma


# Lê o tamanho do array
n = int(input())

# Lê os números digitados e transforma em lista
ar = list(map(int, input().split()))

# Chama a função e dá o resultado
print(soma_array(ar))
