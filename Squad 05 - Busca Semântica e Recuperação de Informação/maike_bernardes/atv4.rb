def bubble_sort(vetor)
    n = vetor.length

    i = 0
    while i < n - 1
        j = 0
        while j < n - i - 1
            if vetor[j] > vetor[j + 1]
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
            end
            j += 1
        end
        i += 1
    end
end

def organizingContainers(containers)
    n = containers.length

    soma_containers = Array.new(n, 0)
    soma_tipos = Array.new(n, 0)

    i = 0
    while i < n
        j = 0
        while j < n
            soma_containers[i] += containers[i][j]
            soma_tipos[j] += containers[i][j]
            j += 1
        end
        i += 1
    end

    bubble_sort(soma_containers)
    bubble_sort(soma_tipos)

    i = 0
    while i < n
        if soma_containers[i] != soma_tipos[i]
            return "Impossible"
        end
        i += 1
    end

    return "Possible"
end

# Programa principal

q = gets.to_i

consulta = 0
while consulta < q
    n = gets.to_i

    containers = []

    i = 0
    while i < n
        linha = gets.split.map(&:to_i)
        containers << linha
        i += 1
    end

    puts organizingContainers(containers)

    consulta += 1
end

