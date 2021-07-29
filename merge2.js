function mergeSort(arr) {

    // Cortamos la recursividad
    if (arr.length === 1) return arr;

    //Nos quedamos con la parte entera de la mitad
    let mid = Math.trunc(arr.length / 2)

    //Nos quedamos con la mitad izquierda del array
    let left = arr.splice(0, mid)

    //Nos quedamos con la mitad derecha del array
    let right = arr

    //Aplicamos recursividad con las 2 mitades para dividirlas y ordenarlas
    let mergeLeft = mergeSort(left);
    let mergeRight = mergeSort(right)

    //Cuando la recursividad se corte, va a empezar a ordenar las mitades 
    //y devolverlas a las llamadas anteriores
    return merge(mergeLeft, mergeRight)
}

function merge(left, right) {

    let arrOrdenado = [];

    while(left.length != 0 && right.length != 0){
        let firstElement;
        if(left[0] < right[0]){
            firstElement = left.shift();
        }
        else{
            firstElement = right.shift();
        }
        arrOrdenado.push(firstElement);

    }
    arrOrdenado = arrOrdenado.concat(left).concat(right);
    return arrOrdenado;
}

let arr = [10, 6, 8, 25, 3, 46, 55, 12, 9, 0, 32, 56, 11, 456, 123, 664, 434, 557, 55,1322, 577, 864, 3335 , 123, 1, 2]

console.log(mergeSort(arr));
