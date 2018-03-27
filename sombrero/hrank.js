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
    console.log('Factorial: '+factorial(5))
    console.log('Area:' + area(r));
    console.log('Perimeter:' + perimeter(r))

    // const score = +(readLine());
    let score = 23;
    console.log('Grade:'+getGrade(score));
}


function getGrade(score) {
    let grade;
    
    if ( 0 <= score && score <= 5 ) {
        grade='F';
    }
    else if (5<score && score <=10){
        grade='E';
    }
    else if (10<score && score <=15 ){
        grade='D';
    }
    else if ( 15 < score && score <= 20 ) {
        grade='C';
    }
    else if ( 20 < score && score <= 25 ) {
        grade='B';
    }
    else if ( 25 < score && score <= 30 ) {
        grade='A';
    } 
    return grade;
}