using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());

        string[] numeros = Console.ReadLine().Split(' ');

        int soma = 0;

        for (int i = 0; i < n; i++)
        {
            soma = soma + int.Parse(numeros[i]);
        }

        Console.WriteLine(soma);
    }
}
