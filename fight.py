import random
import util
import time
import player_menu
import tabulate
import sys


def fight_window(player_bar, monster_bar):
    fight_window = (f'''+--------------------------------------------------------------------------+
|                                                                          |
|        YOU: {player_bar}                      ENEMY: {monster_bar}            |
|             ___                                   ___                    |
|            |===|                                 |===|                   |
|            |___|                                 |___|                   |
|      ___  /#####\                               /#####\  ___             |
|     |   |//#####\\\                             //#####\\\|   |            |
|     |(₡)|/ ##### \\\                           // ##### \|(₡)|            |
|     |   |  ^^^^^  &[═══════           ═══════]&  ^^^^^  |   |            |
|      \_/   |#|#|                                 |#|#|   \_/             |
|            |_|_|                                 |_|_|                   |
|            [ | ]                                 [ | ]                   |
+--------------------------------------------------------------------------+
| HP: {player_bar} || ATTACK (1) || FOOD (2)                                 |
+--------------------------------------------------------------------------+''')
    print(fight_window)


def fight_window_hit(player_bar, monster_bar, player_hit, monster_hit):
    window_space = ' '*int(38-(len(str(monster_hit))+len(str(player_hit))))
    fight_window = (f'''+--------------------------------------------------------------------------+
|                   -{monster_hit}{window_space}-{player_hit}               |
|        YOU: {player_bar}                      ENEMY: {monster_bar}            |
|             ___                                   ___                    |
|            |===|                                 |===|                   |
|            |___|                                 |___|                   |
|      ___  /#####\                               /#####\  ___             |
|     |   |//#####\\\                             //#####\\\|   |            |
|     |(₡)|/ ##### \\\                           // ##### \|(₡)|            |
|     |   |  ^^^^^  &[═══════           ═══════]&  ^^^^^  |   |            |
|      \_/   |#|#|                                 |#|#|   \_/             |
|            |_|_|                                 |_|_|                   |
|            [ | ]                                 [ | ]                   |
+--------------------------------------------------------------------------+
| HP: {player_bar} || ATTACK (1) || FOOD (2)                                 |
+--------------------------------------------------------------------------+''')
    print(fight_window)


def fight_window_heal(player_bar, monster_bar, player_hit, monster_hit):
    window_space = ' '*int(40-(len(str(monster_hit))))
    fight_window = (f'''+--------------------------------------------------------------------------+
|                   +{monster_hit}{window_space}               |
|        YOU: {player_bar}                      ENEMY: {monster_bar}            |
|             ___                                   ___                    |
|            |===|                                 |===|                   |
|            |___|                                 |___|                   |
|      ___  /#####\                               /#####\  ___             |
|     |   |//#####\\\                             //#####\\\|   |            |
|     |(₡)|/ ##### \\\                           // ##### \|(₡)|            |
|     |   |  ^^^^^  &[═══════           ═══════]&  ^^^^^  |   |            |
|      \_/   |#|#|                                 |#|#|   \_/             |
|            |_|_|                                 |_|_|                   |
|            [ | ]                                 [ | ]                   |
+--------------------------------------------------------------------------+
| HP: {player_bar} || ATTACK (1) || FOOD (2)                                 |
+--------------------------------------------------------------------------+''')
    print(fight_window)


def health_bar(player, monster):
    player_h = int(player['health']/10)
    monster_h = int(monster['health']/10)
    player_bar = []
    monster_bar = []
    for i in range(player_h):
        player_bar.append('▓')
    for i in range(10-player_h):
        player_bar.append('░')
    for i in range(monster_h):
        monster_bar.append('▓')
    for i in range(10-monster_h):
        monster_bar.append('░')
    player_bar = "".join(player_bar)
    monster_bar = "".join(monster_bar)
    return player_bar, monster_bar


def attack(player, monster):
    player_hit = random.randint(
        int(player['strength']/4), int(player['strength']/2))
    monster_hit = random.randint(
        int(monster['strength']/4), int(monster['strength']/2))
    player_def = random.randint(
        int(player['armor']/20), int(player['armor']/10))
    monster_def = random.randint(
        int(monster['armor']/20), int(monster['armor']/10))
    if player_hit > monster_def:
        player_hit = player_hit - monster_def
    else:
        player_hit = 0
    if monster_hit > player_def:
        monster_hit = monster_hit - player_def
    else:
        monster_hit = 0
    monster['health'] -= player_hit
    player['health'] -= monster_hit
    return player_hit, monster_hit


