def soma_array(arr):
    soma = 0

    for i in range(len(arr)):
        soma = soma + arr[i]

    return soma


arr = [1, 2, 3, 4, 10, 11]
print(soma_array(arr))