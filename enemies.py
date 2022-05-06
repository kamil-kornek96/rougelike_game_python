
import random
import engine
import util
from tabulate import tabulate


def enemies_creator(board, BOARD_WIDTH, BOARD_HEIGHT):
    baby_demon_start_position = starting_position_for_enemies(
        BOARD_HEIGHT, BOARD_WIDTH, board, "!")
    skeleton_start_position = starting_position_for_enemies(
        BOARD_HEIGHT, BOARD_WIDTH, board, "&")
    warrior_demon_start_position = starting_position_for_enemies(
        BOARD_HEIGHT, BOARD_WIDTH, board, "*")
    baby_demon = {"mark": "!", "name": "Baby Demon", "type": "Demon", "health": 20,
                  "strength": 20, "armor": 20, "luck": 0, "start_position": baby_demon_start_position}
    skeleton = {"mark": "&", "name": "Skeleton", "type": "Undead", "health": 30,
                "strength": 30, "armor": 30, "luck": 0, "start_position": skeleton_start_position}
    warrior_demon = {"mark": "*", "name": "Warrior Demon", "type": "Demon", "health": 40,
                     "strength": 40, "armor": 40, "luck": 0, "start_position": warrior_demon_start_position}

    return(baby_demon, skeleton, warrior_demon)


def boss_creator(board):
    dragon = {'name': 'Dragon', 'type': 'Creature', 'health': 100,
              "strength": 50, "armor": 300, "luck": 0, "start_position": [7, 12]}
    dragon_all_positions = []

    for i in range(7, 12):
        for j in range(12, 17):
            dragon_all_positions.append([i, j])
    for i, j in dragon_all_positions:
        if board[i][j] == '.':
            board[i][j] = 'D'

    return dragon_all_positions, dragon


def create_edge_positions(positions):
    edge_positions_1 = positions[:6]
    edge_positions_2 = positions[9:11]
    edge_positions_3 = positions[14:16]
    edge_positions_4 = positions[19:]

    edge_positions = edge_positions_1 + edge_positions_2 + \
        edge_positions_3 + edge_positions_4
    return edge_positions


def check_correct_movement_dragon(board, positions):
    for position in positions:
        if board[position[0]][position[1]] in ['#', '!', '&', '*', '?', 'K', 'G', 'E', 'F', '@']:
            return False
    return True


def dragon_movement(board, dragon_all_positions):
    keys = ["w", "s", "a", "d"]
    key = random.choice(keys)

    new_positions = []
    if key == 'w':
        for position in dragon_all_positions:
            new_position = [position[0] - 1, position[1]]
            new_positions.append(new_position)
    if key == 's':
        for position in dragon_all_positions:
            new_position = [position[0] + 1, position[1]]
            new_positions.append(new_position)
    if key == 'd':
        for position in dragon_all_positions:
            new_position = [position[0], position[1] + 1]
            new_positions.append(new_position)
    if key == 'a':
        for position in dragon_all_positions:
            new_position = [position[0], position[1] - 1]
            new_positions.append(new_position)
    edge_positions = create_edge_positions(new_positions)

    correct_movement = check_correct_movement_dragon(board, edge_positions)
    if correct_movement:
        for position in dragon_all_positions:
            board[position[0]][position[1]] = "."

        for position in new_positions:
            board[position[0]][position[1]] = 'D'

    else:
        new_positions = dragon_all_positions
    dragon_all_positions = new_positions
    util.clear_screen()
    print(tabulate(board))
    return dragon_all_positions


def make_move(key, enemy, board, previous_position):
    if key == 'w':
        enemy['start_position'][0] -= 1
    if key == 's':
        enemy['start_position'][0] += 1
    if key == 'd':
        enemy['start_position'][1] += 1
    if key == 'a':
        enemy['start_position'][1] -= 1
    correct_movement, interaction = engine.check_correct_movement_enemies(
        board, enemy['start_position'])
    if correct_movement:
        board[previous_position[0]][previous_position[1]] = "."
        board[enemy['start_position'][0]
              ][enemy['start_position'][1]] = enemy['mark']
    else:
        enemy['start_position'] = previous_position
    return correct_movement, interaction, previous_position


def enemies_movement(enemy, board, counter):

    keys = ["w", "s", "a", "d"]
    key = random.choice(keys)
    previous_position = enemy['start_position'].copy()
    if counter > 0:
        if board[enemy['start_position'][0]][enemy['start_position'][1]] == enemy['mark']:
            correct_movement, interaction, previous_position = make_move(
                key, enemy, board, previous_position)
            return correct_movement, interaction, previous_position
    if counter == 0:
        correct_movement, interaction, previous_position = make_move(
            key, enemy, board, previous_position)
        return correct_movement, interaction, previous_position


def starting_position_for_enemies(height, width, board, mark):
    while True:
        object_h = random.randint(1, height-1)
        object_w = random.randint(1, width-1)
        if board[object_h][object_w] == '.':
            board[object_h][object_w] = mark
            return [object_h, object_w]
