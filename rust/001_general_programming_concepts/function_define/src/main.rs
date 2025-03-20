fn main() {
    hello()
}

fn hello() {
    println!("Hello, world!");
    println!("{}", add(1, 2));

    let mut flag = 0;
    't1: loop {
        loop {
            println!("{}", flag);
            flag+=1;
            if flag > 10 {
                break 't1;
            }
        }
    }
}

fn add(num1:i32, num2:i32) -> i32 {

    // 可以提前用return 返回
    println!("{} + {} = {}", num1, num2, num1);
    num1 + num2
}
