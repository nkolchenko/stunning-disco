# List Overlap
# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

resulted_list = []
for element in a:
    if element in b:
        resulted_list.append(element)

#print( dict.fromkeys(resulted_list) )
resulted_list = list( dict.fromkeys(resulted_list) )
print(resulted_list)

