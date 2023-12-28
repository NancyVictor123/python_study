#Syntax error , missing () in print statement
print("Welcome to the error program")
# Syntax error, Indentation not necessary . Also missing () 
print ("\n")
# Syntax error - Removed indentation in the below lines
# Variables declaring the user's age, casting the str to an int, and printing the result

"""
Runtime Error - age_Str is not defined. Also I think it could 
be a logical error as instead of assinging the string value to 
age_Str we are comparing it with "=="
"""
age_Str = "24" 

"""
Value Error - when casting a string to integer we can only have numbers
in the String. Here age_Str has 24 years old, and it cannot be casted to 
integer hence value error accured in age. To rectify it, I change 24 years old 
to 24
"""
age = int(age_Str) 

"""
Run time error, age variable has an integer, so we cannot concatenate a 
string and integer in print statement. So I casted age to string. Also 
to make the output statement presentable I added a space string 
"""
print("I'm" +" " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age

years_from_now = "3"
"""
Runtime error - Type error - years_from_now has a string value and a string 
annot be added to an integer, So I casted years_from_now to integer  
"""
total_years = age + int(years_from_now)
# Syntax error - Missing () in print statement
"""
Logical error : The rpint statement will only print The total number of years:
answer_years as they both are strings. But to print the answer obtained from previous
step we have to cast and concatenate the total_years variable."""
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result

"""
Run time error - Name error. variable total is not defined earlier. instead i have added total_years
to the calculation as per the need .

Logical error - the final print statement states in 3 years and 6 months , So as per logic we have to
add 3 years and 6 months and this code doesn't have 6 months added to it. Hence i added 6 months also
to get the desired output
"""
total_months = (total_years * 12) + 6
# Syntax error - Missing () in print statement
"""
Runtime error - Type error - total_months has an integer value, and in print statement we 
cannot concatenate a string and an integer, hence I casted it to string

"""
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
