import os
import fight
import util


def title():
    util.clear_screen()
    fight.display_screen('''                                                                                                                                                                                                                                                                                                            
 ______            _        _______  _______  _______  _        _______ 
(  __  \ |\     /|( (    /|(  ____ \(  ____ \(  ___  )( (    /|(  ____ \ 
| (  \  )| )   ( ||  \  ( || (    \/| (    \/| (   ) ||  \  ( || (    \/
| |   ) || |   | ||   \ | || |      | (__    | |   | ||   \ | || (_____ 
| |   | || |   | || (\ \) || | ____ |  __)   | |   | || (\ \) |(_____  )
| |   ) || |   | || | \   || | \_  )| (      | |   | || | \   |      ) |
| (__/  )| (___) || )  \  || (___) || (____/\| (___) || )  \  |/\____) |
(______/ (_______)|/    )_)(_______)(_______/(_______)|/    )_)\_______)\n
   _______  _        ______     ______   _______  _______  _______  _        _______  _
  (  ___  )( (    /|(  __  \   (  __  \ (  ____ \(       )(  ___  )( (    /|(  ____ \( )
  | (   ) ||  \  ( || (  \  )  | (  \  )| (    \/| () () || (   ) ||  \  ( || (    \/| |
  | (___) ||   \ | || |   ) |  | |   ) || (__    | || || || |   | ||   \ | || (_____ | |
  |  ___  || (\ \) || |   | |  | |   | ||  __)   | |(_)| || |   | || (\ \) |(_____  )| |
  | (   ) || | \   || |   ) |  | |   ) || (      | |   | || |   | || | \   |      ) |(_)
  | )   ( || )  \  || (__/  )  | (__/  )| (____/\| )   ( || (___) || )  \  |/\____) | _ 
  |/     \||/    )_)(______/   (______/ (_______/|/     \|(_______)|/    )_)\_______)(_)
''')

    input('Press enter to continue')


def game_history():

    message = """


In forgotten land, that is so far away, that nobody remembers its name, a dragon appeared. 
Dragon summoned Demons and undead skeletons.
Those fearsome creatures started to terror people and their villages.
There is only one option to save the world.
The world needs a HERO to slay the DRAGON.


"""
    print(message)
    input("Press enter to continue: ")


def show_instructions():
    util.clear_screen()
    message = """INSTRUCTIONS:
WSAD - move
I - show inventory
C - enter cheat code
Q - quit


Legend:
E - Equipment
F - Food
G - Gate
K - Key
! - Baby demon
& - Skeleton
* - Warrior demon
D - Dragon
M - Milosc (xD)
? - NPC
# - Wall
@ - Player"""
    print(message)
    input("Press enter to go back to menu")
    util.clear_screen()


def show_authors():
    util.clear_screen()
    message = """Kornek Kamil - kamil.kornek96@gmail.com"""
    print(message)
    input("Press enter to go back to menu")
    util.clear_screen()


def welcome_screen():
    util.clear_screen()
    title()
    game_history()
    util.clear_screen()


def main_menu():
    print("1. Choose character\n2. Create character\n3. Instructions\n4. About Authors")
    choices = ['0', '1', '2', '3', '4']
    valid_choice = False
    while not valid_choice:
        choice = input("Choose game mode: ")
        if choice in choices:
            valid_choice = True
            if choice == "1":
                player = choose_character_menu()
            elif choice == "2":
                player = create_character_menu()
            elif choice == "3":
                show_instructions()
                player = main_menu()
            elif choice == "4":
                show_authors()
                player = main_menu()
            else:
                print("DUNGEONS & DEMONS\nTHE END")
        else:
            print("You have to press 1/2/0!")
    return player


def choose_character_menu():
    os.system('cls')
    valid_choice = False
    player1_character, player2_character, player3_character, player4_character, player5_character, player6_character, player7_character, player8_character, player9_character = done_players()
    choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    print(f'''1. {create_message_for_menu2(player1_character)}\n2. {create_message_for_menu2(player2_character)}\n3. {create_message_for_menu2(player3_character)}
4. {create_message_for_menu2(player4_character)}\n5. {create_message_for_menu2(player5_character)}\n6. {create_message_for_menu2(player6_character)}
7. {create_message_for_menu2(player7_character)}\n8. {create_message_for_menu2(player8_character)}\n9. {create_message_for_menu2(player9_character)}''')
    while not valid_choice:
        choice = input("Choose your character: ")
        if choice in choices:
            valid_choice = True
            if choice == "1":
                player = player1_character
            elif choice == "2":
                player = player2_character
            elif choice == "3":
                player = player3_character
            elif choice == "4":
                player = player4_character
            elif choice == "5":
                player = player5_character
            elif choice == "6":
                player = player6_character
            elif choice == "7":
                player = player7_character
            elif choice == "8":
                player = player8_character
            else:
                player = player9_character
        else:
            print("You have to press number of your character!")
    os.system('cls')
    print(f"Your character: {create_message_for_menu2(player)}")
    return player


