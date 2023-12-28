VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
user_input = input("Please enter a text to count \
vowels and consonants:\n")
vowel_count = 0
consonant_count = 0
for letter in user_input.lower():
    if letter in VOWELS:
        vowel_count +=1
    elif letter in CONSONANTS:
        consonant_count +=1
print(f"The total number of vowels is {vowel_count} \
and consonant is {consonant_count}")            