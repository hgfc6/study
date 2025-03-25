// 循环
for (i=0;i<10;i++) {

}
// for in
let arr = [1,2,3]
for (let index in arr) {//index是索引，数组也是对象，索引就是key

}
let o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (let key in o) {//key是属性名
    if (o.hasOwnProperty(key)) {
        console.log(key); // 'name', 'age', 'city'
    }
}

// while
while (condition1) {

}
// do while
do {

} while (condition2)