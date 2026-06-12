def somar_a_e_b():
    print("--- Soma Simples de A e B ---")
    
   
    entrada_a = input("Digite o valor de A: ")
    entrada_b = input("Digite o valor de B: ")
    
    
    a = int(entrada_a)
    b = int(entrada_b)
    
    
    soma_total = 0
    s
   
    if a >= 1 and a <= 1000:
        soma_total = soma_total + a
    else:
        print("Aviso: O número A foi ignorado porque está fora do intervalo.")
        
  
    if b >= 1 and b <= 1000:
        soma_total = soma_total + b
    else:
        print("Aviso: O número B foi ignorado porque está fora do intervalo.")
        
    
    print("-" * 29)
    print("O resultado da soma manual é:", soma_total)


somar_a_e_b()
