// 对象是一种无序的集合数据类型，它由若干键值对组成。
let xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
// 访问属性是通过.操作符完成的，但这要求属性名必须是一个有效的变量名。如果属性名包含特殊字符，就必须用''括起来：
let xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};
// 然后用.['']访问
xiaohong['middle-school'];

//访问不存在的属性返回undefined
// 判断对象有没有属性，使用in
'toString' in xiaoming; // true
// 但是in可能是父类的，判断自己的用hasOwnProperty()
xiaoming.hasOwnProperty('toString');