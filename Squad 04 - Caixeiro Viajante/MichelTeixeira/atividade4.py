# Atividade 4 - Organizing Containers
#
# Ideia central:
# Em cada troca, um contêiner perde uma bola e ganha outra.
# Portanto, o total de bolas dentro de cada contêiner nunca muda.
#
# Além disso, a quantidade total de cada tipo de bola também nunca muda.
#
# No final, cada contêiner precisa guardar apenas um tipo de bola.
# Então, para ser possível, cada capacidade de contêiner precisa ser igual
# à quantidade total de algum tipo de bola.
#
# Por isso, comparamos manualmente:
# - soma de cada linha: total de bolas em cada contêiner;
# - soma de cada coluna: total de bolas de cada tipo.

def organizingContainers(container):
    n = len(container)

    # Soma de cada linha = total de bolas em cada contêiner.
    total_por_container = [0] * n

    i = 0
    while i < n:
        j = 0
        while j < n:
            total_por_container[i] += container[i][j]
            j += 1
        i += 1

    # Soma de cada coluna = total de bolas de cada tipo.
    total_por_tipo = [0] * n

    j = 0
    while j < n:
        i = 0
        while i < n:
            total_por_tipo[j] += container[i][j]
            i += 1
        j += 1

    # Agora fazemos o casamento manual entre os totais.
    # Cada contêiner precisa encontrar um tipo de bola com a mesma quantidade.
    # Um mesmo tipo não pode ser usado para dois contêineres diferentes.
    tipos_usados = [False] * n

    i = 0
    while i < n:
        encontrou = False
        j = 0

        while j < n:
            if tipos_usados[j] == False and total_por_container[i] == total_por_tipo[j]:
                tipos_usados[j] = True
                encontrou = True
                break

            j += 1

        if encontrou == False:
            return "Impossible"

        i += 1

    return "Possible"


# Leitura no formato do enunciado:
# Primeira linha: q, quantidade de consultas.
# Para cada consulta:
# - uma linha com n;
# - depois n linhas com n inteiros cada.

q = int(input())

consulta = 0

while consulta < q:
    n = int(input())

    container = []

    i = 0
    while i < n:
        valores_texto = input().split()

        linha = []

        j = 0
        while j < n:
            numero = int(valores_texto[j])
            linha.append(numero)
            j += 1

        container.append(linha)

        i += 1

    resultado = organizingContainers(container)
    print(resultado)

    consulta += 1
