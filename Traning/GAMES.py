capital_guess = input("What is the capital of Ireland?")
number_of_guesses = 1

while capital_guess != "Dublin":
    number_of_guesses = number_of_guesses + 1
    if number_of_guesses > 3:
        print("You guessed incorrectly three times. Game over.")
        
    capital_guess = input("Guess again. ")
if number_of_guesses <= 3:
    print("You guessed it. Dublin is the capital of Ireland.")


    


