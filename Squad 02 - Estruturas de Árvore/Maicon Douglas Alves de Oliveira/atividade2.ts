function somaArray(arr: number[]): number {
    let resultado: number = 0;
    if(arr.length >= 0 && arr.length <= 1000){

        for(let i = 0; i < arr.length; i++) {

            let arrayTemp: number = arr[i];

            resultado += arrayTemp;
        
        }
        
    }
    return resultado;
}

somaArray([1, 2, 3, 4, 5]);
