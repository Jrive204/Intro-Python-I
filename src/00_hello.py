# # Print "Hello, world!" to your terminal
# print("Hello, world!")
# fruits = ["Apple", "Banana"]

# # 1. append()
# print(f'Current Fruits List {fruits}')

# f = input("Please enter a fruit name:\n")
# fruits.append(f)

# print(f'Updated Fruits List {fruits}')

# t = (1, 2, 5, 7, 99)
# def hello(t):
#     for i in t:
#         print (i)
# print(range(len(t)),"HELLO")
# print(hello(t))

# for i in range(20): 
#     print(i, end = " ") 

# stuff = round(59*.5)
# print(12**12 /12)

# def primeNumbers(endRange):
#     nonPrime = []
#     Prime = []
#     for x in range(2,endRange +1):
#         for i in range(2,endRange +1):
#             num= x*i 
#             if num not in nonPrime:
#                 nonPrime.append(num)
#     for x in range (2,endRange +1):
#         if x not in nonPrime:
#             Prime.append(x)
#     return Prime

# print(primeNumbers(7))

def primeNumbers(endRange):
    if endRange < 2:
        return "Range has to be 2 or Greater"
    nonPrime = []
    Prime = []
    for x in range(2,endRange +1):
        for i in range(2,endRange +1):
            num= x*i 
            nonPrime.append(num)
            if  x  not in Prime  and x not in nonPrime:
                Prime.append(x)
    return Prime

primelist = input("Please enter a number to check prime range:\n")


print(primeNumbers(int(primelist)))


