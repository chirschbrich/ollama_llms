def gcf(a, b):
    if a < b:
        a, b = b, a

    while(b != 0):
        remainder = a % b
        a = b
        b = remainder

    return abs(a)

# Example usage
num1 = 543
num2 = 34
gcf_value = gcf(num1, num2)
print(f"The GCF of {num1} and {num2} is: {gcf_value}")