def heal(player, food):
    player['health'] += food
    if player['health'] > 100:
        food = food - (player['health']-100)
        player['health'] = 100
    return food


def display_screen(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(0.0001**100)
    print('')


def game_over():
    util.clear_screen()
    display_screen(""" 
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
   _______  _______  _______  _______    _______           _______  _______  _ 
  (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )( )
  | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|| |
  | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|| |
  | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)| |
  | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   (_)
  | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__ _ 
  (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/(_)
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                                
    """)

    input('Press enter to continue')


def game_finished():
    util.clear_screen()
    display_screen('''
            _______                      _______  _        _                                                
    |\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /|( )                                               
    ( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( || |                                               
     \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | || |                                               
      \   /  | |   | || |   | |  | |( )| || |   | || (\ \) || |                                               
       ) (   | |   | || |   | |  | || || || |   | || | \   |(_)                                               
       | |   | (___) || (___) |  | () () || (___) || )  \  | _                                                
       \_/   (_______)(_______)  (_______)(_______)|/    )_)(_)                                               
                                                                                                                                                                                                                                                                                                                                                                                         
  ''')

    input('Press enter to continue')


def fight(player, monster):
    while player['health'] > 0 and monster['health'] > 0:
        player_bar, monster_bar = health_bar(player, monster)
        fight_window(player_bar, monster_bar)
        player_menu.player_statistics_display(player)
        print("====================================================")
        monster_stats = f"Name: {monster['name']} | Type: {monster['type']}\nStrength: {monster['strength']} | Luck: {monster['luck']} | Armor: {monster['armor']} | Health: {monster['health']}"
        print(monster_stats)
        action = input('Choose action:')
        util.clear_screen()
        if action == 'i':
            print(tabulate.tabulate(
                player['inventory'], headers='keys', tablefmt='fancy_grid', showindex=True))
            input('Press enter to exit inventory')
            util.clear_screen()
        if action in ['1', '2']:
            if action == '2':
                food_to_eat = []
                for items in player['inventory']:
                    if items['type'] == 'cure':
                        food_to_eat.append(items)
                        player['inventory'].remove(items)
                if len(food_to_eat) > 0:
                    for i in range(1):
                        health_to_add = food_to_eat[0]['health']
                    player_heal = heal(player, health_to_add)
                    player_hit, monster_hit = 0, player_heal
                    fight_window_heal(player_bar, monster_bar,
                                      player_hit, monster_hit)
                    player_menu.player_statistics_display(player)
                    print("====================================================")
                    monster_stats = f"Name: {monster['name']} | Type: {monster['type']}\nStrength: {monster['strength']} | Luck: {monster['luck']} | Armor: {monster['armor']} | Health: {monster['health']}"
                    print(monster_stats)
                    time.sleep(2)
                    util.clear_screen()
                else:
                    fight_window(player_bar, monster_bar)
                    player_menu.player_statistics_display(player)
                    print("====================================================")
                    monster_stats = f"Name: {monster['name']} | Type: {monster['type']}\nStrength: {monster['strength']} | Luck: {monster['luck']} | Armor: {monster['armor']} | Health: {monster['health']}"
                    print(monster_stats)
                    print('You have no food!')
                    time.sleep(2)
                    util.clear_screen()
            if action == '1':
                player_hit, monster_hit = attack(player, monster)
                fight_window_hit(player_bar, monster_bar,
                                 player_hit, monster_hit)
                player_menu.player_statistics_display(player)
                print("====================================================")
                monster_stats = f"Name: {monster['name']} | Type: {monster['type']}\nStrength: {monster['strength']} | Luck: {monster['luck']} | Armor: {monster['armor']} | Health: {monster['health']}"
                print(monster_stats)
                time.sleep(2)
                util.clear_screen()
        else:
            print('You must type 1 - Attack or 2 - Food')
            continue
    monster_stats = f"Name: {monster['name']} | Type: {monster['type']}\nStrength: {monster['strength']} | Luck: {monster['luck']} | Armor: {monster['armor']} | Health: {monster['health']}"
    if player['health'] <= 0:
        fight_window(player_bar, monster_bar)
        player_menu.player_statistics_display(player)
        print("====================================================")
        print(monster_stats)
        print('You loose fight!')
        game_over()
        util.clear_screen()
        return False
    if monster['health'] <= 0:
        fight_window(player_bar, monster_bar)
        player_menu.player_statistics_display(player)
        print("====================================================")
        print(monster_stats)
        input('You won fight! Press enter to continue')
        util.clear_screen()
        return True
