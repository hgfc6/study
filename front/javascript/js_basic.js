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

/*
1. Array（数组）
数组用于存储多个值在单个变量中。JavaScript数组是动态的，可以存储不同类型的元素。

常用方法：
push(element1, element2, ...): 将一个或多个元素添加到数组的末尾，并返回数组的新长度。
pop(): 移除数组的最后一个元素，并返回该元素。
unshift(element1, element2, ...): 在数组的开头添加一个或多个元素，并返回数组的新长度。
shift(): 移除数组的第一个元素，并返回该元素。
slice(start, end): 返回一个新的数组对象，这一对象是一个由begin和end决定的原数组的浅拷贝，原始数组不会被改变。
splice(start, deleteCount, item1, item2, ...): 更改数组的内容，可以通过删除现有元素和/或添加新元素来实现。
map(callback, thisArg): 创建一个新数组，其结果是对原数组的每个元素都执行一次提供的函数后的返回值。
filter(callback, thisArg): 创建一个新数组，其中所有元素都通过了提供的函数实现的测试。
reduce(callback, initialValue): 对数组中的每个元素执行一个由你提供的 reducer 函数(升序执行)，将其结果汇总为单个返回值。
forEach(callback, thisArg): 对数组的每个元素执行一次提供的函数。
concat(value1, value2, ..., valueN): 合并两个或更多的数组。此方法不会更改现有数组，而是返回一个新数组。

2. Object（对象）
对象是用于存储和管理数据的复合数据类型。对象存储键/值对，其中键被称作属性（或属性名），值可以是任何类型的数据。

常用方法：
Object.keys(obj): 返回一个包含对象自身所有可枚举属性的数组。
Object.values(obj): 返回一个包含对象自身所有可枚举属性值的数组。
Object.entries(obj): 返回一个给定对象自身可枚举属性的 [key, value] 对数组。
Object.assign(target, ...sources): 将所有可枚举属性的值从一个或多个源对象复制到目标对象。它将返回目标对象。
Object.create(proto, [propertiesObject]): 创建一个新对象，使用现有对象作为新创建对象的原型。
Object.defineProperty(obj, prop, descriptor): 直接在一个对象上定义一个新属性，或者修改一个现有属性，并返回此对象。
Object.freeze(obj): 冻结对象：即不能添加新属性，不能修改已有属性的可枚举性、可配置性、可写性，不能修改已有属性的值，不能删除已有属性。之后此对象成为一个常量。
obj.hasOwnProperty(prop): 返回一个布尔值，指示对象自身属性中是否具有指定名称的属性（不包括从原型链继承的属性）。
obj.isPrototypeOf(obj2): 返回一个布尔值，指示对象是否为另一个对象的原型。


3. String（字符串）
字符串是用于存储文本的数据类型。字符串在JavaScript中是不可变的。

常用方法：
length: 返回字符串的长度。
charAt(index): 返回指定位置的字符。
concat(str1, str2, ..., strX): 连接两个或多个字符串，并返回新的字符串。
indexOf(searchValue, fromIndex): 返回指定值的首次出现的位置，如果未找到则返回 -1。
substring(startIndex, endIndex): 返回从索引startIndex开始到endIndex(不包括)结束的字符串。
toUpperCase(): 将字符串转换为大写。
toLowerCase(): 将字符串转换为小写。
split(separator, limit): 通过指定分隔符将字符串分割成数组。
trim(): 去除字符串两端的空白字符。
includes(searchString, position): 判断一个字符串是否包含在另一个字符串中，返回布尔值。
startsWith(searchString, position): 判断一个字符串是否以指定的子字符串开始，返回布尔值。
endsWith(searchString, length): 判断一个字符串是否以指定的子字符串结束，返回布尔值。

4. Date（日期）
Date对象用于处理日期和时间。

常用方法：
new Date(): 创建一个表示当前日期和时间的Date对象。
getDate(): 返回指定日期的日期。
getMonth(): 返回指定日期的月份（0-11）。
getFullYear(): 返回指定日期的年份。
getMinutes(): 返回指定日期的分钟。
getSeconds(): 返回指定日期的秒数。
getMilliseconds(): 返回指定日期的毫秒数。
setDate(date): 设置指定日期中的日期。
setMonth(month): 设置指定日期中的月份。
setFullYear(year): 设置指定日期中的年份。
toDateString(): 把日期转换为易读的字符串。
toISOString(): 根据世界时返回一个ISO格式的字符串。

5. Math（数学）
Math对象提供了许多数学函数和常量。

常用方法：
Math.random(): 返回0到1之间的随机数。
Math.max(value1, value2, ..., valueN): 返回一组数中的最大值。
Math.min(value1, value2, ..., valueN): 返回一组数中的最小值。
Math.floor(x): 返回小于或等于x的最大整数。
Math.ceil(x): 返回大于或等于x的最小整数。
Math.round(x): 返回最接近的整数。
Math.pow(base, exponent): 计算base的exponent次方。
Math.sqrt(x): 计算x的平方根。
Math.abs(x): 返回x的绝对值。
Math.sin(x), Math.cos(x), Math.tan(x): 返回x的正弦、余弦和正切值。
Math.PI: 提供π的值。

6. JSON（JavaScript对象表示法）
JSON对象用于解析和生成JSON格式的数据。

常用方法：
JSON.parse(text, reviver): 解析一个JSON字符串，构造由字符串描述的JavaScript值或对象。
JSON.stringify(value, replacer, space): 将一个JavaScript值或对象转换为JSON字符串。

7. Map（映射）
Map对象保存键值对，并且能够记住键的原始插入顺序。任何值都可以作为键或值。

常用方法：
new Map([iterable]): 创建一个Map对象。
map.set(key, value): 设置Map对象中指定键的值。
map.get(key): 返回Map对象中指定键的值。
map.has(key): 返回一个布尔值，用来判断Map对象中是否存在指定的键。
map.delete(key): 删除Map对象中指定键的值。
map.clear(): 清空Map对象的所有键值对。
map.size: 返回Map对象键值对的数量。
map.forEach(callbackFn, thisArg): 为Map对象中的每个键值对执行一次提供的函数。

8. Set（集合）
Set对象允许你存储任何类型的唯一值，无论是原始值还是对象引用。

常用方法：
new Set([iterable]): 创建一个Set对象。
set.add(value): 添加一个指定的值到Set对象中。
set.has(value): 返回一个布尔值，用来判断Set对象中是否存在指定的元素。
set.delete(value): 删除Set对象中指定的元素。
set.clear(): 清空Set对象的所有元素。
set.size: 返回Set对象中元素的数量。
set.forEach(callbackFn, thisArg): 为Set对象中的每个元素执行一次提供的函数。

9. RegExp（正则表达式）
RegExp对象用于创建正则表达式。

常用方法：
new RegExp(pattern, flags): 创建一个正则表达式。
test(str): 检测一个字符串是否与正则表达式匹配。
exec(str): 在一个字符串中执行一个搜索匹配。

10. Error（错误）
Error对象用于创建错误对象。

常用方法：
new Error(message): 创建一个Error对象。
name: 错误名称。
message: 错误消息。
stack: 错误堆栈。
 */