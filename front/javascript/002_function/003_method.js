// 方法：在对象内部绑定的函数
let xiaoming = {
    name:"cjh",
    birth: 2000,
    age: function () {
        return new Date().getFullYear() - this.birth;
    }
}