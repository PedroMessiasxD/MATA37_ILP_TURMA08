using System;

class Program
{
    static void Main()
    {
        int quantidade = int.Parse(Console.ReadLine());

        for (int x = 0; x < quantidade; x++)
        {
            string palavra = Console.ReadLine();
            Console.WriteLine(ProximaPalavra(palavra));
        }
    }

    static string ProximaPalavra(string palavra)
    {
        char[] letras = palavra.ToCharArray();

        int posicao = -1;

        for (int i = letras.Length - 2; i >= 0; i--)
        {
            if (letras[i] < letras[i + 1])
            {
                posicao = i;
                break;
            }
        }

        if (posicao == -1)
        {
            return "no answer";
        }

        for (int i = letras.Length - 1; i > posicao; i--)
        {
            if (letras[i] > letras[posicao])
            {
                char aux = letras[i];
                letras[i] = letras[posicao];
                letras[posicao] = aux;
                break;
            }
        }

        int inicio = posicao + 1;
        int fim = letras.Length - 1;

        while (inicio < fim)
        {
            char aux = letras[inicio];
            letras[inicio] = letras[fim];
            letras[fim] = aux;

            inicio++;
            fim--;
        }

        return new string(letras);
    }
}
