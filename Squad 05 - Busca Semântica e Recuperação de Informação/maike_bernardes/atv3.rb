def proxima_permissao(w)
    # Convertemos a string em um array de caracteres para manipular por índice
    caracteres = w.chars
    n = caracteres.length

    # Encontrar o primeiro elemento (pivô) que é menor que o seu sucessor
    i = n - 2
    while i >= 0 && caracteres[i] >= caracteres[i + 1]
        i -= 1
    end

    # Se não encontramos nenhum pivô, significa que a string já está na maior ordem possível
    return "no answer" if i < 0

    # Encontrar o elemento à direita de 'i' que seja o menor caractere maior que caracteres[i]
    j = n - 1
    while caracteres[j] <= caracteres[i]
        j -= 1
    end

    # Trocar os elementos dos índices i e j
    temp = caracteres[i]
    caracteres[i] = caracteres[j]
    caracteres[j] = temp

    # Inverter manualmente os elementos à direita do índice i
    esquerda = i + 1
    direita = n - 1
    while esquerda < direita
        temp_inv = caracteres[esquerda]
        caracteres[esquerda] = caracteres[direita]
        caracteres[direita] = temp_inv
        esquerda += 1
        direita -= 1
    end

    # o array de caracteres de volta para uma string
    return caracteres.join
end

# Casos

puts "--- Resultados Entrada de Exemplo 0 ---"
casos_0 = ["ab", "bb", "hefg", "dhck", "dkhc"]
casos_0.each { |w| puts "#{w} -> #{proxima_permissao(w)}" }

puts "\n--- Resultados Entrada de Exemplo 1 ---"
casos_1 = ["lmno", "dcba", "dcbb", "abdc", "abcd", "fedcbabcd"]
casos_1.each { |w| puts "#{w} -> #{proxima_permissao(w)}" }
