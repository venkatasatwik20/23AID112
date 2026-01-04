#Q17
import random
numbers = [random.randint(1, 100) for _ in range(8)]
biggest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
    if num < smallest:
        smallest = num
print("List:", numbers)
print("Biggest number:", biggest)
print("Smallest number:", smallest)
