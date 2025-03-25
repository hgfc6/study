// 字符串
"ABC";
'ABC';
// 如果字符串内部含有需要转义的字符，用反斜杠标识
'I\'m OK';
// 还可以用\u####表示一个Unicode字符
'\u4e2d\u6587'; // 完全等同于 '中文'

// ES6标准中新增了多行字符串的表示方式，就是用反引号``将多行字符串括起来
`it is
a 
mutiline`;

// >>>>>>模板字符串
// 字符串拼接可以用+，也可以用如下的模板形式
let name = "小明";
let age = 22;
let message = `${name} 今年 ${age}岁`;
console.log(message);

// >>>>>>操作字符串
// 需要特别注意的是，字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果：
let s = 'Test';
s[0] = 'X';
console.log(s); // s仍然为'Test'
// JavaScript为字符串提供了一些常用方法，注意，调用这些方法本身不会改变原有字符串的内容，而是返回一个新字符串
"ADC".length // 字符串长度
"".toUpperCase();
"".toLowerCase();
"ABC".indexOf("B");//1
"ABC".substring(1, 2)//B
