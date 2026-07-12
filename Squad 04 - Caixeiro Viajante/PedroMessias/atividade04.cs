using System;

class Result
{
    static void BubbleSort(long[] vetor)
    {
        int n = vetor.Length;

        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (vetor[j] > vetor[j + 1])
                {
                    long aux = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = aux;
                }
            }
        }
    }

    static bool VetoresIguais(long[] a, long[] b)
    {
        for (int i = 0; i < a.Length; i++)
        {
            if (a[i] != b[i])
                return false;
        }

        return true;
    }

    public static string organizingContainers(int[][] container)
    {
        int n = container.Length;

        long[] capacidadeContainer = new long[n];
        long[] quantidadeTipo = new long[n];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                capacidadeContainer[i] += container[i][j];
                quantidadeTipo[j] += container[i][j];
            }
        }

        BubbleSort(capacidadeContainer);
        BubbleSort(quantidadeTipo);

        if (VetoresIguais(capacidadeContainer, quantidadeTipo))
            return "Possible";

        return "Impossible";
    }
}

class Solution
{
    static void Main()
    {
        int q = int.Parse(Console.ReadLine());

        while (q > 0)
        {
            int n = int.Parse(Console.ReadLine());

            int[][] container = new int[n][];

            for (int i = 0; i < n; i++)
            {
                container[i] = new int[n];

                string[] valores = Console.ReadLine().Split();

                for (int j = 0; j < n; j++)
                {
                    container[i][j] = int.Parse(valores[j]);
                }
            }

            Console.WriteLine(Result.organizingContainers(container));

            q--;
        }
    }
}
