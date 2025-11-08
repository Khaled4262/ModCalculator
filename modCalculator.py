def modCalculator(a, b):
    """
    This function takes two integers a and b, and returns the result of a modulo b.
    """
    if b == 0:
        raise ValueError("The divisor b cannot be zero.")
    return a % b
def main():
    a = 100
    b = 30
    print(f"The result of {a} mod {b} is: {modCalculator(a, b)}")
main()