#sum of n numbers usinf  functional recursion
def func(n):
    if n == 1:
        return 1
    return n + func(n-1)

x = func(49)
print(x)