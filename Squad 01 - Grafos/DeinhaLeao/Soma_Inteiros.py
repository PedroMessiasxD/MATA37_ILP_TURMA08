#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

  

if __name__ == '__main__':
    intTotal = 0

    print("************************************************")
    print("")
    print("Programa para somar dois números inteiros")
    print("")
    print("************************************************")

    while True:
        try:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))

            intTotal = a + b

            print(f"Total soma inteiros: {intTotal}")

            opcao = input("\nPressione ENTER para nova soma ou digite 'S' para sair: ").strip()

            if opcao.upper() == "S" or opcao == "\x1b":
                print("Fim do programa.")
                break
            
        except ValueError:
            print("Erro: informe apenas números inteiros.")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")
        
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            break
        
        

    

    

    
    

