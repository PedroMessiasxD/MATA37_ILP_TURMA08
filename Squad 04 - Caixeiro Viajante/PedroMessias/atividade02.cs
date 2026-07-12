/*Atividade 2 -> Simples = 1 ponto
Dado um array de inteiros, encontre a soma de seus elementos.

Por exemplo, se o array ar = [1, 2, 3], então 1 + 2 + 3 = 6; portanto, retorne 6.

Descrição da função
Construa uma função com o seguinte parâmetro:

ar[n]: um array de inteiros

Retorno
int: a soma dos elementos do array

Formato de entrada
A primeira linha contém um inteiro, n, indicando o tamanho do array.

A segunda linha contém n inteiros separados por espaço, representando os elementos do array.

Restrições
0 < n, ar[i] ≤ 1000

Entrada de exemplo
STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]
Saída de exemplo
31
Explicação
Imprima a soma dos elementos do array: 1 + 2 + 3 + 4 + 10 + 11 = 31.Atividade 2 -> Simples = 1 ponto
Dado um array de inteiros, encontre a soma de seus elementos.

Por exemplo, se o array ar = [1, 2, 3], então 1 + 2 + 3 = 6; portanto, retorne 6.

Descrição da função
Construa uma função com o seguinte parâmetro:

ar[n]: um array de inteiros

Retorno
int: a soma dos elementos do array

Formato de entrada
A primeira linha contém um inteiro, n, indicando o tamanho do array.

A segunda linha contém n inteiros separados por espaço, representando os elementos do array.

Restrições
0 < n, ar[i] ≤ 1000

Entrada de exemplo
STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]
Saída de exemplo
31
Explicação
Imprima a soma dos elementos do array: 1 + 2 + 3 + 4 + 10 + 11 = 31.
*/


static int SomaArray(int[] ar)
{
    int soma = 0;

    for (int i = 0; i < ar.Length; i++)
    {
        soma += ar[i];
    }

    return soma;
}

int n = int.Parse(Console.ReadLine());

string[] entrada = Console.ReadLine().Split(' ');
int[] ar = new int[n];

for (int i = 0; i < n; i++)
{
    ar[i] = int.Parse(entrada[i]);
}

int resultado = SomaArray(ar);
Console.WriteLine(resultado);
