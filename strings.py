# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards).

string = input("Please enter a string: ")

#print(string[0:])
#print(string[-1::-1])   # reads it backward

if string[0:] == string[-1::-1]:
    print("palindrome detected")
else:
    print("regular string detected")



