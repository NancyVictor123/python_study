# Open the text file in read mode
file_path = "DOB.txt"
with open(file_path, "r") as data_file:
    dob_data = data_file.readlines()

# Declare variable to Store names and date of birth
#names = []
birthday = []

print("Name: ")
for line in dob_data:
    splitted_data = line.split()
    name = ' '.join(splitted_data[:2])
    dob = ' '.join(splitted_data[-3:])
    #names.append(name)
    print(name)
    birthday.append(dob)

# Print names and dates of birth separately
# for name in names:
#     print(name)
print("\nBirthday: ")
for dob in birthday:
    print(dob)
