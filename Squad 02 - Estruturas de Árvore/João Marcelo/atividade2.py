def soma_array(ar):
    soma = 0

    for numero in ar:
        soma = soma + numero

    return soma


# Exemplo de uso
ar = [1, 2, 3, 4, 10, 11]

resultado = soma_array(ar)
print(resultado)
