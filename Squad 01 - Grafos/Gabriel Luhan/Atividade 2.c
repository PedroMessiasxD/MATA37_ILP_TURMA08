#include <stdio.h>
#include <stdlib.h>

/*
 * 
 * Parâmetros:
 *   ar: vetor de inteiros
 *   n:  quantidade de elementos do vetor
 *
 * Retorno:
 *   soma dos elementos do array
 */
int soma_array(int ar[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total = total + ar[i];
    }
    return total;
}

int main(void) {
    int n;

    /* Lê o tamanho do array */
    scanf("%d", &n);

        int *ar = malloc(n * sizeof(int));

    /* Lê os elementos, um por um */
    for (int i = 0; i < n; i++) {
        scanf("%d", &ar[i]);
    }

    /* Resultado */
    printf("%d\n", soma_array(ar, n));

    free(ar);
    return 0;
}