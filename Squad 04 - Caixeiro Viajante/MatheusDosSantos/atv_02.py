# Função para somar.
def soma_array(ar):
    soma = 0
    # Passa por cada número dentro da lista e adiciona à soma
    for numero in ar:
        soma = soma + numero
    return soma

# 1. Lendo o tamanho do array.
n = int(input("Digite o tamanho do array (n): "))

# 2. Lendo os elementos do array
texto_array = input("Digite os elementos do array separados por espaço: ")
pedacos_texto = texto_array.split()

# Laço manual para preencher a lista
ar = []
for pedaco in pedacos_texto:
    ar.append(int(pedaco)) # Convertendo para inteiro e adicionando na lista

# 3. Mantendo a verificação manual de restrições
restricoes_atendidas = True

if n <= 0 or n > 1000:
    restricoes_atendidas = False

for numero in ar:
    if numero <= 0 or numero > 1000:
        restricoes_atendidas = False

# 4. Exibindo o resultado final
if restricoes_atendidas == False:
    print("Erro! O tamanho do array e os números devem ser maiores que 0 e menores ou iguais a 1000.")
else:
    resultado_final = soma_array(ar)
    print("A soma dos elementos é:", resultado_final)