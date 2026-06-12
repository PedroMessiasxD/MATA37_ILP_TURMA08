while True:
    n = int(input("Digite a quantidade de números que você deseja na lista: "))
    if 0 < n <= 1000:
        break
    else:
        print("Erro: A quantidade (n) deve ser maior que 0 e menor ou igual a 1000.")

ar = []

for i in range(n):
    faltam = n - i
    
    while True:
        numero = int(input(f"Digite 1 numero (faltam {faltam}): "))
        if 0 < numero <= 1000:
            break
        else:
            print("Erro")
            
    ar = ar + [numero]

SomaTotal = 0
for x in ar:
    SomaTotal = SomaTotal + x

print(f"A soma dos {n} números digitados é: {SomaTotal}")