def create_message_for_menu2(player_character):
    message_name = player_character["name"]
    message_race = player_character["race"]
    message_specialization = player_character["specialization"]
    message = f"Name: {message_name} | Race: {message_race} | Specialization: {message_specialization}"
    return message


def create_character_menu():
    os.system('cls')
    player_name = input("Choose your name: ")
    player_race = choose_race()
    player_specialization = choose_specialization()
    player = {"name": player_name, "race": player_race,
              "specialization": player_specialization}
    os.system('cls')
    print(f"Your character: {create_message_for_menu2(player)}")
    return player


def choose_race():
    race_possibilities = ["H", "D", "E"]
    race = False
    while not race:
        player_race = input(
            "Choose race (Human - H, Dwarf - D, Elf - E): ").upper()
        if player_race in race_possibilities:
            race = True
            if player_race == "H":
                player_race = "Human"
            elif player_race == "D":
                player_race = "Dwarf"
            else:
                player_race = "Elf"
        else:
            print("You have to choose your race(H/D/E)!")
    return player_race


def choose_specialization():
    specialization_possibilities = ["T", "B", "TH"]
    specialization = False
    while not specialization:
        player_specialization = input(
            "Choose specialization (Tank - T, Bruzer - B, Thief - TH): ").upper()
        if player_specialization in specialization_possibilities:
            specialization = True
            if player_specialization == "T":
                player_specialization = "Tank"
            elif player_specialization == "B":
                player_specialization = "Bruzer"
            else:
                player_specialization = "Thief"
        else:
            print("You have to choose your specialization(T/B/TH)!")
    return player_specialization


def done_players():
    player1_character = {"name": "Ulfrik",
                         "race": "Human", "specialization": "Bruzer"}
    player2_character = {"name": "Bauzer",
                         "race": "Human", "specialization": "Tank"}
    player3_character = {"name": "Klaus",
                         "race": "Human", "specialization": "Thief"}
    player4_character = {"name": "Gunter",
                         "race": "Dwarf", "specialization": "Bruzer"}
    player5_character = {"name": "Jimbo",
                         "race": "Dwarf", "specialization": "Tank"}
    player6_character = {"name": "Pablo",
                         "race": "Dwarf", "specialization": "Thief"}
    player7_character = {"name": "Eulalia",
                         "race": "Elf", "specialization": "Bruzer"}
    player8_character = {"name": "Sven",
                         "race": "Elf", "specialization": "Tank"}
    player9_character = {"name": "Troy",
                         "race": "Elf", "specialization": "Thief"}
    return(player1_character, player2_character, player3_character, player4_character, player5_character, player6_character, player7_character, player8_character, player9_character)


def player_statistics():
    player = main_menu()
    player = player_statistics_race(player)
    player = player_statistics_specialization(player)
    player["inventory"] = []
    return player


def player_statistics_race(player):
    if player["race"] == "Human":
        player["strength"] = 30
        player["luck"] = 30
        player["armor"] = 30
        player["health"] = 30
    elif player["race"] == "Dwarf":
        player["strength"] = 20
        player["luck"] = 20
        player["armor"] = 40
        player["health"] = 40
    else:
        player["strength"] = 40
        player["luck"] = 30
        player["armor"] = 20
        player["health"] = 30
    return player


def player_statistics_specialization(player):
    if player["specialization"] == "Tank":
        player["armor"] += 10
        player["health"] += 10
        player["start_position"] = [2, 2]
    elif player["specialization"] == "Bruzer":
        player["strength"] += 10
        player["health"] += 10
        player["start_position"] = [2, 2]
    else:
        player["luck"] += 10
        player["strength"] += 5
        player["health"] += 5
        player["start_position"] = [2, 2]
    return player


def create_message_for_statistics(player):
    player_strength = player["strength"]
    player_luck = player["luck"]
    player_armor = player["armor"]
    player_health = player["health"]
    message = f"Strength: {player_strength} | Luck: {player_luck} | Armor: {player_armor} | Health: {player_health}"
    return message


def player_statistics_display(player):
    message1 = create_message_for_menu2(player)
    message2 = create_message_for_statistics(player)
    print(message1)
    print(message2)
