using System;

class Result
{
    public static string organizingContainers(int[][] container)
    {
        int n = container.Length;

        long[] totalContainer = new long[n];
        long[] totalTipo = new long[n];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                totalContainer[i] += container[i][j];
                totalTipo[j] += container[i][j];
            }
        }

        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (totalContainer[j] > totalContainer[j + 1])
                {
                    long aux = totalContainer[j];
                    totalContainer[j] = totalContainer[j + 1];
                    totalContainer[j + 1] = aux;
                }
            }
        }

        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (totalTipo[j] > totalTipo[j + 1])
                {
                    long aux = totalTipo[j];
                    totalTipo[j] = totalTipo[j + 1];
                    totalTipo[j + 1] = aux;
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            if (totalContainer[i] != totalTipo[i])
            {
                return "Impossible";
            }
        }

        return "Possible";
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

                string[] entrada = Console.ReadLine().Split();

                for (int j = 0; j < n; j++)
                {
                    container[i][j] = int.Parse(entrada[j]);
                }
            }

            Console.WriteLine(Result.organizingContainers(container));

            q--;
        }
    }
}
