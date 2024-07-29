import math

print("Enter the following operation to do.")
op = input("/,*,+,-,power,root,trigonometric ratio: ").strip()

# This will help you to divide two numbers.
if op in ["/", "Divide", "divide", "Division", "division"]:
    n = float(input("Enter your 1st number: "))
    m = float(input("Enter your 2nd number: "))
    if m == 0:
        print("Zero is not allowed in the denominator")
    else:
        print("Division of 1st no. by 2nd no. is =", n / m)

# This will help you to multiply two numbers.
elif op in ["*", "multiply", "Multiply"]:
    n = float(input("Enter your 1st number: "))
    m = float(input("Enter your 2nd number: "))
    print("Multiplication of 1st no. and 2nd no. is =", n * m)

# This will help you to add two numbers.
elif op in ["+", "add", "Add", "Addition"]:
    n = float(input("Enter your 1st number: "))
    m = float(input("Enter your 2nd number: "))
    print("The sum of 1st no. and 2nd no. is:", n + m)

# This will help to subtract two numbers.
elif op in ["-", "Sub", "sub", "Subtract", "subtract"]:
    n = float(input("Enter your 1st number: "))
    m = float(input("Enter your 2nd number: "))
    if n > m:
        print("Subtraction of 1st no. by 2nd no. is:", n - m)
    else:
        print("Subtraction of 2nd no. by 1st no. is:", m - n)

# This will help you to find the value of n to the power of m.
elif op in ["power", "Power"]:
    n = float(input("Enter your number: "))
    m = float(input("Enter power of your number: "))
    print(n, "to the power of", m, "=", n ** m)

# This will help you to find roots of the given or chosen number.
elif op in ["root", "Root"]:
    n = float(input("Enter your number: "))
    q = math.sqrt(n)
    print("Root of", n, "is =", q)

# This will help you to calculate the value of trigonometric ratios.
elif op in ["trigonometric ratio", "trigonometric", "ratio", "Trigonometric", "Ratio"]:
    # Provide values
    n = float(input("Enter the value of Theta (in degrees): "))
    print("What do you want to find?")
    t = input("Sin, Cos, Tan, Cosec, Sec, Cot: ").strip()
    theta_radians = math.radians(n)

    if t.lower() == "sin":  # This will find the value of sin
        s = math.sin(theta_radians)
        print("The value of Sin", n, "is =", s)

    elif t.lower() == "cos":  # This will find the value of cos
        s = math.cos(theta_radians)
        print("The value of Cos", n, "is =", s)

    elif t.lower() == "tan":  # This will find the value of tan
        s = math.tan(theta_radians)
        print("The value of Tan", n, "is =", s)

    elif t.lower() == "cosec":  # This will find the value of cosec
        s = 1 / math.sin(theta_radians)
        print("The value of Cosec", n, "is =", s)

    elif t.lower() == "sec":  # This will find the value of sec
        s = 1 / math.cos(theta_radians)
        print("The value of Sec", n, "is =", s)

    elif t.lower() == "cot":  # This will find the value of cot
        s = 1 / math.tan(theta_radians)
        print("The value of Cot", n, "is =", s)

    else:
        print("Enter a correct Trigonometric Ratio")

else:
    print("Enter a valid operation")
