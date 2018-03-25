'use strict';

// process.stdin.resume();
// process.stdin.setEncoding('utf-8');

// let inputString = '';
// let currentLine = 0;

// process.stdin.on('data', inputStdin => {
//     inputString += inputStdin;
// });

// process.stdin.on('end', _ => {
//     inputString = inputString.trim().split('\n').map(string => {
//         return string.trim();
//     });
    
    main();    
// });

// function readLine() {
//     return inputString[currentLine++];
// }

function greeting(parameterVariable) {
    // This line prints 'Hello, World!' to the console:
    console.log(parameterVariable)

    // Write a line of code that prints parameterVariable to stdout using console.log:
    
}

function factorial(input){
    if ( input == 1 || input == 0 )
        return 1;
    else
        {return input * factorial(input-1)}
    
}
function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    const PI = Math.PI;
    // var r = readLine(inputString);
    var r = 2.6;
    // Print the area of the circle:
    function area(r){
        return Math.pow(r,2)*PI;       
    }
    // Print the perimeter of the circle:
    function perimeter(r){
        return 2*r*PI;
    }
    console.log(area(r));
    console.log(perimeter(r))
}