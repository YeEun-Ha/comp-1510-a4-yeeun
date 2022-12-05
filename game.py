"""
YeEun Ha
A01298478
"""

import random
import itertools
import operator
import time


def intro():
    print("""
Welcome to Yennie's Journey Game🦄
The Journey Game is about an animal character😺 who is in the journey of 
saving its human buddy, Chris. He's captured in the Dark Castle!
""")


def name_character() -> str:
    character_name = input("➡ Name you character: ")
    return character_name


def explain_characters():
    print("""
There are 3 characters.
1. Cat 😺
   HP: 50, Attack power: 10, Skill: scratching
2. Dog 🐶 
   HP: 40, Attack power: 15, Skill: biting
3. Pig 🐷
   HP: 30, Attack power: 20, Skill: ripping up
""")


def add_user_to_character(user_name: str) -> list:
    cat = {'Character': 'cat', 'Face': '😺', 'HP': 60, 'Attack_power': 10, 'Skill': 'scratching'}
    dog = {'Character': 'dog', 'Face': '🐶', 'HP': 45, 'Attack_power': 15, 'Skill': 'biting'}
    pig = {'Character': 'lovely pig', 'Face': '🐷', 'HP': 30, 'Attack_power': 20, 'Skill': 'ripping up'}
    user_info = {'Name': user_name, 'Level': 'cute', 'Experience': 1, 'Location': (0, 0)}

    user_character_list = [dict(user_info, **cat), dict(user_info, **dog), dict(user_info, **pig)]
    return user_character_list


def get_user_input() -> int:
    while True:
        user_input = input("""What is your choice?
(1) Cat
(2) Dog
(3) Pig
""")
        if user_input in ['1', '2', '3']:
            return int(user_input)
        else:
            print("Oops! Please choose among the three numbers above.\n")


def make_character(user_name: str, user_input: int) -> dict:
    user_character_list = add_user_to_character(user_name)
    characters_with_index = dict(enumerate(user_character_list, 1))
    return characters_with_index[user_input]


def print_user_choice(character_dictionary: dict):
    print(f"\n🌻 Welcome, {character_dictionary['Name']} the "
          f"{character_dictionary['Character']}{character_dictionary['Face']}!")
    print("""
OK, let's go to the Dark Castle to save your buddy!
You will encounter some evil guards of the castle on the way.

Your level goes up from 'cute' to 'awesome' and 'The Greatness'. 
When you level up to The Greatness, you can combat the boss.
If you win, you will finally save your buddy! He is waiting for you.
Enjoy your journey🌻
""")
    print(f"[Status - Level: {character_dictionary['Level']}, Experience: {character_dictionary['Experience']}, "
          f"HP: {character_dictionary['HP']}, Attack power: {character_dictionary['Attack_power']}, "
          f"Skill: {character_dictionary['Skill']} ]")


def is_alive(character_dictionary: dict) -> bool:
    if character_dictionary['HP'] > 0:
        return True


# ----------Below is building the basic map----------------


def make_board(rows: int, columns: int) -> dict:
    description = ['Empty room', 'Yay! Hot tea🍵', 'Wow! Weapon🔪']
    coordinates_list = [(row, column) for row, column in itertools.product(range(rows), range(columns))]
    choices_list = [random.choice(description) for _ in range(len(coordinates_list))]
    board = dict(zip(coordinates_list, choices_list))
    return board


def make_map(rows: int, columns: int, character_dictionary: dict) -> str:
    map_list = []
    for row in range(rows):
        for column in range(columns):
            map_list.append('🔸')
        map_list.append('\n')
    map_list[0] = character_dictionary['Face']
    map_list[-2] = '🕌'
    return ''.join(map_list)


def describe_current_location(character_dictionary: dict, made_board: dict, made_map: str):
    user_location = character_dictionary['Location']
    print(made_map)
    print(f"Current location: {user_location}. There are: {made_board[user_location]}")

    if made_board[user_location] == 'Yay! Hot tea🍵':
        character_dictionary['HP'] += 2
        print(f"→ HP + 2! Current [HP]:{character_dictionary['HP']}")
    elif made_board[user_location] == 'Wow! Weapon🔪':
        character_dictionary['Attack_power'] += 1
        print(f"→ Attack power + 1! Current [Attack power]:{character_dictionary['Attack_power']}")
    else:
        return

# ----------Below is moving characters on the map----------------


