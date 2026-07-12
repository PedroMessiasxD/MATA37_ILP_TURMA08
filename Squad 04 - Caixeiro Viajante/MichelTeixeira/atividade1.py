def soma_dos_dois_numeros(a, b):
    soma = a + b
    return soma


def ler_numero_valido():
    numero = int(input())

    while numero < 1 or numero > 1000:
        numero = int(input())

    return numero


a = ler_numero_valido()
b = ler_numero_valido()

resultado = soma_dos_dois_numeros(a, b)

print(resultado)