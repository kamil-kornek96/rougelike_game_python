import random
import fight
import util
import player_items


def create_board(width, height):
    top_edge = ['#']*width
    botom_edge = ['#']*width
    middle = ['#'] + ['.']*(width - 2) + ['#']
    board = []
    board.append(top_edge)
    for row in range(height-2):
        board.append(middle.copy())
    board.append(botom_edge)
    return board


def put_player_on_board(board, player, marker):
    if isinstance(player, dict):
        board[player['start_position'][0]][player['start_position'][1]] = marker
    else:
        board[player[0]][player[1]] = marker


def making_gate(board, map_level):
    if map_level == 1:
        board[-1][15] = 'G0'

    elif map_level == 2:
        board[-1][15] = 'G1'
        board[0][18] = 'G2'
        pass
    elif map_level == 3:
        board[0][18] = 'G3'
        pass
    return board


def object_placement(board, number, width, height, mark):
    while number >= 0:
        object_h = random.randint(2, height-2)
        object_w = random.randint(2, width-2)
        if number == 0:
            break

        elif board[object_h][object_w] == '.':
            board[object_h][object_w] = mark
            number -= 1
    return (board, [object_h, object_w])


# check that move was correct, returns what interactions will be performed and previous position coords
def player_movement(key, player, board,):
    key = key.lower()
    previous_position = player['start_position'].copy()
    if key == 'w':
        player['start_position'][0] -= 1
    if key == 's':
        player['start_position'][0] += 1
    if key == 'd':
        player['start_position'][1] += 1
    if key == 'a':
        player['start_position'][1] -= 1
    correct_movement, interaction = check_correct_movement(
        board, player['start_position'], player['inventory'])
    return correct_movement, interaction, previous_position


def perform_action(interaction, player, baby_demon, skeleton, warrior_demon, dragon, map_level):
    if interaction in ['!', '&', '*', 'D']:
        monsters = baby_demon, skeleton, warrior_demon, dragon
        if interaction == '!':
            monster = monsters[0]
        if interaction == '&':
            monster = monsters[1]
        if interaction == '*':
            monster = monsters[2]
        if interaction == 'D':
            monster = monsters[3]
        player_won = fight.fight(player, monster)
        return player_won
    if interaction in ['F', 'E', 'K', 'K1', 'K2', ]:
        player_items.add_items(interaction, player)
    if interaction == 'M':
        player_items.add_strong_sword(interaction, player)
    if interaction == '?' and map_level == 0:
        util.clear_screen()
        npc_message(map_level, player['inventory'])
        input("Press enter twice to continue")
    if interaction == '?' and map_level == 1:
        util.clear_screen()
        npc_message(map_level, player['inventory'])
        input("Press enter twice to continue")


def check_correct_movement(board, position, inventory):
    is_key_in_inventory = False
    is_key1_in_inventory = False
    for item in inventory:
        if item['name'] == "Forgotten Key":
            is_key_in_inventory = True
        if item['name'] == "Silver Key":
            is_key1_in_inventory = True
    if board[position[0]][position[1]] in ['G0', 'G1'] and is_key_in_inventory:
        return True, board[position[0]][position[1]]
    if board[position[0]][position[1]] in ['G2', 'G3'] and is_key1_in_inventory:
        return True, board[position[0]][position[1]]
    elif board[position[0]][position[1]] not in ['#', '!', '&', '*', '?', 'G0', 'G1', 'G2', 'G3']:
        return True, board[position[0]][position[1]]
    else:
        return False, board[position[0]][position[1]]


def check_correct_movement_enemies(board, position):
    if board[position[0]][position[1]] not in ['#', '!', '&', '*', '?', 'K', 'G0', 'G1', 'G2', 'G3', 'E', 'F', '@', 'K1', 'K2', ]:
        return True, board[position[0]][position[1]]
    else:
        return False, board[position[0]][position[1]]


def board_0_wall_layout(board):
    height = len(board)
    for i in range(height-3):
        board[i][5] = '#'
    for i in range(height-3):
        board[-i][8] = '#'
    for i in range(6):
        board[4][8+i] = '#'
    for i in range(6):
        board[4+i][8+6] = '#'


def put_strong_sword(board1):
    board1[1][1] = 'M'


