def fibfast(num):
    if num < 2:
        return 1
    else:
        return fibfast(num-1) + fibfast(num-2)



num = int(input("enter what fib number you want: "))
print(fibfast(num))