def get_user_choice() -> tuple:
    north_south_east_west = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    coordinates = dict(enumerate(north_south_east_west, 1))  # {1: (0, -1), 2: (0, 1), 3: (1, 0), 4: (-1, 0)}
    while True:
        user_input = input("""
Which direction do you wanna go?
(1) North
(2) South
(3) East
(4) West
(10) Quit the game
""")
        if user_input == '10':
            print("OK, Bye!")
            quit()
        elif user_input in ['1', '2', '3', '4']:
            return coordinates[int(user_input)]  # type(coordinates[int(user_input)]) : <class 'tuple'>
        else:                                   # I don't know why the error says the type of it is int..
            print("Oops! Please choose among the four numbers above.\n")


def validate_move(row: int, column: int, character_dictionary: dict, user_input: tuple) -> bool:
    new_coordinate = tuple(map(operator.add, user_input, character_dictionary['Location']))
    if 0 <= new_coordinate[0] < row and 0 <= new_coordinate[1] < column:
        return True
    else:
        return False


def move_character(character_dictionary: dict, user_input: tuple):
    character_dictionary['Location'] = tuple(map(operator.add, user_input, character_dictionary['Location']))


def make_new_map(character_dictionary: dict, previous_map: str, row: int) -> str:
    map_list = list(previous_map)
    map_list[map_list.index(character_dictionary['Face'])] = '🔸'

    x_coordinate = character_dictionary['Location'][0]
    y_coordinate = character_dictionary['Location'][1]
    location_in_string_map = x_coordinate + y_coordinate * (row + 1)
    map_list[location_in_string_map] = character_dictionary['Face']
    return ''.join(map_list)


# ----------Below is about foes and experience ----------------


def foes_list() -> list:
    ghost = {'Name': 'Evil Ghost', 'Level': 1, 'Face': '👻', 'Attack_power': 5, 'HP': 20, 'Skill': 'chasing'}
    mask = {'Name': 'Evil Mask', 'Level': 1, 'Face': '👺', 'Attack_power': 5, 'HP': 20, 'Skill': 'cursing'}
    skeleton = {'Name': 'Evil Skeleton', 'Level': 2, 'Face': '💀', 'Attack_power': 6, 'HP': 25,
                'Skill': 'strong hugging'}
    dragon = {'Name': 'Evil Dragon', 'Level': 3, 'Face': '🐲', 'Attack_power': 7, 'HP': 30, 'Skill': 'throwing'}
    ai_robot = {'Name': 'Evil AI ', 'Level': 3, 'Face': '🤖', 'Attack_power': 7, 'HP': 30,
                'Skill': 'autonomous martial arts'}
    boss = {'Name': ' Alien the boss', 'Level': 10, 'Face': '👽', 'Attack_power': 20, 'HP': 100, 'Skill': 'laser beam'}
    enemies_list = [ghost, mask, skeleton, dragon, ai_robot, boss]
    return enemies_list


def what_foe(character_dictionary: dict, enemies_list: list) -> dict:
    if character_dictionary['Level'] == 'cute':
        cute_foes_list = list(filter(
            lambda element: element['Level'] == 1 or element['Level'] == 2, enemies_list))
        return random.choice(cute_foes_list)
    else:
        chosen_foes_list = list(filter(
            lambda element: element['Level'] == 2 or element['Level'] == 3, enemies_list))
        return random.choice(chosen_foes_list)


def is_there_challenge() -> bool:
    if random.randint(0, 2) == 1:
        return True
    else:
        return False


def fight_or_flee(foe_dictionary: dict) -> str:
    print(f"\nYou encountered {foe_dictionary['Name']}{foe_dictionary['Face']}! "
          f"It has {foe_dictionary['HP']}HP and {foe_dictionary['Attack_power']} attack power.\n")

    while True:
        user_input = input("""Do you want to fight or flee?: 
(1) Fight
(2) Flee        
""")
        if user_input == '1':
            return 'fight'
        elif user_input == '2':
            return 'flee'
        else:
            print("Oops! Please choose between the two numbers above.\n")


def fight(character_dictionary: dict, foe_dictionary: dict, attacker: str):
    if attacker == 'user':
        foe_dictionary['HP'] -= character_dictionary["Attack_power"]
        print(f"Your {character_dictionary['Skill']} LACERATES {foe_dictionary['Name']}.\n"
              f"{foe_dictionary['Name']}'s HP: {foe_dictionary['HP']}")
        time.sleep(1)
    else:
        character_dictionary['HP'] -= foe_dictionary["Attack_power"]
        print(f"{foe_dictionary['Name']}'s {foe_dictionary['Skill']} attacks you.\n"
              f"{character_dictionary['Face']}'s HP: {character_dictionary['HP']}")
        time.sleep(1)


