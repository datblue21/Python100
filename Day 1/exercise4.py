'''Write a program that switches the values stored in the variables a and b.'''

# a, b = map(int, input().split(" "))
# c1:
a = input("a=")
b = input("b=")
#c2
a = a+b
b = a -b
a = a - b
a, b = b, a
print(a, b)
