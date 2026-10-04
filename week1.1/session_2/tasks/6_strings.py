# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #prints the original string
print(f"Modified String 1: {user_string.lower()}") #prints the original string in lowercase
print(f"Modified String 2: {user_string.upper()}") #prints the original string in uppercase
print(f"Modified String 3: {user_string.strip()}") #prints the original strings while removing any spaces
print(f"Modified String 4: {user_string.replace('a', '@')}") #prints the original string while replacing a 'a' with a '@'
print(f"Modified String 5: {user_string.capitalize()}") #prints the original string with every letter capatalised
print(f"Modified String 6: {user_string[::-1]}") #prints the original string backwards
print(f"Modified String 7: {user_string.title()}") #prints the original string with the first letter capital of each word
print(f"Modified String 8: {len(user_string)}") #prints the number of charcters in the string
print(f"Modified String 9: {user_string.find('a')}") #prints 
print(f"Modified String 10: {user_string.count('a')}") 
print(f"Modified String 11: {user_string.startswith('Hello')}")
print(f"Modified String 12: {user_string.endswith('!')}") 
print(f"Modified String 13: {user_string.isalnum()}") #
print(f"Modified String 14: {user_string.isalpha()}") #prints true or false depending if therre are symbols in the string
print(f"Modified String 15: {user_string.isdigit()}") #prints true or false depending if there are digits in the string



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!