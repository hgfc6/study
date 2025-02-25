// CommonJS模块化
// CommonJS主要用于Node.js环境中，使用require来导入模块，使用module.exports或exports来导出模块。

// 导出模块（module.exports）：
const myFunction1 = () => {
    console.log("这是一个CommonJS导出的函数");
}

module.exports = myFunction1;

// 命名导出
module.exports = {
    myFunction2: () => {
        console.log("这是一个CommonJS命名导出的函数");
    },
    myVariable2: 22
}