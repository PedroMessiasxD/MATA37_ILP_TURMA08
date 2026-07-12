#include <stdio.h>

void proximaPalavra(char texto[]) {

    int quantidadeLetras = 0;

    // Descobre o tamanho da palavra
    while (texto[quantidadeLetras] != '\0') {
        quantidadeLetras++;
    }

    // Procura a posição que permite formar uma palavra maior
    int posicaoMudanca = quantidadeLetras - 2;

    while (posicaoMudanca >= 0 &&
           texto[posicaoMudanca] >= texto[posicaoMudanca + 1]) {
        posicaoMudanca--;
    }

    // Se não encontrou, não existe resposta
    if (posicaoMudanca < 0) {
        printf("no answer\n");
        return;
    }

    // Procura a letra adequada para substituir
    int posicaoSubstituta = quantidadeLetras - 1;

    while (texto[posicaoSubstituta] <= texto[posicaoMudanca]) {
        posicaoSubstituta--;
    }

    // Realiza a troca
    char letraTemporaria = texto[posicaoMudanca];
    texto[posicaoMudanca] = texto[posicaoSubstituta];
    texto[posicaoSubstituta] = letraTemporaria;

    // Inverte a parte final da palavra
    int inicioTrecho = posicaoMudanca + 1;
    int fimTrecho = quantidadeLetras - 1;

    while (inicioTrecho < fimTrecho) {

        letraTemporaria = texto[inicioTrecho];
        texto[inicioTrecho] = texto[fimTrecho];
        texto[fimTrecho] = letraTemporaria;

        inicioTrecho++;
        fimTrecho--;
    }

    printf("%s\n", texto);
}

int main() {

    int quantidadePalavras;

    scanf("%d", &quantidadePalavras);

    char listaPalavras[100][101];

    // Lê todas as palavras
    for (int contador = 0; contador < quantidadePalavras; contador++) {
        scanf("%s", listaPalavras[contador]);
    }

    // Processa todas as palavras
    for (int contador = 0; contador < quantidadePalavras; contador++) {
        proximaPalavra(listaPalavras[contador]);
    }

    return 0;
}