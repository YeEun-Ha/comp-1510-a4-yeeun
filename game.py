"""
YeEun Ha
A01298478
"""


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


def game(): # called from main
    intro()
    user_name = name_character()
    explain_characters()
    input_result = get_user_input()
    dictionary_of_character = make_character(user_name, input_result)
    print_user_choice(dictionary_of_character)

    rows = 5
    columns = 5


def main():
    game()


if __name__ == '__main__':
    main()

