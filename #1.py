"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral
number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

# We should first get input form user
number = int(input('Please enter a number:'))

# We should also need a loop from 1 to our n

# We will use a count variable to loop
count = 1

# We declare the dictionary here
dictionary = {}

while count <= number:
    # Dictionary of count should be count * count
    dictionary[count] = count*count

    count += 1

print(dictionary)
