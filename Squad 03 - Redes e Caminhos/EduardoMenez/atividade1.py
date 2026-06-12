def soma(a, b): 
    if not (1 <= a <= 1000) or not (1 <= b <= 1000): 
        raise ValueError("Os números devem estar entre 1 e 1000")
    while b > 0: 
        a += 1 
        b -= 1
    return a    
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))    
print(soma(a, b))