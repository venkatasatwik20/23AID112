#Q18
secret_number = 7
guess = int(input("Guess the secret number : "))
while guess != secret_number:  
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:   
        print("Congratulations! You guessed it right.")
    guess = int(input("Guess the secret number: "))
print("Congratulations! You guessed it right.")