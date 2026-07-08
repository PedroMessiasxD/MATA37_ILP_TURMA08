#include <stdio.h>

/*
 * Parâmetros:
 *   a: primeiro valor
 *   b: segundo valor
 *
 * Retorno:
 *   a soma de a e b
 */
int soma(int a, int b) {
    int resultado = a + b;
    return resultado;
}

int main(void) {
    int a, b;

    /* Lê os dados de entrada */
    scanf("%d", &a);
    scanf("%d", &b);

    /* Resultado */
    printf("%d\n", soma(a, b));

    return 0;
}