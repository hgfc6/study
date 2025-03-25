// 数组可以包含任何元素
// 给数组length赋值可以改变数组的大小，多余出来的位置值为undefined
let newVar = [1, 2, "3"];
newVar.length = 5
console.log(newVar)// [1,2,3,undefined,undefined]
// 给超出长度的索引赋值同样会导致这种效果
newVar[6]="x";
console.log(newVar)// [1,2,3,undefined,undefined,undefined,x]
// 大多数其他编程语言不允许直接改变数组的大小，越界访问索引会报错。然而，JavaScript的Array却不会有任何错误。

newVar.indexOf(1)//类似string.indexOf()
newVar.slice(0,1)//类似string.substring(),返回一个新数组。不给参数的话可以复制一个数组
newVar.push("A","B")//末尾添加元素
newVar.pop()//末尾移除一个
newVar.unshift("+")//头部添加元素
newVar.shift()//移除一个头部元素
newVar.splice(1,2, "666")//从指定位置1删除2个元素并把随后的值加进1这里 --- 万能方法
newVar.concat([1,2,4])//数组拼接
newVar.join(",")//把数组元素拼接成一个字符串
