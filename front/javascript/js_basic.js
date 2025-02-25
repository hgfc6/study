function sayHello(name) {
    let num = 0;
    for (let i = 0; i < name.length; i++) {
        num++
    }
    c = closure()
    c()
    c()
    c()
    document.getElementById("app").innerHTML = "Hello " + name + "! you name length is " + num;
}

/*
JavaScript中的闭包（Closure）是一个非常重要的概念，它涉及到函数的执行环境和变量的作用域。闭包指的是一个函数能够记住并访问它的词法作用域，即使这个函数在其词法作用域之外执行。

闭包的基本概念
词法作用域：JavaScript使用词法作用域（也称为静态作用域），这意味着函数的作用域在定义时就已经确定，而不是在运行时确定。
闭包的形成：当一个函数在其定义的词法作用域之外被调用时，它仍然可以访问这个作用域中的变量。这种现象就是闭包。

闭包的工作原理
函数内部的函数：闭包通常通过在一个函数内部定义另一个函数并返回这个内部函数来形成。
闭包捕获变量：内部函数可以访问外部函数的变量，即使外部函数已经执行完毕。这是因为内部函数维护了对外部函数作用域的引用。
*/
function closure() {
    let num = 0;
    return function () {
        num++
        console.log(num)
    }
}