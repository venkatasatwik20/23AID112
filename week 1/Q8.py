#Q8
# Traffic Light Simulator
signal = input("Enter traffic light color: ")
if signal == "red":
    print("STOP!")
elif signal == "yellow":
    print("Prepare to stop")
elif signal == "green":
    print("You can go")
else:
    print("Wrong input!")
