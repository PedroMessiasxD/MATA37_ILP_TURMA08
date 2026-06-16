def somar_array(ar)
  soma = 0
  indice = 0
  tamanho = ar.length

  # Laço de repetição que percorre o array elemento por elemento
  while indice < tamanho
    # Validação da restrição do elemento (0 < ar[i] <= 1000)
    if ar[indice] <= 0 || ar[indice] > 1000
      puts "Aviso: O elemento no índice #{indice} quebra as restrições."
    end

    # Soma o elemento atual à variável acumuladora
    soma = soma + ar[indice]
    
    # Incrementa o índice para avançar no array
    indice = indice + 1
  end

  return soma
end

# --- Simulando a Entrada de Dados (STDIN) ---

# tamanho do array (n)
n = 6 

# Elementos separados por espaço (convertidos em um array de inteiros)
entrada_elementos = "1 2 3 4 10 11"
array_dados = entrada_elementos.split(" ").map { |x| x.to_i }

# Validação da restrição do tamanho n (0 < n <= 1000)
if n > 0 && n <= 1000 && array_dados.length == n
  # Executa a função e exibe o resultado
  resultado = somar_array(array_dados)
  puts "Saída de exemplo:"
  puts resultado # Saída esperada: 31
else
  puts "Tamanho do array inválido."
end

