"""
Run time error - Name error, Lion is not defined. As it is a string it 
has be defined inside ""
"""
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16
""" Logical error - The program will print the full_spec string as such, But the 
actual purpose of the program is to print the concatenated value of animal,
number_of_teeth and the animal type. To make it feasible I have made it to be 
a formatted string instead of a regular string.
Also the variables number_of_teeth and animal_type are misplaced hence rearranged
to make it logically correct """
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# Syntax error - missing () in print statement
print(full_spec)