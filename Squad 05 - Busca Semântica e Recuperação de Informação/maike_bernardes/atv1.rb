def somar_dois_inteiros(a, b)
  #(Garantir que 1 <= a, b <= 1000)
  if a < 1 || a > 1000 || b < 1 || b > 1000
    return "Os valores devem estar entre 1 e 1000."
  end

  resultado = a + b

  # Retorna o valor final
  return resultado
end

# Exemplos

# Exemplo 1 da descrição
print "Resultado do Exemplo 1 (7 + 3): "
puts somar_dois_inteiros(7, 3) # Saída: 10

# Exemplo 2 (Entrada de exemplo)
print "Resultado do Exemplo 2 (2 + 3): "
puts somar_dois_inteiros(2, 3) # Saída: 5
