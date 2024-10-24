def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test the function with some examples
print(gcd(27, 36)) # Output: 2
print(gcd(144, 72)) # Output: 3
print(gcd(543, 34)) # Output: 5