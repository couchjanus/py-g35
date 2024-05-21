# comment

a = 2
b = 2

# + - * / // % **
c = a + b

A = "hello"
# A123_rrr _abc x y a1 c3

print(c)
print(a, b, c, sep=":", end="\t")
print(c)

# name = input("Enter name: ")

# print(A, name)

x = int(input("Enter x: "))
y = int(input("Enter y: "))
o = input("Enter operation: ")

first = "sum" if o == '+' else "not sum"
print(first)

if o == '+':
    print("x + y = ", x + y) 
elif o == "-":
    print("x - y = ", x - y) 
else:
    print("Bad operation!")

match o:
    case "+":
        print("x + y = ", x + y) 
    case '-':
        print("x - y = ", x - y) 
    case _:
        print("Bad operation!")
        
