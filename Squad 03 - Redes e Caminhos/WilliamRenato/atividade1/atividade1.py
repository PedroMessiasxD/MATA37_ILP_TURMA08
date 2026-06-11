def soma(x, y):
    if x < 1 or x > 1000 or y < 1 or y > 1000:
        print("ERRO OS VALORES DEVEM ESTAR ENTRE 1 E 1000")
        return 0        
    res = x + y
    return res
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

resultado_final = soma(a, b)
print("Resultado da soma:", resultado_final)