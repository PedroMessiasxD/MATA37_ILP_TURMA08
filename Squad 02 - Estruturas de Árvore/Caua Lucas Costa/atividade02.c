#include <stdio.h>

int main(){

    int n = 0;
    scanf("%d", &n);

    int elemnts[n];
    int soma = 0;

    for (int i = 0; i < n; i++){
        scanf("%d", &elemnts[i]);   

        if (elemnts[i] < 0 || elemnts[i] > 1000){
            printf("digite um numero valido, entre 0-1000\n");
            i--;
        } else {
            soma = elemnts[i] + soma;
        }
    }
    printf("%d", soma);
}