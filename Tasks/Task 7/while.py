"""
Start of the pseudo code
Declare a variable sum to add the numbers entered by user
When user_input not equal to -1 the trial should increment 
and the number should be added and prompt the user to add another number
When the user enters -1, the loop should stop 
and the average of numbers entered by user should be printed
end of the pseudo code
"""
user_input = 0
trial = 0
sum = 0
average = 0 
while user_input != -1:
    user_input = float(input("Please enter a number : "))
    if user_input != -1:
        trial += 1
        sum +=  user_input
    else:    
        average = sum / trial
        print(f"The average of numbers you entered is {average:.2f}")
