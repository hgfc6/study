def fn(*args, **kwargs):
    def fn2():
        i = 0
        nonlocal kwargs
        newArgs = []
        for arg in args:
            if isinstance(arg, str):
                newArgs.insert(i, arg.upper())
            i = i + 1
        for key, value in kwargs.items():
            if isinstance(value, str):
                kwargs[key] = value.upper()
        return newArgs, kwargs
    return fn2


if __name__ == '__main__':
    f = fn("a", "b", "C", name="abC", age="eDt")
    a, b = f()
    print(a)
    print(b)