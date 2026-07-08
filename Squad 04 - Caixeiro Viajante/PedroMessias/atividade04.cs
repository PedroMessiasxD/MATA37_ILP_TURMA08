using System;
using System.Linq;

class Result
{
    public static string organizingContainers(int[][] container)
    {
        int n = container.Length;

        long[] containers = new long[n];
        long[] types = new long[n];

        for (int i = 0; i < n; i++)
        {
            containers[i] = container[i].Sum(x => (long)x);

            for (int j = 0; j < n; j++)
            {
                types[j] += container[i][j];
            }
        }

        Array.Sort(containers);
        Array.Sort(types);

        return containers.SequenceEqual(types)
            ? "Possible"
            : "Impossible";
    }
}

class Solution
{
    static void Main()
    {
        int q = int.Parse(Console.ReadLine());

        while (q-- > 0)
        {
            int n = int.Parse(Console.ReadLine());

            int[][] container = new int[n][];

            for (int i = 0; i < n; i++)
            {
                container[i] = Console.ReadLine()
                    .Split()
                    .Select(int.Parse)
                    .ToArray();
            }

            Console.WriteLine(Result.organizingContainers(container));
        }
    }
}
