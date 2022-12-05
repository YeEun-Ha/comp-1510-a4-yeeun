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
    cat = {'Character': 'cat', 'Face': '😺', 'HP': 50, 'Attack_power': 10, 'Skill': 'scratching'}
    dog = {'Character': 'dog', 'Face': '🐶', 'HP': 40, 'Attack_power': 15, 'Skill': 'biting'}
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
    print(f"\n🌻 Welcome, {character_dictionary['Name']} the {character_dictionary['Character']}{character_dictionary['Face']}!")
    print("""
OK, let's go to the Dark Castle to save your buddy!
You will encounter some evil guards of the castle on the way.

Your level goes up from 'cute' to 'awesome' and 'The Greatness'. 
When you level up to The Greatness, you can combat the boss.
If you win, you will finally save your buddy! He is waiting for you.
Enjoy your journey🌻
""")
    print(f"[Status - Level: {character_dictionary['Level']}, Experience: {character_dictionary['Experience']}, "
          f"HP: {character_dictionary['HP']}, Attack power: {character_dictionary['Attack_power']}, Skill: {character_dictionary['Skill']} ]")


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
    North_South_East_West = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    coordinates = dict(enumerate(North_South_East_West, 1))  # {1: (0, -1), 2: (0, 1), 3: (1, 0), 4: (-1, 0)}
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
            return coordinates[int(user_input)] # type(coordinates[int(user_input)]) : <class 'tuple'>
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


def make_new_map(character_dictionary:dict, previous_map: str, row: int) -> str:
    map_list = list(previous_map)
    map_list[map_list.index(character_dictionary['Face'])] = '🔸'

    x_coordinate = character_dictionary['Location'][0]
    y_coordinate = character_dictionary['Location'][1]
    location_in_string_map = x_coordinate + y_coordinate * (row + 1)
    map_list[location_in_string_map] = character_dictionary['Face']
    return ''.join(map_list)


def game(): # called from main
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

    boss_die = False
    while is_alive(character) and not boss_die:
        direction_input = get_user_choice()
        is_valid = validate_move(rows, columns, character, direction_input)
        if is_valid:
            move_character(character, direction_input)
            board_map = make_new_map(character, board_map, rows)
            describe_current_location(character, board_description, board_map)
        else:
            print("\nYou can't go there! Choose another direction.")


def main():
    game()


if __name__ == '__main__':
    main()

