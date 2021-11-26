from typing import Callable

a = int(input('Enter the first number - '))
b = int(input('Enter the second number - '))

def decor(function: Callable):
    def decoratee():
        return f"{function.__name__}\n{function()}"
    return decoratee

@decor
def sum():
    c = str(a + b)
    return c
print(sum())

@decor
def multi():
    c = str(a * b)
    return c
print(multi())

def main():
    for i in range(1000000001):
        if i % 2 == 0:
            yield i**2
gen = main()

for item in gen:
    print(item)
