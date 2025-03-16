def jisuanqi():
    str = input('请输入')
    if str == "exit":
        return True
    split = str.split(" ")
    if len(split) != 3:
        print("输入格式错误")
        return False
    num1, num2, op = split[0], split[2], split[1]
    # 也可直接解包 num1, op, nums = split
    if '.' in num1 or '.' in num2:
        num1, num2 = float(num1), float(num2)
    else:
        num1, num2 = int(num1), int(num2)
    match op:
        case "+":
            print("result = ", num1 + num2)
        case "-":
            print("result = ", num1 - num2)
        case "*":
            print("result = ", num1 * num2)
        case "/":
            if num2 == 0:
                print("错误，除数不能为0")
                return False
            print("result = ", num1 / num2)
        case _:
            print("%s 未定义" % op)
    return False


if __name__ == '__main__':
    exitFlag = False
    while True:
        if exitFlag:
            break
        exitFlag = jisuanqi()
