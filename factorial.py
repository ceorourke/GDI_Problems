def factorial(num):
    """Returns the factorial of a number"""

    if num == 1:
        return num

    return num * factorial(num-1)

print factorial(4) #=> 4*3*2*1 = 24
print factorial(1) #=> 1
print factorial(5) #=> 5*4*3*2*1 = 120