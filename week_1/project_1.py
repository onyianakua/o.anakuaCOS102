
def get_float_input(prompt):
    """Function to safely get float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def simple_interest(P, R, T):
    """Calculate Simple Interest"""
    return P * (1 + (R / 100) * T)

def compound_interest(P, R, n, t):
    """Calculate Compound Interest"""
    return P * (1 + R / n) ** (n * t)

def annuity_plan(PMT, R, n, t):
    """Calculate Annuity Plan"""
    return PMT * ((1 + R / n) ** (n * t) - 1) / (R / n)

def main():
    print("Choose the type of calculation:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Annuity Plan")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Simple Interest
        P = get_float_input("Enter Principal Amount: ")
        R = get_float_input("Enter Annual Interest Rate (in %): ")
        T = get_float_input("Enter Time Period (in years): ")
        A = simple_interest(P, R, T)
        print(f"Total Amount after Simple Interest: {A:.2f}")

    elif choice == "2":
        # Compound Interest
        P = get_float_input("Enter Principal Amount: ")
        R = get_float_input("Enter Annual Interest Rate (in decimal, e.g., 5% as 0.05): ")
        n = int(get_float_input("Enter Number of Times Interest is Compounded per Year: "))
        t = get_float_input("Enter Time Period (in years): ")
        A = compound_interest(P, R, n, t)
        print(f"Total Amount after Compound Interest: {A:.2f}")

    elif choice == "3":
        # Annuity Plan
        PMT = get_float_input("Enter Periodic Payment Amount: ")
        R = get_float_input("Enter Annual Interest Rate (in decimal, e.g., 5% as 0.05): ")
        n = int(get_float_input("Enter Number of Payments per Year: "))
        t = get_float_input("Enter Total Number of Years: ")
        A = annuity_plan(PMT, R, n, t)
        print(f"Total Amount Accumulated in Annuity Plan: {A:.2f}")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

# Run the program
main()
