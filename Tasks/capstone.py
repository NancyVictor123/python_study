import math
# Explain user about the options.
# Ask user to choose from the given option
# perform task as per the chosen option.
print("Investment - To calculate the amount of interest you'll earn on your investment")
print("Bond - To calculate the amount you'll have to pay on a home loan")
user_input = input("\nEnter either 'Investment' or 'Bond' from the above menu to proceed: ")
# When user selects investment , ask user to enter values for principle, rate of interest and time
# Divide the rate of interest by 100
# Ask user to choose the type of interest and perform task as per their choice using the formula
if user_input.lower() == "investment":
    principle = float(input("\nEnter the amount you are planning to invest: "))
    rate_interest = float(input("Enter rate of interest (Enter only the number eg. 8 and not 8%): ")) / 100
    time = float(input("Enter the number of years you plan to invest: "))
    interest = input("Choose the type of interest. Simple or Compound : ")
    if interest.lower() == "simple":
        simple_interest = principle * (1 + rate_interest * time)
        print(f"\nThe total amount you receive after {time} years = £{simple_interest:.2f}")
    elif interest.lower() == "compound":
        compound_interest = principle * math.pow((1 + rate_interest), time)
        print(f"\nThe total amount you receive after {time} years = £{compound_interest:.2f}")
    else:
        print("Please enter a valid input")
# If user select bond, ask user to key in values and divide rate of interest by 100
# divide rate of interest by 12 to get monthly interest
# Calculate repayment using the formula        
elif user_input.lower() == "bond":
    value = float(input("\nEnter the present value of your house (e.g 100000) :"))
    rate_interest = float(input("\
Enter rate of interest (Enter only the number eg. 8 and not 8%):  ")) / 100
    time = float(input("Enter the number of months you will take to repay (eg. 120): "))
    monthly_interest = rate_interest / 12
    repayment = (monthly_interest*value) / (1 - (1 + monthly_interest) ** (-time))
    print(f"\nThe money you have to repay each month = £{repayment:.2f}")
else:
    print("Please enter a valid input")
    