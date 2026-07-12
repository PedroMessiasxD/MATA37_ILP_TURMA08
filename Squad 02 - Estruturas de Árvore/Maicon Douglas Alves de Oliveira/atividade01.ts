function soma(num1: number, num2: number): number {

    if(num1 >= 1 && num2 >= 1000) {
        let resultado: number = num1 + num2;
        return resultado;
    }
    const mensagem: string = "Os números devem ser maiores ou iguais a 1 e 1000, respectivamente.";
    console.log(mensagem);
    return 0;
}

// Exemplo de uso da função
soma(10, 500);
soma(0, 500);

