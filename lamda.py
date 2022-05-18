#A lambda function is a small anonymous function.
x = lambda a : a + 4
# print(x(5))

""" The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number """
def myLamFun(n):
    return lambda a: a * n

mydoubler = myLamFun(2)
print(mydoubler(5))