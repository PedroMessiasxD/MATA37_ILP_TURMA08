#include <stdio.h>
#include <stdlib.h>

/*
  * Parâmetros:
 *   lista:   vetor aque vai ser ordenado
 *   tamanho: quantidade de elementos do vetor
 */
void bubble_sort(long long lista[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        for (int j = 0; j < tamanho - i - 1; j++) {
            if (lista[j] > lista[j + 1]) {
                long long temp = lista[j];
                lista[j] = lista[j + 1];
                lista[j + 1] = temp;
            }
        }
    }
}

/*
  * Parâmetros:
 *   containers: matriz n x n onde containers[i][j] é a quantidade
 *               de bolas do tipo j no contêiner i
 *   n: dimensão da matriz
 *
 * Retorno:
 *   1 se for "Possível", 0 se for "Impossível"
 */
int organizando_containers(long long **containers, int n) {
    long long *somas_linhas = malloc(n * sizeof(long long));
    long long *somas_colunas = malloc(n * sizeof(long long));

    /* Soma de cada linha = total de bolas em cada contêiner */
    for (int i = 0; i < n; i++) {
        long long soma_linha = 0;
        for (int j = 0; j < n; j++) {
            soma_linha += containers[i][j];
        }
        somas_linhas[i] = soma_linha;
    }

    /* Soma de cada coluna = total de bolas de cada tipo */
    for (int j = 0; j < n; j++) {
        long long soma_coluna = 0;
        for (int i = 0; i < n; i++) {
            soma_coluna += containers[i][j];
        }
        somas_colunas[j] = soma_coluna;
    }

    bubble_sort(somas_linhas, n);
    bubble_sort(somas_colunas, n);

    int possivel = 1;
    for (int i = 0; i < n; i++) {
        if (somas_linhas[i] != somas_colunas[i]) {
            possivel = 0;
            break;
        }
    }

    free(somas_linhas);
    free(somas_colunas);

    return possivel;
}

int main(void) {
    int q;
    scanf("%d", &q);

    for (int consulta = 0; consulta < q; consulta++) {
        int n;
        scanf("%d", &n);

        /* Alocação dinâmica da matriz n x n */
        long long **containers = malloc(n * sizeof(long long *));
        for (int i = 0; i < n; i++) {
            containers[i] = malloc(n * sizeof(long long));
            for (int j = 0; j < n; j++) {
                scanf("%lld", &containers[i][j]);
            }
        }

        int resultado = organizando_containers(containers, n);
        printf("%s\n", resultado ? "Possível" : "Impossível");

        for (int i = 0; i < n; i++) {
            free(containers[i]);
        }
        free(containers);
    }

    return 0;
}