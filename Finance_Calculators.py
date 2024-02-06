# Program that gives users options of choosing between 2 financial calculators: investment calculator or home loan calculator

import math
def investment_calculator():
    print("\nInvestment Calculator")
    deposit = float(input("Enter the amount of money you are investing as a deposit (£): "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of planned investment years: "))
    
   # Validate user input for interest type (Simple or Compound)
    valid_interest_types = ["simple", "compound"] 
    interest_type = input("Enter a choice for interest calculation (Simple/Compound): ").lower()
    while interest_type not in valid_interest_types:
        print("Invalid choice. Please enter either 'Simple' or 'Compound'.")
        interest_type = input("Enter choice for interest calculation (Simple/Compound): ").lower()

    # Convert interest rate into decimal
    interest_rate /= 100   
    
    # Calculate investment amount based on user's choice
    if interest_type == "simple":
        amount = deposit * (1 + interest_rate * years)
    else:  # Compound interest
        amount = deposit * math.pow(1 + interest_rate, years)

    print(f"\nAfter {years} years, your investment will be: £{amount:.2f}")

def bond_calculator():
    print("\nBond Calculator")
    present_value = float(input("Enter the present value of the house (£): "))
    interest_rate = float(input("Enter the interest rate of the house (as a percentage): "))
    months = int(input("Enter the number of months you plan to repay the bond: "))

    # Convert interest rate into decimal
    interest_rate /= 100  

    # Calculate monthly repayment using the bond formula
    i = interest_rate / 12
    repayment = i * present_value / (1 - math.pow(1 + i, -months))

    print(f"\nYou will have to repay £{repayment:.2f} each month for the bond.")

def main():
    print("Welcome to the Financial Calculator Program")
    print("Investment - To calculate the amount of interest you will earn on your investment")
    print("Bond - To calculate the amount you will have to pay for a home loan")

    user_choice = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ").lower()

    if user_choice == "investment":
        investment_calculator()
    elif user_choice == "bond":
        bond_calculator()
    else:
        print("Invalid choice. Please enter either 'Investment' or 'Bond'.")

if __name__ == "__main__":
    main()