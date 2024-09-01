# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    r = 1
    while r != 0:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
