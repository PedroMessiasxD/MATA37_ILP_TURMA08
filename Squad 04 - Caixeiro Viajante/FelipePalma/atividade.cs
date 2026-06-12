def somavalore(a: int, b: int):

    if 1 <= a <= 1000 and 1 <= b <= 1000:
        return a + b

    else:

         print("Os Valores de a ou b devem estar como numeros inteiros de 1-100 ")
         exit()



result_1 = somavalore(7, 3)
print(f"Exemplo 1 (7 + 3): {result_1}")


result_2 = somavalore(2, 3)
print(f"Exemplo 2 (2 + 3): {result_2}")
