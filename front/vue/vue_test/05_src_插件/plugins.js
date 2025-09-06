//定义插件
export default {
    install(Vue, x, y, z) {
        //在此添加各种全局配置
        Vue.filter('myfilter', function (value) {
            console.log(x, y, z)
            return value.slice(0, 3)
        })
        Vue.prototype.x = 100
    }
}