import random

from menuItems import *
from pokemon import get_pokemon
from replit import clear

pokemon_list = get_pokemon()

def play():
    playing = True
    while playing:
        score = 0
        guessing = True
        while guessing:

            clear()
            print(name)

            #Get pokemon
            poke1 = assign()
            poke2 = assign()

            #Second loop, for round >1
            if score > 0:
                poke1 = poke2
                poke2 = assign()

            #in the case we get the same pokemon
            if poke1 == poke2:
                poke2 = assign()

            print(f"Pokemon: {poke1['name']}")

            print(VS)

            print(f"Pokemon: {poke2['name']}")

            print("----------------------------------------------")
            print(f"Your score is: {score}")
            print("----------------------------------------------")

            guess = input("Guess the pokemon with the highest (newest pokemon) id: ")

            if compare(poke1, poke2, guess):
                score += 1
            else:
                guessing = False
                if poke1["id"] > poke2["id"]:
                    print(f"Nice try! The correct answer is {poke1['name']}")
                else:
                    print(f"Nice try! The correct answer is {poke2['name']}")

        play_again = input("Would you like to play again? (y/n): ").lower()

        if play_again == "y":
            continue
        elif play_again == "n":
            playing = False
            clear()
            print("Thank you for playing!")
        else:
            playing = False
            print("Invalid input. Assuming no.")



def assign():
    return random.choice(pokemon_list)

def compare(p1,p2, user_input):
    poke1 = p1["id"]
    poke2 = p2["id"]
    higher = ""

    if poke1 > poke2:
        higher = p1["name"]
    elif poke1 < poke2:
        higher = p2["name"]

    if user_input == higher:
        return True
    else:
        return False

start = input("Do you want to play Higher or Lower: Pokemon edition? (y/n)\n").lower()
if start == "y":
    clear()
    play()
elif start == "n":
    print("Thank you for playing!")
else:
    print("Please enter y or n\n")
