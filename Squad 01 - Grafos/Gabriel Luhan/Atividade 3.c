#include <stdio.h>
#include <string.h>

/*
  * Parâmetros:
 *   w: palavra de entrada
 *   resultado: buffer onde o resultado final é escrito
 */
void proxima_palavra(char *w, char *resultado) {
    int n = strlen(w);

    /* 1º: encontrar o maior índice i - w[i] < w[i+1] */
    int i = n - 2;
    while (i >= 0 && w[i] >= w[i + 1]) {
        i--;
    }

    /* 2º: se o indice não existe, não há palavra maior */
    if (i < 0) {
        strcpy(resultado, "sem resposta");
        return;
    }

    /* 3º: encontrar o maior índice j > i - w[j] > w[i] */
    int j = n - 1;
    while (w[j] <= w[i]) {
        j--;
    }

    /* 4º: trocar w[i] e w[j] */
    char temp = w[i];
    w[i] = w[j];
    w[j] = temp;

    /* 5º: inverter o sufixo a partir de i+1 */
    int esquerda = i + 1;
    int direita = n - 1;
    while (esquerda < direita) {
        temp = w[esquerda];
        w[esquerda] = w[direita];
        w[direita] = temp;
        esquerda++;
        direita--;
    }

    strcpy(resultado, w);
}

int main(void) {
    int t;
    scanf("%d", &t);

    char w[105];
    char resultado[105];

    for (int caso = 0; caso < t; caso++) {
        scanf("%s", w);
        proxima_palavra(w, resultado);
        printf("%s\n", resultado);
    }

    return 0;
}
