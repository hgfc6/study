// 》》》》》变量作用域
// >>>>>变量提升 js会把var声明的变量提升到函数顶部
function pp4() {
    var x = "hello" + y;
    console.log(x);
    var y = "Bob";
}

pp4();// hello undefined 虽然y没有报错(js提升了y的声明)，但是js并没有给y赋值，y在打印时值为undefined
// 所以一定要声明时赋值，否则会出现意想不到的错误

// >>>>>>全局作用域
// 没有在任何函数体内声明的变量(不止变量，还有函数、对象...)作用域是全局
// js默认有个全局对象window
window.pp4();
// 任何作用域都会从当前作用域寻找，找不到就会向上寻找，直到window，如果还没找到就会报错ReferenceError

// >>>>>>名字空间
// 为了防止各种变量都在window下导致冲突严重，可以定义一个全局变量，后续的变量都挂在这个全局变量下，很多开源项目都是这样做的，例如：JQuery,YUI,underscore
var MYAPP = {};
MYAPP.name = "张三";
MYAPP.pp5 = function () {
    console.log("pp5");
}

// >>>>>>局部作用域
// 由于var声明的变量作用域是函数内部，这可能导致各种奇葩的用法，所以ES6引入了let来代替，let作用域只在定义它的块内
function pp6() {
    for (var i = 0; i <= 10; i++) {

    }
    console.log(i + 100);//110
}

function pp7() {
    for (let im = 0; i <= 10; i++) {

    }
    console.log(im + 100);//// SyntaxError:
}

//>>>>>>常量
// ES6之前我们无法定义一个常量，只能把名称写成全部大写，软性的告诉别人：这是一个常量，请不要改动
// ES6后使用const表示常量，const声明的常量不可改变，具有和let一样的块级作用域
const PI = 3.14;
// PI = 123; error


// 》》》》》》解构赋值
// 从ES6开始，JavaScript引入了解构赋值，可以同时对一组变量进行赋值。
let [a1, a2, a3] = [1, 2, 3]
console.log(a1, a2, a3);// 1 2 3G
// 有嵌套也可以
let [b1, [b2, b3]] = [1, [2, 3]]
console.log(b1, b2, b3);// 1 2 3
// 忽略某些元素
let [, c2] = [1, 2]
console.log(c2);//2
// 对象也可以,注意用{}
let person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school',
    address: {
        city: 'Beijing',
        street: 'No.1 Road',
        zipcode: '100001'
    }
};
let {name, age, address: {city, nib}} = person
console.log(name, age, city, nib);// 小明 20 Beijing undefined（没有该变量）
// console.log(address) //Uncaught ReferenceError: address is not defined
// 注意: address不是变量，而是为了让city和nib获得嵌套的address对象的属性:
// 把passport属性赋值给变量id:
let {passport: id} = person;
id; // 'G-12345678'
// 注意: passport不是变量，而是为了让变量id获得passport属性:
// passport; // Uncaught ReferenceError: passport is not defined

// 还可以使用默认值
let {single = true} = person
console.log(single); // true

// 如果变量已被声明，再解构就会报错
let d1, d2;
// {d1, d2} = {d1:12,d2:13}
// 这是因为JavaScript引擎把{开头的语句当作了块处理，于是=不再合法。解决方法是用小括号括起来：
({d1, d2} = {d1: 12, d2: 13})

// >>>>>>使用场景
// 1.交换值
let e1 = 1, e2 = 2;
[e1, e2] = [e2, e1];
// 2.快速获取当前页面的域名和路径：
let {hostname:domain, pathname:path} = location;
// 3.解构对象类型的参数
function buildDate({year, month, day, hour=0, minute=0, second=0}) {
    return new Date(`${year}-${month}-${day} ${hour}:${minute}:${second}`);
}
buildDate({year:2025, month:3, day:26})//也可以传入minute,second等参数，不传也行，因为有默认值