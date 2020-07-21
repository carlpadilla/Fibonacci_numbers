def fib(number):
    # start of the numbers
    a = 0
    b = 1
    for i in range(number):
        # pause at a
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(20):
    print(x)
