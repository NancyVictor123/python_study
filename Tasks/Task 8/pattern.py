"""Start
Declare a variable length to store the mid point of the pattern
Declare a variable num to store the incremented value
AS there are 9 lines in the pattern, set the i range from 1-10
When i<= length, increment num and print star muliplied by num
When i > length decrement num and print star multiplied by num
End """
length = 5
num = 0
for i in range(1,10):
    if i <= length:
        num += 1
        print("*" * num)
    else:
        num -= 1
        print("*" * num)