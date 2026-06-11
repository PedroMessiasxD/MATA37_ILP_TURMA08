def soma_dos_dois_numeros(a, b):
    return a + b

print("Digite dois números inteiros entre 1 e 1000 para serem somados.")

a = int(input("Digite o primeiro número: "))
while a < 1 or a > 1000:
    a = int(input("Valor fora do intervalo. Digite entre 1 e 1000: "))

b = int(input("Digite o segundo número: "))
while b < 1 or b > 1000:
    b = int(input("Valor fora do intervalo. Digite entre 1 e 1000: "))

c = soma_dos_dois_numeros(a, b)
print(f"O resultado é: {c}")