#include <stdio.h>

int main(){
    
    int a = 0;
    int b = 0;
    int soma = 0;

    scanf("%d", &a);
    scanf("%d", &b);
    if (a >= 1 && a <= 1000 && b >= 1 && b <= 1000) {

        soma = a + b;
        printf("%d", soma);
    } else {
        printf("Digite um numero de 1-100");
    }

    return 0;
}