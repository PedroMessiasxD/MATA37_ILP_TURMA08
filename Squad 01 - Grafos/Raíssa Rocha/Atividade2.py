def soma_array(ar):
    soma = 0
    for i in ar: 
        soma = soma + i
    return soma
n = int(input())
elementos = list(map(int, input().split()))
elementos = elementos[:n]
print(soma_array(elementos))
