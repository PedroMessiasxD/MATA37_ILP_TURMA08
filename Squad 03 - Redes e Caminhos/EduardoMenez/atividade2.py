def SomaDosArray(array):
    soma_total = 0
    for numero in array:
        soma_total = soma_total + numero
    return soma_total
n = int(input("Qual o tamanho do Array?"))
linha_numeros = input("Digite os números do Array:")
lista_strings = linha_numeros.split()
array = []
for i in range(n):
    numero_inteiro = int(lista_strings[i])
    array.append(numero_inteiro) 
print(SomaDosArray(array))