# Task to print alternate words to upper and lower
# Read in the user input as string
# Declare a variable to store the final string
# Using For loop, check the index of words and store alternate
# word as upper and lower
# print the final string

string = input("Please enter a sentence : ")
final_string = ""
for i in range(len(string)):
    if i % 2 == 0:
        final_string += string[i].upper()
    else:
        final_string += string[i].lower()
print(final_string)

# Task 2 to print alternate words to upper and lower
# Using the same input, split the string to a list
# Using for loop, check the index of list value and convert alternate
# words to upper and lower case and append it to split_list
# Join and print the split_list

splitted_string = string.split()
split_list = []
#print("Splitted string is = " , splitted_string)
for i in range(len(splitted_string)):
    if i % 2 == 0:
        split_list.append(splitted_string[i].upper())
    else:
        split_list.append(splitted_string[i].lower())
#print("Splitted list = " , split_list)
print(" ".join(split_list))
