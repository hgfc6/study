// AMD模块化
// AMD（Asynchronous Module Definition）主要用于浏览器环境，通过define函数来定义模块，使用require函数来导入模块。
//
// 定义模块（define）：
// // myModule.js
// define(['dependency1', 'dependency2'], function(dep1, dep2) {
//     const myFunction = () => {
//         console.log("这是一个AMD导出的函数");
//     }
//
//     return myFunction;
// });
//
// 第一个参数是一个数组，表示依赖的模块；第二个参数是一个函数，表示模块的实现。
//
// 导入模块（require）：
//
// require(['./myModule.js'], function(myFunction) {
//     myFunction(); // 输出：这是一个AMD导出的函数
// });