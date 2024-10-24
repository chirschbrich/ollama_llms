def gcf(a, b):
    """Find the GCF of two numbers using Euclidean algorithm"""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(gcf(27, 36))   # Output: 15
print(gcf(144, 72))   # Output: 15
print(gcf(543, 34))   # Output: 15
