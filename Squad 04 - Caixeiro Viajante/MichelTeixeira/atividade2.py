def soma_array_monstra(ar):
    soma = 0

    for i in range(len(ar)):
        soma = soma + ar[i]

    return soma


print("Digite o tamanho do array:")
n = int(input())

if n <= 0:
    print("Erro: o tamanho do array deve ser maior que 0.")
else:
    print(f"Digite {n} números separados por espaço:")
    entrada = input().split()

    if len(entrada) != n:
        print(f"Erro: você deve digitar exatamente {n} números.")
    else:
        ar = []
        entrada_valida = True

        for i in range(n):
            numero = int(entrada[i])

            if numero <= 0 or numero > 1000:
                entrada_valida = False

            ar.append(numero)

        if entrada_valida == False:
            print("Erro: todos os números devem estar entre 1 e 1000.")
        else:
            resultado = soma_array_monstra(ar)

            print("A soma dos elementos do array é:")
            print(resultado)