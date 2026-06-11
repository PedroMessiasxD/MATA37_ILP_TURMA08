#!/bin/python3

import math
import os
import random
import re
import sys


from dotenv import load_dotenv

load_dotenv()

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    intTotal = 0
    
    for valor in ar:
        intTotal = intTotal + valor
    
    return intTotal
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print("************************************************")
    print("")
    print("Programa para somar itens de um array")
    print("")
    print("************************************************")

    while True:
        try:
            print("Informe quantos números quer somar:")
            ar_count = int(input().strip())
            print("")
            
            print(f"Informe os números {ar_count} números a serem somados separados por espaço:")
            ar = list(map(int, input().rstrip().split()))
            print("")

            result = simpleArraySum(ar)

            print("A soma de todos os números inormados é: " + str(result) + '\n')

            fptr.write(str(result) + '\n')

            fptr.close()

            opcao = input("\nPressione ENTER para nova soma ou digite 'S' para sair: ").strip()

            if opcao.upper() == "S" or opcao == "\x1b":
                print("Fim do programa.")
                break

        except ValueError:
                print("Erro: informe apenas números inteiros separados por espaço.")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")
