"""
List Overlap
# Take two lists, say for example these two:


# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
"""

"""
# Initially I came up with: 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

resulted_list = []

for element in a:
    if element in b:
        resulted_list.append(element)

#print( dict.fromkeys(resulted_list) )
resulted_list = list(dict.fromkeys(resulted_list))
print(resulted_list)
"""


import random

# random.sample ( population, k )

#Return a k length list of unique elements chosen from the population sequence or set.
# Used for random sampling without replacement.
# Returns a new list containing elements from the population while leaving the original population unchanged.
# The resulting list is in selection order so that all sub-slices will also be valid random samples.
# This allows raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices).

a = list(random.sample(range(40), 10 + random.randrange(4)))
b = list(random.sample(range(30), 10 + random.randrange(6)))

print(list(set(a).intersection(set(b))))

