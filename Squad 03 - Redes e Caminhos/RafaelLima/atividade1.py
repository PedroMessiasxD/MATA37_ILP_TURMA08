def soma(a, b):
    return a + b

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))

if 1 <= a <= 1000 and 1 <= b <= 1000:
    resultado = soma(a,b)
    print(resultado)
else:
    print('Os valores devem estar entre 1 e 1000.')