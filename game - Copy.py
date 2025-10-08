import random
print("welcome to the game")
secret_number = random.randint(1,10)
for guess in range(3):
    guess=int(input("enter your value"))
    if guess==secret_number:
        print("you are win")
    elif guess>secret_number:
        print("didn't close to the number")
    elif guess<secret_number:
        print("close to the number")
    else:
        print("you lose the game")