def npc_message(map_level, inventory):
    forgotten_key = False
    strong_sword = False
    for item in inventory:
        if item['name'] == 'Forgotten Key':
            forgotten_key = True
    for item in inventory:
        if item['name'] == 'Magic Long Sword':
            strong_sword = True

    if map_level == 0 and not forgotten_key:
        print('''+--------------------------------------------------------------------------+
|                                                                          |
|             YOU                                OLD MAGE                  |
|             ___                                   /\                     |
|            |===|                             _  _/__\_                   |
|            |___|                            / \  |__|                    |
|      ___  /#####\                           \ / / \/  \  ___             |
|     |   |//#####\\\                           ║ //|   |\\\|   |            |
|     |(₡)|/ ##### \\\                          ║// |   |  |(₡)|            |
|     |   |  ^^^^^  &[═══════                  ║   |   |  |   |            |
|      \_/   |#|#|                             ║   | | |   \_/             |
|            |_|_|                             ║   |_|_|                   |
|            [ | ]                             ║   [ | ]                   |
+--------------------------------------------------------------------------+
| Old mage says: Maybe you should look for a key to open the gate?         |
+--------------------------------------------------------------------------+''')
    if map_level == 0 and forgotten_key:
        print('''+--------------------------------------------------------------------------+
|                                                                          |
|             YOU                                OLD MAGE                  |
|             ___                                   /\                     |
|            |===|                             _  _/__\_                   |
|            |___|                            / \  |__|                    |
|      ___  /#####\                           \ / / \/  \  ___             |
|     |   |//#####\\\                           ║ //|   |\\\|   |            |
|     |(₡)|/ ##### \\\                          ║// |   |  |(₡)|            |
|     |   |  ^^^^^  &[═══════                  ║   |   |  |   |            |
|      \_/   |#|#|                             ║   | | |   \_/             |
|            |_|_|                             ║   |_|_|                   |
|            [ | ]                             ║   [ | ]                   |
+--------------------------------------------------------------------------+
| Old mage says: Oh. You found the key. Use it to open gate?               |
+--------------------------------------------------------------------------+''')
    if map_level == 1 and not strong_sword:
        print('''+--------------------------------------------------------------------------+
|                                                                          |
|             YOU                                OLD MAGE                  |
|             ___                                   /\                     |
|            |===|                             _  _/__\_                   |
|            |___|                            / \  |__|                    |
|      ___  /#####\                           \ / / \/  \  ___             |
|     |   |//#####\\\                           ║ //|   |\\\|   |            |
|     |(₡)|/ ##### \\\                          ║// |   |  |(₡)|            |
|     |   |  ^^^^^  &[═══════                  ║   |   |  |   |            |
|      \_/   |#|#|                             ║   | | |   \_/             |
|            |_|_|                             ║   |_|_|                   |
|            [ | ]                             ║   [ | ]                   |
+--------------------------------------------------------------------------+
| Old mage says: Somewhere here are hidden powerful...(press to continue)  |
+--------------------------------------------------------------------------+''')
        input()
        util.clear_screen()
        print('''+--------------------------------------------------------------------------+
|                                                                          |
|             YOU                                OLD MAGE                  |
|             ___                                   /\                     |
|            |===|                             _  _/__\_                   |
|            |___|                            / \  |__|                    |
|      ___  /#####\                           \ / / \/  \  ___             |
|     |   |//#####\\\                           ║ //|   |\\\|   |            |
|     |(₡)|/ ##### \\\                          ║// |   |  |(₡)|            |
|     |   |  ^^^^^  &[═══════                  ║   |   |  |   |            |
|      \_/   |#|#|                             ║   | | |   \_/             |
|            |_|_|                             ║   |_|_|                   |
|            [ | ]                             ║   [ | ]                   |
+--------------------------------------------------------------------------+
| Old mage says: ...sword it might be useful to defeat the dragon.         |
+--------------------------------------------------------------------------+''')
    if map_level == 1 and strong_sword:
        print('''+--------------------------------------------------------------------------+
|                                                                          |
|             YOU                                OLD MAGE                  |
|             ___                                   /\                     |
|            |===|                             _  _/__\_                   |
|            |___|                            / \  |__|                    |
|      ___  /#####\                           \ / / \/  \  ___             |
|     |   |//#####\\\                           ║ //|   |\\\|   |            |
|     |(₡)|/ ##### \\\                          ║// |   |  |(₡)|            |
|     |   |  ^^^^^  &[═══════                  ║   |   |  |   |            |
|      \_/   |#|#|                             ║   | | |   \_/             |
|            |_|_|                             ║   |_|_|                   |
|            [ | ]                             ║   [ | ]                   |
+--------------------------------------------------------------------------+
| Old mage says: With these sword dragon will be easliy defeated           |
+--------------------------------------------------------------------------+''')


def create_hole(board):
    for i in range(7, 12):
        for j in range(12, 17):
            board[i][j] = "o"
    board[7][12] = "."
    board[11][12] = "."
    board[7][16] = "."
    board[11][16] = "."
