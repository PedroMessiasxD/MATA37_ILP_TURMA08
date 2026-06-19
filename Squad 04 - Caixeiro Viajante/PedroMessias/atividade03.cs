using System;

class Program
{
    static void Main()
    {
        int t = int.Parse(Console.ReadLine());

        for (int i = 0; i < t; i++)
        {
            string palavra = Console.ReadLine();
            Console.WriteLine(ProximaPalavra(palavra));
        }
    }

    static string ProximaPalavra(string w)
    {
        char[] letras = w.ToCharArray();

        int i = letras.Length - 2;

        while (i >= 0 && letras[i] >= letras[i + 1])
        {
            i--;
        }

        if (i < 0)
        {
            return "no answer";
        }

        int j = letras.Length - 1;

        while (letras[j] <= letras[i])
        {
            j--;
        }

        char temp = letras[i];
        letras[i] = letras[j];
        letras[j] = temp;

        int inicio = i + 1;
        int fim = letras.Length - 1;

        while (inicio < fim)
        {
            temp = letras[inicio];
            letras[inicio] = letras[fim];
            letras[fim] = temp;

            inicio++;
            fim--;
        }

        return new string(letras);
    }
}
