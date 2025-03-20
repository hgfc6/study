fn main() {
    let mut x = 5;
    't1:loop {
        loop {
            x += 1;
            println!("x = {}", x);
            if x > 10 {
                break 't1
            }
        }
    }

    let mut y = 5;
    let yr = loop {
        y += 1;
        if y > 10 {
            break y * 2;
        }
    };
    println!("yr = {}", yr);// yr = 22

    let mut z = 5;
    while z < 10 {
        z += 1;
    }

    let arr = [1,2,3,4,5,6,7];
    for element in arr {
        println!("element = {}", element);
    }

    for element in (1..10).rev() {
        println!("element = {}", element);
    }
}
