/**
 * 	• var is function-scoped (or globally scoped if declared outside a function), meaning it is accessible anywhere within the function it is declared in. It does not have block scope, so it ignores curly braces outside of functions145611.
	• let and const are block-scoped, meaning they are only accessible within the nearest set of curly braces (block) where they are declared (such as inside a loop or if statement)145611.

 */

var global_var = 'global';

function print_global_var() {
    console.log(global_var)
}

print_global_var()

function print_function_var() {
    var function_var = 'function';
    console.log(function_var)
}

print_function_var()

function print_function_var_b() {
    console.log(function_var)
}
// print_function_var_b() //not defined

let global_let = 'global';

function print_global_let() {
    console.log(global_let)
}

print_global_let()

function print_function_let() {
    let function_let = 'function';
    console.log(function_let)
}

print_function_let()

function print_function_let_b() {
    console.log(function_let)
}
// print_function_let_b() //not defined it also functions same as var so as const too


//but the difference is
//let can't access outside loop
for (let i = 0; i<9; i++) {
    let a = 1;
    a+= 1;
}
// console.log(a) //not defined

// var can be accessed outside loop
for (let i = 0; i<9; i++) {
    var b = 1;
    b+= 1;
}
console.log(b)

// const can't be modified and redeclared, let can be modified but cant be redeclared and var can both redeclared and modified

let x = 5;
x = 4;
console.log(x);
// let x = 6; //error
// console.log(x);

const y = 6;
// y = 7; //error
// console.log(y)

var z = 15;
z = 14;
console.log(z);
var z = 16;
console.log(z);

// var doesn't need initialization ie default variables will be var and not let
m = 0;
console.log(m)