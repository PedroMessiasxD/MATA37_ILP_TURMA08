#include <stdio.h>

// Função que realiza a soma
int soma(int a, int b) {
    return a + b;
}
int main() {

    int a = 0;
    int b = 0;
    int resultado = 0;

    scanf("%d", &a);
    scanf("%d", &b);

    if (a >= 1 && a <= 1000 && b >= 1 && b <= 1000) {

        resultado = soma(a, b);
        printf("%d", resultado);

    } else {
        printf("Digite um numero de 1 a 1000");
    }
    return 0;
}