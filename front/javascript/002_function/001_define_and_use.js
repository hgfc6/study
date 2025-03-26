// 》》》》》》函数定义
// 第一种
function name(params) {
    // 逻辑
    return "返回值（可以是多个）";
}

// 第二种
let f = function (params) {
    // 逻辑
    return "返回值";
};//记得加;表示定义结束

// >>>>>>函数参数
// 调用函数时，参数给多了也没事，后面的参数不会用。传少了，后面的参数为undefined
function pp(a, b, c) {
    console.log(a, b, c);
}

pp(1, 2, 3, 4)//1 2 3
pp(1, 2)//1,2,undefined
// >>>>>>arguments js定义的关键字，表示函数的所有入参
function ppp(a, b) {
    console.log(arguments.length);
}

ppp(1, 2, 3, 4)//4

// >>>>>>rest参数 : ES6新增的，rest参数只能写在最后，前面用...标识
function pp2(a,b,...rest) {
    console.log(a, b , rest);
}
pp2(1,2,3,4)// 1 2 [3, 4]
pp2(1,2)// 1 2 [] 没多余参数rest是一个空数组

// 内部变量会屏蔽外部变量
function pp3() {
    var a = 0;
    function pp4() {
        var a = 2;
        console.log(a);//2
    }
    console.log(a);//0
}