def flee(foe_dictionary: dict):
    print(f"You managed to flee from {foe_dictionary['Name']}!")
    foe_dictionary['HP'] = 0


def earn_experience(character_dictionary: dict, foe_dictionary: dict):
    character_dictionary['Experience'] += 1
    print(f"✨ You defeated {foe_dictionary['Name']}! [Experience]: +1 ✨"
          f"\nYour current Experience: {character_dictionary['Experience']}"
          f"\nYour HP: {character_dictionary['HP']}, Attack power: {character_dictionary['Attack_power']}")
    if foe_dictionary['Level'] == 2:
        character_dictionary['Attack_power'] += 0.5
    elif foe_dictionary['Level'] == 3:
        character_dictionary['Attack_power'] += 1
    else:
        return


def check_level(made_character: dict):
    if made_character['Experience'] == 4:
        made_character['Level'] = 'awesome'
        made_character['Attack_power'] += 5
        made_character['HP'] += 10
        print("\n🎉 Congrats! Now you leveled up to 'awesome'🎉\n"
              "When you reach [Experience] 10, you will finally level up to 'The Greatness'!\n\n"
              "[Attack power]: +5, [HP]: +10\n"
              f"Current [Attack power]: {made_character['Attack_power']}. Current [HP]: {made_character['HP']}")
    elif made_character['Experience'] == 10:
        made_character['Level'] = 'The Greatness'
        made_character['Attack_power'] += 5
        made_character['HP'] += 10
        print("🎉 Congrats! Now you leveled up to 'The Greatness'🎉\n"
              "Let's go to the Dark Castle to save your buddy!\n\n[Attack power]: +5, [HP]: +10, "
              f"Current [Attack power]: {made_character['Attack_power']}. Current [HP]: {made_character['HP']}")
    else:
        return


def execute_challenge_protocol(character_dictionary: dict, foe_dictionary: dict, user_decision: str):
    attacker_generator = itertools.cycle(["user", "foe"])
    while foe_dictionary['HP'] > 0 and character_dictionary['HP'] > 0:
        if user_decision == 'fight':
            fight(character_dictionary, foe_dictionary, next(attacker_generator))
            if foe_dictionary['HP'] <= 0:
                earn_experience(character_dictionary, foe_dictionary)
                check_level(character_dictionary)
        else:
            flee(foe_dictionary)


def hp_back(foe_dictionary:  dict):
    if foe_dictionary['Level'] == 1:
        foe_dictionary['HP'] = 20
    elif foe_dictionary['Level'] == 2:
        foe_dictionary['HP'] = 25
    else:
        foe_dictionary['HP'] = 30


def defeat_boss(made_character: dict):
    boss = foes_list()[-1]
    print(f"You finally encountered {boss['Name']}{boss['Face']}! It has {boss['HP']}HP and {boss['Attack_power']} attack power.\n")

    attacker_generator = itertools.cycle(["user", "foe"])
    while boss['HP'] > 0 and made_character['HP'] > 0:
        fight(made_character, boss, next(attacker_generator))
        if boss['HP'] <= 0:
            return True


