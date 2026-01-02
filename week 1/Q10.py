#Q10
celsius =int(input("Enter the temperature in Celcius : "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

if celsius < 0:
    print("Very cold! Wear thick jacket")
elif 0 <= celsius <= 15:
    print("Cold. Wear jacket")
elif 16 <= celsius <= 25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")
