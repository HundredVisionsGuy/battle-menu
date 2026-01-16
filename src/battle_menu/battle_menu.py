"""
battle_menu.py
by Chris Winikka
A menu of options for a battle sequence in an RPG with various random outcomes

1. Greet the user (name of program and purpose)
2. Set the user's stats (health, strength, attack, etc.)
3. Set one or more enemies stats (health, strength, attack, etc.)
4. Present a menu of options (I will save the full menu as a variable)
5. Use a loop to continue presenting the menu and giving the user a choice.
6. User can attack, defend, run away, or quit.
7. Use the user choice to decide what happens.
8. If the user attacks, deal random damage to enemy.
9. If the enemy still has health, have the enemy attack (or defend or run 
   away).
10. If the enemy attacks, give damage to player
11. If all enemies die or run away, end the loop and congratulate the user.
12. If the user dies, end the loop and pronounce the user's failure and death
    (was it honorable?)
13. Display both the enemy's (or enemies') and user's stats
14. Repeat step 4 and continue
15. Thank the user and quit
"""

import os
import time
import random


def main():
    print("Welcome")

    # Display prompt and wait for user
    input("Press enter to clear screen")

    # clear the console screen
    os.system('cls')

    # delay release of output (random numbers from 0 and up to 10 at most)
    for i in range(random.randrange(10)):
        print(i)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
