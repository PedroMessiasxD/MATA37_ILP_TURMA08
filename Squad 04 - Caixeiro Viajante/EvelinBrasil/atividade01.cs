/*
 * Atividade 1 ->  Simples = 1 ponto
Construa uma função para calcular a soma de dois números inteiros.

Exemplo
a = 7

b = 3

Retorne 10.

Descrição da função
Complete a função com os seguintes parâmetros:

int a: o primeiro valor

int b: o segundo valor

Retorno
int: a soma de a e b

Restrições
1 ≤ a, b ≤ 1000

Entrada de exemplo
a = 2
b = 3
Saída de exemplo
5
Explicação
2 + 3 = 5.
*/

int a, b, soma;

a = int.Parse(Console.ReadLine());
b = int.Parse(Console.ReadLine());

soma = a + b;

if (a >= 1 && a <= 1000 && b >= 1 && b <= 1000)
{
    Console.WriteLine(soma);
}
else
{
    Console.WriteLine("Valores inválidos.");
}
