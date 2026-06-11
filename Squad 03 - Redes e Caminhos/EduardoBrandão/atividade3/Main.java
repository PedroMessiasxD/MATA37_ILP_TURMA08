public static String biggerIsGreater(String palavra) {
    char[] letras = palavra.toCharArray();
    int indice = letras.length - 2;
    while (indice >= 0 && letras[indice] >= letras[indice + 1]) {
        indice--;
    }
    if (indice < 0) {
        return "no answer";
    }
    int posicaoTroca = letras.length - 1;
    while (letras[posicaoTroca] <= letras[indice]) {
        posicaoTroca--;
    }
    char auxiliar = letras[indice];
    letras[indice] = letras[posicaoTroca];
    letras[posicaoTroca] = auxiliar;
    int inicio = indice + 1;
    int fim = letras.length - 1;
    while (inicio < fim) {
        auxiliar = letras[inicio];
        letras[inicio] = letras[fim];
        letras[fim] = auxiliar;
        inicio++;
        fim--;
    }
    return new String(letras);
}