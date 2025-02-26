//1. 函数声明
//这是最常见的函数定义方式，使用 function 关键字来声明一个函数。

function add1(a, b) {
    return a + b;
}

//2. 函数表达式
//函数表达式是将函数赋值给一个变量。这种方式允许你在需要时定义函数，并且可以作为参数传递给其他函数。

const add2 = function (a, b) {
    return a + b;
};

//3. 箭头函数
//箭头函数是ES6引入的一种简洁的函数定义方式，特别适合用于匿名函数或回调函数。

const add3 = (a, b) => a + b;

//如果函数体只有一行代码，可以省略 return 关键字和大括号。

//4. 立即执行函数表达式 (IIFE)
//立即执行函数表达式在定义后立即执行，通常用于创建一个独立的作用域。

(function () {
    console.log('This function is executed immediately!');
})();

//5. 生成器函数
//生成器函数使用 function* 关键字定义，可以通过 yield 关键字暂停和恢复函数执行。

function* generateSequence() {
    yield 1;
    yield 2;
    yield 3;
}

const generator = generateSequence();
console.log(generator.next().value); // 输出 1
console.log(generator.next().value); // 输出 2
console.log(generator.next().value); // 输出 3

//6. 异步函数
//异步函数使用 async 关键字定义，通常与 await 关键字一起使用，用于处理异步操作。

async function fetchData() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
}

//7. 构造函数
//构造函数用于创建对象实例，通常与 new 关键字一起使用。

function Person(name, age) {
    this.name = name;
    this.age = age;
}

const person = new Person('Alice', 25);
console.log(person.name); // 输出 Alice

//8.方法定义
//在对象中定义的方法,可以使用简写语法

const obj = {
    name: String,
    add(a, b) {
        return a + b;
    }
};

console.log(obj.add(1, 2)); // 输出 3