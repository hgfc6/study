// UMD模块化
// UMD（Universal Module Definition）是一种兼容CommonJS和AMD的模块化规范，使得一个模块可以在不同的环境中使用。
//
// 定义UMD模块：
//
// // myModule.js
// (function (root, factory) {
//     if (typeof define === 'function' && define.amd) {
//         // AMD
//         define(['dependency1', 'dependency2'], factory);
//     } else if (typeof exports === 'object') {
//         // CommonJS
//         module.exports = factory(require('dependency1'), require('dependency2'));
//     } else {
//         // Browser globals (root is window)
//         root.myModule = factory(root.dependency1, root.dependency2);
//     }
// }(this, function (dep1, dep2) {
//     const myFunction = () => {
//         console.log("这是一个UMD导出的函数");
//     }
//
//     return myFunction;
// }));
//
//
// 导入UMD模块：
//
// 在Node.js中：
// const myModule = require('./myModule.js');
// myModule();
//
// 在浏览器中：
// <script src='./myModule.js'></script>
// <script>
//     myModule();
// </script>