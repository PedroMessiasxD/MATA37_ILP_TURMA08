def soma(numero01, numero02):
    resultado = numero01 + numero02
    return resultado


while True:
    try:
        numero01 = int(input("Digite o primeiro número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

while True:
    try:
        numero02 = int(input("Digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

resultado = soma(numero01, numero02)

print(f"A soma dos números é {resultado}")

