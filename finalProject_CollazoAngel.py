# Angel Collazo

# December 10, 2025

# Final Project

# A simple text fight game where the player will comfront the Chupa Cabras and the game will end in Victory,Defeat
#or Quit.



import random
import time
# Player will create his character
def create_character():
    name = input("Enter your character's name: ")
    return {
        "name": name,
        "life": 100,
        "muscle": random.randint(5, 15),
        "inventory": {"Potion": 2}
    }

def display_character(character):
    print("\nCharacter Stats:")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

def punch(attacker, defender):
    damage = random.randint(1, attacker["muscle"])
    defender["life"] -= damage
    return damage

def enemy_attack(enemy, player):
    damage = random.randint(1, enemy["muscle"])
    player["life"] -= damage
    print(f"{enemy['name']} hits you for {damage} damage!")
    return damage

def use_item(player):
    if player["inventory"]["Potion"] > 0:
        player["life"] = min(player["life"] + 20, 100)
        player["inventory"]["Potion"] -= 1
        print("You used a potion and recovered 20 life!")
    else:
        print("No potions left!")

def main():
    print("Welcome to the FIGHT Game")
    player = create_character()
    display_character(player)

    # Player will select difficulty
    difficulty = input("\nChoose difficulty: Easy / Hard > ").lower()
    if difficulty == "hard":
        enemy = {"name": "Chupa Cabras", "life": 80, "muscle": 12}
    else:
        enemy = {"name": "Chupa Cabras", "life": 50, "muscle": 8}

    while True:
        print("\nChoose an action: [1] Punch [2] Block [3] Use Potion [4] Quit")
        choice = input("> ")

        if choice == "1":
            dmg = punch(player, enemy)
            print(f"You hit the {enemy['name']} for {dmg} damage!")
            time.sleep(1)

            if enemy["life"] <= 0:
                print("You defeated the enemy!")
                break

            # Chupa Cabras counterattack
            enemy_attack(enemy, player)
            if player["life"] <= 0:
                print("You were defeated... Game Over!")
                break

        elif choice == "2":
            player["life"] = min(player["life"] + 10, 100)
            print("You block and recover +10 life.")
            time.sleep(1)
            enemy_attack(enemy, player)
            if player["life"] <= 0:
                print("You were defeated... Game Over!")
                break

        elif choice == "3":
            use_item(player)
            time.sleep(1)
            enemy_attack(enemy, player)
            if player["life"] <= 0:
                print("You were defeated... Game Over!")
                break

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice, try again.")

        # Show updated stats
        print(f"\n{player['name']} Life: {player['life']} | {enemy['name']} Life: {enemy['life']}")

if __name__ == "__main__":
    main()

# PSEUDO CODE:
# START GAME
#   - Create player (name, life, muscle, potions)
#   - Choose difficulty → set enemy stats
#
# BATTLE LOOP
#   - Player chooses: Punch / Block / Use Potion / Quit
#       * Punch → damage enemy, check win → else enemy attacks
#       * Block → heal +10, then enemy attacks
#       * Potion → heal +20 if available, then enemy attacks
#       * Quit → end game
#       * Invalid → retry
#
# ENEMY ATTACK
#   - Enemy deals random damage each turn
#   - If player life ≤ 0 → Game Over
#
# END GAME
#   - Victory if enemy life ≤ 0
#   - Defeat if player life ≤ 0
#   - Quit ends game early

