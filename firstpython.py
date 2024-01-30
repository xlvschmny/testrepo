#hello i am under the water
mystery_player = "Alfredo Di Canio"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("I am a football player hailing from Italy. ")
print("I played for one of the London clubs in the Premier League. ")
print("At some point in my career, I was suspended for an offensive celebration. ")
print("Who am I?")

while guess != mystery_player and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
        if guess != mystery_player:
            print("Wrong guess!")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, you lose.")
else:
    print("You win!")
