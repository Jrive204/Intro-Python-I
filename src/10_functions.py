# Write a function is_even that will return true if the passed-in number is even.

def is_even(n):
    if n % 2 is 0:
        return print(f'{n} is Even') 
    else:
        return print(f'{n} is Odd') 
    

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

print(is_even(num))
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

