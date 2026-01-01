#Q5
a=input("enter the first number: ")
b=input("enter the second number: ")
a=int(a)
b=int(b)
sum=a+b
product=a*b
difference=a-b
print("sum", a + b)
print("product", a*b)
print("difference", a-b)
if a>b:
 print("The first number is bigger.")
elif a>b:
    print("The second number is bigger.")
else:
    print("Both numbers are equal.")