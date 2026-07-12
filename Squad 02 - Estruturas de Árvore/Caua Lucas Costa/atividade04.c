#include <stdio.h>

int main(){

    int q = 0;
    scanf("%d", &q);

    for(int teste = 0; teste < q; teste++){

        int n = 0;
        scanf("%d", &n);

        long long containers[n];
        long long tipos[n];

        for(int i = 0; i < n; i++){
            containers[i] = 0;
            tipos[i] = 0;
        }

        long long numero = 0;

        for(int i = 0; i < n; i++){

            for(int j = 0; j < n; j++){

                scanf("%lld", &numero);

                containers[i] = containers[i] + numero;
                tipos[j] = tipos[j] + numero;

            }

        }

        for(int i = 0; i < n - 1; i++){

            for(int j = i + 1; j < n; j++){

                if(containers[i] > containers[j]){

                    long long aux = containers[i];
                    containers[i] = containers[j];
                    containers[j] = aux;

                }

                if(tipos[i] > tipos[j]){

                    long long aux = tipos[i];
                    tipos[i] = tipos[j];
                    tipos[j] = aux;

                }

            }

        }

        int igual = 1;

        for(int i = 0; i < n; i++){

            if(containers[i] != tipos[i]){

                igual = 0;
                break;

            }

        }

        if(igual == 1){

            printf("Possible\n");

        }else{

            printf("Impossible\n");

        }

    }

    return 0;

}