// js的对象是一组键值对，但是键只能是字符串，其他数据类型不可以
// 为了解决这个问题，ES6新增了Map这种类型
let m = new Map;
m.set(1, 2);
m.delete(1);
// Set 值不重复的集合
let s = new Set;
s.add(1);
s.add(2);
s.add(1);
console.log(s)//[1,2]
s.delete(2);