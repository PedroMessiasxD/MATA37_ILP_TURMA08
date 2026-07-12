def soma (a,b):
    if 1 <= a <= 1000 and 1 <= b <= 1000:
        resultado = a + b
        return resultado
    else:
        return "Erro"

total = soma(2,3)
print (F"O total da soma é {total}")
