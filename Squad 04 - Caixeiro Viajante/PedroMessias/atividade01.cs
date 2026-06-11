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

static int Soma(int a, int b)
{
    return a + b;
}

int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());

if (a >= 1 && a <= 1000 && b >= 1 && b <= 1000)
{
    Console.WriteLine(Soma(a, b));
}
else
{
    Console.WriteLine("Valores inválidos.");
}
