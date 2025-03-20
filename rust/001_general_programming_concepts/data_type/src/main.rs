fn main() {
    // 在类型有可能是多种类型时，我们必须指定类型，否则会报error[E0282]: type annotations needed
    let num: u32 = "22".parse().expect("Not a number!");

    // 》》》》》》》》整数
    let num2 = 22; // Rust默认整型类型为i32

    println!("{} -> {}", num, num2);// 22 -> 22

    // let num3: u8 = 256; // cargo build 会报错 error: literal out of range for `u8`
    // cargo build --release会二进制补码包裹，256变成0 257变成1 并不会？还是报错，为什么
    // println!("num3 -> {}", num3);

    // 要显式处理溢出的可能性，可以使用标准库针对原始数字类型提供的以下一系列方法：
    //
    // 使用 wrapping_* 方法在所有模式下进行包裹，例如 wrapping_add
    // 如果使用 checked_* 方法时发生溢出，则返回 None 值
    // 使用 overflowing_* 方法返回该值和一个指示是否存在溢出的布尔值
    // 使用 saturating_* 方法使值达到最小值或最大值
    // 没懂怎么用 TODO


    // 》》》》》》》》浮点数
    let f1: f32 = 22.0;
    let f2 = 22.0;
    println!("{} -> {}", f1, f2);//22 -> 22



    // 》》》》》》》》数字运算
    // 加+减-乘*除/取模%
    // addition
    let sum = 5 + 10;
    println!("{}",sum);// 15

    //subtraction
    let difference = 95.5 - 4.3;
    println!("{}", difference);// 91.2

    // multiplication
    let product = 4 * 30;
    println!("{}", product);// 120

    // division
    let quotient = 56.7 / 32.2;
    let floored = 5 / 3;
    println!("{} {}", quotient, floored);//1.7608695652173911 1

    // remainder
    let remainder = 43 % 5;// 3
    println!("{}", remainder);


    // 》》》》》》》》字符类型
    let c: char = 'A';
    println!("{}",c); // A



    // 》》》》》》》》复合类型
    // 》》》》》》》》元组
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    // 想从元组中获取个别值，我们可以使用模式匹配来【解构】（destructure）元组的一个值
    let (m1, m2, m3) = tup;
    println!("{}, {}, {}", m1, m2, m3);// 500, 6.4, 1
    // 还可以使用.n 通过索引访问元组元素
    println!("{}, {}, {}",tup.0, tup.1, tup.2);// 500, 6.4, 1
    // println!("{}",tup.3);// error[E0609]: no field `3` on type `(i32, f64, u8)`

    // 没有任何值的元组 () 是一种特殊的类型，只有一个值，也写成 ()。
    // 该类型被称为单元类型（unit type），该值被称为单元值（unit value）
    // 如果表达式不返回任何其他值，就隐式地返回单元值。

    // 》》》》》》》》数组
    // 三种初始化方式
    let a = [1, 2, 3, 4, 5];
    let b: [i64;5] = [1, 2, 3, 4, 5];
    let c = [3;5];
    println!("{}, {}, {}", a[0], b[0], c[0]);// 1, 1, 3
}
