# Atividade 01 - Matheus dos Santos.

# Criando função de soma.
def soma(a, b):
    result = a + b
    return result

# Pedindo os inputs para o user.
a = int(input("Digite o primeiro número (entre 1 e 1000):"))
b = int(input("Digite o primeiro número (entre 1 e 1000):"))

# Verificando as restrições com 'if' e 'else'.
if a < 1 or a > 1000 or b < 1 or b > 1000:
    print("Erro! Os números devem ser maiores ou iguais a 1 e menores ou iguais a 1000.")
else:
    # Segue o baile.
    resultado_final = soma(a, b)
    print("O resultado da soma é:", resultado_final)