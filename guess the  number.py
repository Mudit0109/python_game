from random import randint
# intiate level or stage as 1 
level = 1
#sequence type to store points
points = [100,75,50,25,10]
#initial score is zeero
points_scored = 0
#loop for 3stages
while level <= 3:
    #complexity range for each stage
    end_value = level * 10
    #secret number generation
    secret_number = randint(1,end_value)
    #looping statment for 5 attempts at each stage
    for counter in range(0,5):
        #gets the guessing number as user input
        guess_number = int(input("Guess the secret number between 1 and {} ({} attempts left):".format(end_value,5-counter)))
        #check guessing number is correct or higher or lower
        if secret_number == guess_number:
            print("Your Guess is Correct, You Won the level {} with {} points".format(level,points[counter]))
            points_scored += points[counter]
            level = level + 1
            break
        elif guess_number < secret_number:
            print("Your Guess is lower than secret number")
        else:
            print("Your Guess is higher than secret number")
    else:#else of for statement
        print("Game Over, You Loose the Game, secret number is {}".format(secret_number))
        break
else:#else of while statement
    print("Congratz, You Won the Game with {} !!!".format(points_scored))
