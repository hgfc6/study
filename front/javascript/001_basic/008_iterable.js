// 可迭代对象
// for in 遍历对象属性名，但是数组键是下标，Map和Set以及对象就不能用下标
// 为了统一，ES6推出了for of

// for ... in循环由于历史遗留问题，它遍历的实际上是对象的属性名称。一个Array数组实际上也是一个对象，它的每个元素的索引被视为一个属性。
// 当我们手动给Array对象添加了额外的属性后，for ... in循环将带来意想不到的意外效果：
// let a = ['A', 'B', 'C'];
// a.name = 'Hello';
// for (let x in a) {
//     console.log(x); // '0', '1', '2', 'name'
// }
// for ... in循环将把name包括在内，但Array的length属性却不包括在内。
// for ... of循环则完全修复了这些问题，它只循环集合本身的元素
for (let x of [1, 2, 3]) {
}

// 更好的方式是直接使用iterable内置的forEach【ES5.1支持】方法，它接收一个函数，每次迭代就自动回调该函数。以Array为例：
let a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(`${element}, index = ${index}`);
});

// Set与Array类似，但Set没有索引，因此回调函数的前两个参数都是元素本身：
let s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    console.log(element);
});

// Map的回调函数参数依次为value、key和map本身：
let m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    console.log(value);
});

// 如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，因此可以忽略它们。例如，只需要获得Array的element：
a.forEach(function (element) {
    console.log(element);
});