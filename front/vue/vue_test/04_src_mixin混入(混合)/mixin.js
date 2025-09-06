//局部混入
export const mixin = {
    data() {
        return {
            name: 'zhangsan'
        }
    },
    methods: {
        showName() {
            alert(this.name)
        }
    }
}
//全局混入
export const mixin2 = {
    mounted() {
        console.log('mounted 全局混入 ' + this.name)
    }
}