def simpleArraySum(ar):
    total_soma = 0
    for numero in ar:
        total_soma = total_soma + numero
    return total_soma

n = int(input())
ar = list(map(int, input().split()))