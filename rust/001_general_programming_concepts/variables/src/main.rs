
fn main() {
    // 》》》》》》》》》》》》变量
    // 默认情况下变量是不可变的，但是也可以选择让变量可变，这正是rust安全性和简单并发性特点
    let x = 10;
    println!("x is {}", x);
    // x = 16; //cargo check 你将得到如下报错 error[E0384]: cannot assign twice to immutable variable `x`
    // // Rust 编译器保证了当我们声明了一个值不会改变时，那它就真的不可改变，所以你不必亲自跟踪这个值。这可以使得代码更容易理解。
    // println!("x is {}", x);

    // 要想变量可以改变，可以在前面加上mut
    let mut y = 10;
    println!("y is {}", y);
    y = 16;
    println!("y is {}", y);



    // 》》》》》》》》》》》》常量
    // 使用关键字const定义，并且不能用mut，而且要指定类型，如下
    const PI: f32 = 3.141592653589793;
    println!("PI is {}", PI);
    // 常量一般用大写字母+下划线定义，
    // 最后一个不同点是常量只能设置为常量表达式，而不能是函数调用的结果或是只能在运行时计算得到的值。



    // 》》》》》》》》》》》》遮蔽
    // 后面的变量覆盖前面的变量
    // 注意要使用let重新定义变量，否则会因为变量不可变性 报错
    let m = 10;
    println!("m is {}", m);// 10
    let m = m + 1;
    println!("m is {}", m);// 11
    {
        let m = m * 2;//内部作用域，此时的m只在内部作用域有效
        println!("m is {}", m);//22
    }
    // 出了内部作用域，m=11
    println!("m is {}", m);
    // 重新let和加mut的区别是：
    // let表示重新覆盖了前面一个不可变的变量，这个过程可以做一些转换（特点，下面讲），但是新声明的变量依然是不可变的
    // 使用let定义变量就不能再修改了，防止后续程序一不小心修改变量
    // 而mut则是告诉后续代码，这个变量可以变
    let spaces = "---";
    println!("spaces is {}", spaces);//spaces is ---
    let spaces = spaces.len();
    println!("spaces is {}", spaces);// spaces is 3
    // 上面的代码用同一个名字定义两个变量，spaces前后类型变了
    // 变量遮蔽可以让我们不必给出不同的名称，如 spaces_str 和 spaces_num
    // 相反我们可以重复使用更简单的 spaces 变量名

    // 使用mut则会报错
    // let mut str = "123456";
    // str = str.len()//error[E0308]: mismatched types
}
