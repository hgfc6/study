// JS语法和Java类似，每行代码后面都会以;结尾，代码块以{}包围，结尾不需要;

// 注释 单行注释// 多行注释/**/

// 》》》》》》数据类型

// >>>>>>Number
// js不区分整数与浮点数，统一用Number
// 这些都是合法的Number
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
0xff00; //十六进制表示
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity

// 运算 + - * / %
1 + 2; // 3
(1 + 2) * 5 / 2; // 7.5
2 / 0; // Infinity
0 / 0; // NaN
10 % 3; // 1
10.5 % 3; // 1.5


// >>>>>>字符串
"ABC"
'ABC'

// >>>>>>布尔值
true;
false;

// >>>>>>逻辑运算
// 与 && 或 || 非!

// >>>>>>比较运算
// > 大于 >= 大于等于
// < 小于 <= 小于等于
// 等于 == js会自动做类型转换 false == 0; // true
// 等于 === 类型+值都一样才返回true
// 特殊的Number：NaN 与其他Number都不相等，包括他自己 NaN === NaN;//false 唯一的判断方式就是isNaN(NaN);//true
// 浮点数不要直接比较，要比较差的绝对值，因为计算机不能准确表示浮点数1 / 3 === (1 - 2 / 3); // false
// Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001; // true

// >>>>>>Bigint
// 表示比2的53次方还大的数时用，就是数字后面加个n 9223372036854775808n
// 可以使用Bigint()把Number和字符串转为Bigint
// Bigint只能和Bigint进行加减乘除运算，不能直接和Number进行这类运算
var bi1 = 9223372036854775807n;
var bi2 = BigInt(12345);
var bi3 = BigInt("0x7fffffffffffffff");
console.log(bi1 === bi2); // false
console.log(bi1 === bi3); // true
console.log(bi1 + bi2);

// >>>>>>null undefined
null; //表示空值，既不是0也不是""
undefined; //表示未定义，仅在判断函数参数是否传递的情况下有用

// >>>>>>>数组
// 一组按顺序排列的集合，可以通过索引下标访问其中的元素，元素类型没有要求可以是任意类型
var arr = [1, 2.0, "3", true];
// 或者new Array(1,2,3) 不常用
console.log(arr[0])

// >>>>>>对象
// 一组键(键都是字符串类型)值对组成的无序组合
var person = {
    name: "zhangsan",
    age: 22,
    tags: ['1', '2']
}
console.log(person.name);
console.log(person.age);

// >>>>>>变量
// 用var声明，用=赋值
var in2 = 3;
in2 = "ABC"//动态语言特性，变量可以指向任意类型的值

// >>>>>>strict模式
// 在js代码第一行加上'use strict';
// 禁止未经var声明的变量出现，因为js设计之初没有var声明的变量默认是全局变量，这带来了各种问题