def end_of_game(made_character: dict):
    if is_alive(made_character):
        print(f" You defeated the evil boss, brave {made_character['Name']} the {made_character['Character']}!")
        print("✨ Oh, there's your buddy, Chris! Go hug him! 🌻")
        print("""
✄╔═╗───────────╔╗───────╔╗╔╗
✄║╔╬═╦═╦╦═╦╦╦═╗║╚╦╦╦╗╔═╗║╚╬╬═╦═╦╗
✄║╚╣╬║║║║╬║╔╣╬╚╣╔╣║║╚╣╬╚╣╔╣║╬║║║║
✄╚═╩═╩╩═╬╗╠╝╚══╩═╩═╩═╩══╩═╩╩═╩╩═╝
✄───────╚═╝
        """)
        print("🎀🌻🎀🌻🎀🌻🎀🌻🎀🌻🎀🌻🎀🌻🎀🌻🎀🌻🎀")
    else:
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⢀⣤⣤⣤⣶⣶⣷⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⠀⠀⠀⠀⣠⣾⣿⣿⡇⠀⣿⣿⣿⣿⠿⠛⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⢀⣿⣿⣶⡀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⢀⣴⣿⣿⣿⣿⠁⢸⣿⣿⣿⣀⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⢰⣿⣿⣿⣿⣇⣠⣿⣿⣿⣿⣿⡏⢠⣿⣿⣿⣿⣿⡿⠗⠂⠀⠀
⠀⠀⠀⣰⣾⣿⣿⠟⠛⠉⠉⠉⠉⠋⠀⠀⠀⣰⣿⣿⣿⣿⣿⣇⣠⣤⣤⣿⣿⣿⢿⣿⣿⣿⣿⢿⣿⣿⡿⠀⣼⣿⣿⡟⠉⠁⢀⣀⡄⠀⠀
⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣴⣿⣿⣿⣿⡿⣿⣿⣿⡏⠈⢿⣿⣿⠏⣾⣿⣿⠃⢠⣿⣿⣿⣶⣶⣿⣿⣿⡷⠦⠀
⢠⣾⣿⡿⠀⠀⠀⣀⣠⣴⣶⣿⣿⡷⠀⣠⣿⣿⣿⣿⡿⠟⣿⣿⣿⣠⣿⣿⣿⠀⠀⠀⠀⠁⢸⣿⣿⡏⠀⣼⣿⣿⣿⠿⠛⠛⠉⠀⠀⠀⠀
⢸⣿⣿⠣⣴⣾⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⠋⠁⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠸⠿⠿⠀⠀⠛⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣆⣉⣻⣭⣿⣿⣿⡿⠋⠀⠀⢿⣿⡿⠁⠀⠀⠀⠀⠀⠹⠟⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣶⣶⣦⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠄⣤⣤⣤⣤⣶⣾⣷⣴⣿⣿⣿⣿⠿⠿⠛⣻⣿⣿⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⠀⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⢠⣿⣿⣿⠿⠛⠋⠉⠛⣿⣿⣿⠏⢀⣤⣾⣿⣿⡿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⠓⢹⣿⣿⣷⠀⠀⠀⠀⢀⣶⣿⡿⠁⠀⣾⣿⣿⣟⣠⣤⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⡟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠛⠉⠸⣿⣦⡈⣿⣿⣿⡇⠀⠀⣰⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⣿⠿⠷⢀⣿⣿⣿⣿⡿⠛⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⣧⠘⣿⣿⣿⡀⣼⣿⣿⡟⠀⠀⢀⣿⣿⣿⠋⠁⠀⣀⣀⣼⣿⣿⡟⠁⠀⠀⠘⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⣠⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⡟⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀
⠀⠀⠀⠀⢹⣿⣿⣇⠀⠀⢀⣠⣴⣿⣿⣿⡿⠀⠈⣿⣿⣿⣿⡟⠀⠀⠀⢰⣿⣿⣿⠿⠟⠛⠉⠁⠸⢿⡟⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣿⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠸⣿⣿⡿⠁⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

Sorry, you died...
Chris is crying for you...
But who knows? You might be able to reborn and defeat the boss! 
-- Game Over --
""")


def game():
    intro()
    user_name = name_character()
    explain_characters()
    input_result = get_user_input()
    character = make_character(user_name, input_result)
    print_user_choice(character)

    rows = 5
    columns = 5
    board_description = make_board(rows, columns)
    board_map = make_map(rows, columns, character)
    describe_current_location(character, board_description, board_map)

    all_foes_list = foes_list()
    boss_die = False
    while is_alive(character) and not boss_die:
        direction_input = get_user_choice()
        is_valid = validate_move(rows, columns, character, direction_input)
        if is_valid:
            move_character(character, direction_input)
            board_map = make_new_map(character, board_map, rows)
            describe_current_location(character, board_description, board_map)
            if character["Location"] == (4, 4):
                if character['Level'] == 'The Greatness':
                    boss_die = defeat_boss(character)
                else:
                    print("It's the boss, but you first need to level up to The Greatness.")
            else:
                if is_there_challenge():
                    chosen_foe_dictionary = what_foe(character, all_foes_list)
                    fight_decision = fight_or_flee(chosen_foe_dictionary)
                    execute_challenge_protocol(character, chosen_foe_dictionary, fight_decision)
                    hp_back(chosen_foe_dictionary)
        else:
            print("\nYou can't go there! Choose another direction.")
    end_of_game(character)

def main():
    game()


if __name__ == '__main__':
    main()
