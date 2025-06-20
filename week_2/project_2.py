import math

def solve_quadratic():
    print("\nSolving Quadratic Equation: Ax^2 + Bx + C = 0")
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))

    # Calculate the discriminant
    D = B**2 - 4*A*C  

    if D > 0:
        root1 = (-B + math.sqrt(D)) / (2*A)
        root2 = (-B - math.sqrt(D)) / (2*A)
        print(f"Roots are: {root1} and {root2}")
    elif D == 0:
        root = -B / (2*A)
        print(f"Root is: {root}")
    else:
        print("No real roots (Complex numbers).")

# Test the function
solve_quadratic()

import numpy as np

def solve_cubic():
    print("\nSolving Cubic Equation: Ax^3 + Bx^2 + Cx + D = 0")
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))

    # Solve for roots
    coefficients = [A, B, C, D]
    roots = np.roots(coefficients)

    print("Roots are:", roots)

# Test the function
solve_cubic()

def solve_quartic():
    print("\nSolving Quartic Equation: Ax^4 + Bx^3 + Cx^2 + Dx + E = 0")
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))
    E = float(input("Enter coefficient E: "))

    # Solve for roots
    coefficients = [A, B, C, D, E]
    roots = np.roots(coefficients)

    print("Roots are:", roots)

# Test the function
solve_quartic()

import math
import numpy as np

def solve_quadratic():
    print("\nSolving Quadratic Equation: Ax^2 + Bx + C = 0")
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))

    D = B**2 - 4*A*C  
    if D > 0:
        root1 = (-B + math.sqrt(D)) / (2*A)
        root2 = (-B - math.sqrt(D)) / (2*A)
        print(f"Roots are: {root1} and {root2}")
    elif D == 0:
        root = -B / (2*A)
        print(f"Root is: {root}")
    else:
        print("No real roots (Complex numbers).")

def solve_cubic():
    print("\nSolving Cubic Equation: Ax^3 + Bx^2 + Cx + D = 0")
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))

    roots = np.roots([A, B, C, D])
    print("Roots are:", roots)

def solve_quartic():
    print("\nSolving Quartic Equation: Ax^4 + Bx^3 + Cx^2 + Dx + E = 0")
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    D = float(input("Enter coefficient D: "))
    E = float(input("Enter coefficient E: "))

    roots = np.roots([A, B, C, D, E])
    print("Roots are:", roots)

# Main Program
while True:
    print("\nChoose an equation to solve:")
    print("1. Quadratic Equation (Ax^2 + Bx + C = 0)")
    print("2. Cubic Equation (Ax^3 + Bx^2 + Cx + D = 0)")
    print("3. Quartic Equation (Ax^4 + Bx^3 + Cx^2 + Dx + E = 0)")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        solve_quadratic()
    elif choice == '2':
        solve_cubic()
    elif choice == '3':
        solve_quartic()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
