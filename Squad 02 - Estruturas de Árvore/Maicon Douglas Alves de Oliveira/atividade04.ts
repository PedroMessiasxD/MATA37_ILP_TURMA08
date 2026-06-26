function organizarContainers(containers: number[][]): string {

    
    const n = containers.length;

    let capacidade: number[] = [];
    let quantidadePorCor: number[] = [];

    //inicializando os array da linha e da coluna para terem o mesmo tamanho do que o container 
    for (let i = 0; i < n; i++) {
        capacidade.push(0);
        quantidadePorCor.push(0);
    }

    //Colocando as bolas nas linhas e nas colunas 
    for (let i = 0; i < n; i++) {  // Criando um for para mapear as linhas do container, 
        for (let j = 0; j < n; j++) { //criando outro for para mapear as colunas do container 
            let bolasNestaPosicao = containers[i][j]; //criando variavel temporaria para pegar os valores das linhas[i] e colunas [j]
            
            capacidade[i] += bolasNestaPosicao; //adicionando os valores da linha[i] na variavel de capacidade 
            quantidadePorCor[j] += bolasNestaPosicao; //adicionando os valores da coluna[j] na variavel de quantidade por cor 
        }
    }

    // Ordernando por capacidade 
    for (let i = 0; i < n - 1; i++) { 
        for (let j = 0; j < n - i - 1; j++) { 
            if (capacidade[j] > capacidade[j + 1]) { // Se o valor atual for maior que o seu vizinho à direita, efetue a troca
                let temp = capacidade[j]; // Armazena o valor atual no copo temporário
                capacidade[j] = capacidade[j + 1]; // Puxa o menor valor para a esquerda
                capacidade[j + 1] = temp; // Empurra o maior valor para a direita
            }
        }
    }

    // Ordernando a capacidade por cor 
    //Mesma logica da ordenação acima
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (quantidadePorCor[j] > quantidadePorCor[j + 1]) {
                let temp = quantidadePorCor[j];
                quantidadePorCor[j] = quantidadePorCor[j + 1];
                quantidadePorCor[j + 1] = temp;
            }
        }
    }
    
    // Verificação final - A Invariante: as capacidades e as quantidades totais devem ser idênticas
    for (let k = 0; k < n; k++) { 
        // Se houver qualquer divergência estrutural, a organização total é impossível
        if (capacidade[k] !== quantidadePorCor[k]) { 
            return "Impossible";
        }
    }

    return "Possible";
}