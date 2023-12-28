"""
The below logical error program was the one I came through when 
I was doing for loop task. The program was running and the pattern got 
printed but was not as I expected. Later I debugged line by line 
and found the problem was with the range. Whenever I set range, I start from 0.
Hence I chose from 0-9 as i need to print 9 lines.
"""
length = 5
num = 0
for i in range(0,9):
    if i <= length:
        num += 1
        print("*" * num)
    else:
        num -= 1
        print("*" * num)
# added \n to seperate the 2 outputs :)        
print("\n")
"""
Later I debugged and compared values of i and num line by line, found the 
Problem was with the value of i, hence changed the range from 1-10. So the 
logically corrected problem is below.
"""
length = 5
num = 0
for i in range(1,10):
    if i <= length:
        num += 1
        print("*" * num)
    else:
        num -= 1
        print("*" * num)