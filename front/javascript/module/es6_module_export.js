// ES6模块化
//导出模块（export）
//默认导出：一个模块可以有一个默认导出。默认导出可以是任何类型，如函数、对象、原始值等。

const myFunction1 = () => {
    console.log("这是一个默认导出的函数");
}

export default myFunction1;


//命名导出：一个模块可以有多个命名导出。
export const myFunction2 = () => {
    console.log("这是一个命名导出的函数");
}

export const myVariable = 42;

export const func1 = () => { console.log("函数1"); };
export const func2 = () => { console.log("函数2"); };

// 主要区别
// 数量：命名导出可以导出多个值，每个值都有名称；默认导出只能导出一个值，且该值没有名称（导入时可以自定义名称）。
// 导入时的名称：命名导出在导入时必须使用相同的名称；默认导出在导入时可以使用任何名称。
// 语法：命名导出使用export和import { name }的形式；默认导出使用export default和import name的形式。