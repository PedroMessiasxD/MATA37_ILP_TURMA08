function proximaPalavraMaior(w: string): string {

    //Tranformando a palavra inteira em pequenos caracteres dentro de um array para mnipular a posição  
    const n: number = w.length; //contando o tamanho do palavra 
    const chars: string[] = []; //Definindo o array como vazio 
    
    
    for (let k = 0; k < n; k++) { // Crie uma variavel temporaria k com o valor de 0, enquanto ele for menor que o tamanho do array de caractere, adicione mais 1 na variavel k
        chars.push(w[k]); // Pega o caractere da palavra original na posição 'k' e o adiciona na última posição (final da fila) do array 'chars'.
    }
    
   
    //encontrando o pivor do numero que for maior ou igual ao numero da direita  
    let i: number = n - 2; //Definindo a penultima posição
    while (i >= 0 && chars[i] >= chars[i + 1]) { //Enquanto a leitura atual for maior ou igual o maior que o seu vizinho a direita 
        i--;  //T Passe para a direita
    }
    
    //Se a posição for igual a - 1, não existir retorne no answer
    if (i === -1) {
        return "no answer";
    }
    
   //Enquanto o numero da direita for menor ou igual ao pivor passe para a esquerda
    let j: number = n - 1; //Definindo a ultima posição do array 
    while (chars[j] <= chars[i]) { //enquanto o numero da direita - ultima posição for menor ou igual a posição do numero que o i parou (pivo) passe para a esquerda 
        j--;
    }
    
    //Fazendo a troca do numero menor da direita para o pivor 
    let temp: string = chars[i]; //criando variavel temporaria do pivor
    chars[i] = chars[j]; // mudando o valor do pivor para o menor numero a direita que seja maior que o pivor
    chars[j] = temp; // trocando os valores do pivor antigo para um numero menor que ele 
    
   //Fazendo a troca do numero menor a esquarda para a direita 
    let esquerda: number = i + 1; //Definindo a esquerda 
    let direita: number = n - 1; //definindo o numero a direita, a ultima posição, tamanho - 1
    while (esquerda < direita) { //Enquanto o indice da esquerda for menor que o da direita 
       
        temp = chars[esquerda]; //crie uma variavel tempporaria com o valor da esquerda
        chars[esquerda] = chars[direita]; //pegue o valor da direite e e coloque ele na esquerda
        chars[direita] = temp; //pegue o temporario e mude o valor dele para o menor numero a direita 
        
        esquerda++; //passe para a direita 
        direita--; //passe para a esquerda
    }
    
   
   //Imprimindo o array organizado 
    let resultado: string = "";
    for (let k = 0; k < n; k++) {
        resultado += chars[k];
    }
    
    return resultado;
}

//TESTES DE CODIGO 

const testesExemplo0: string[] = ["ab", "bb", "hefg", "dhck", "dkhc"];
console.log("--- Resultados Exemplo 0 ---");
for (let k = 0; k < testesExemplo0.length; k++) {
    console.log(`Entrada: ${testesExemplo0[k]} -> Saída: ${proximaPalavraMaior(testesExemplo0[k])}`);
}

const testesExemplo1: string[] = ["lmno", "dcba", "dcbb", "abdc", "abcd", "fedcbabcd"];
console.log("\n--- Resultados Exemplo 1 ---");
for (let k = 0; k < testesExemplo1.length; k++) {
    console.log(`Entrada: ${testesExemplo1[k]} -> Saída: ${proximaPalavraMaior(testesExemplo1[k])}`);
}