print("Hello World...")

x = 5
y = "Automation"

print(x)
print(y)

print("Hello " + y)

x = 10
y = 20
print (x+y)

if 10 > 5 :
    print("10 is greater than 5")
    
def sum(a,b): 
    print(a+b)
    
x = sum(10,20)

x = 5
y = 2.5
z = 4j

print(type(x))
print(type(y))
print(type(z))

x = int(2)
y = int(2.4)
z = float(1)
p = str(10)

print(x)
print(y)
print(z)
print(p)

print("Enter your full name:")
x = input()
print("Welcome To Our Course " + x)

if 5 > 2 :
    print("5 is greater than 2")
    
num = 0
if num > 1 :
    print("Number is greater than 1")
elif num == 0 :
    print("Number is equal to 0")
else:
    print("Number is negative Number")
    
num = [1,2,3,4,5]
sum = 0
for val in num:
    sum = sum + val
print("Total is",sum)

fruits = ["apple","kivi","grapes"]
for val in fruits:
    print(val)
else:
    print("No fruits sorry")

print("Enetr Number:")   
i = 0
sum = 0
num = int(input())
while i<num:
    sum = sum + i
    i = i + 1
print("Total is:", sum)