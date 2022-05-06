import util
import engine
import ui
import player_menu
import enemies
import tabulate
import fight


PLAYER_ICON = '@'
PLAYER_START_X = 2
PLAYER_START_Y = 2

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

number_of_food = 3
number_of_equipment = 4
number_of_key = 1
number_of_enemy1 = 1
number_of_enemy2 = 1
number_of_enemy3 = 1
number_of_NPC = 1


def create_objects(board1, key_mark):
    engine.object_placement(board1, number_of_food,
                            BOARD_WIDTH, BOARD_HEIGHT, "F")[0]
    engine.object_placement(board1, number_of_equipment,
                            BOARD_WIDTH, BOARD_HEIGHT, "E")[0]
    engine.object_placement(board1, number_of_key,
                            BOARD_WIDTH, BOARD_HEIGHT, key_mark)[0]
    engine.object_placement(board1, number_of_NPC,
                            BOARD_WIDTH, BOARD_HEIGHT, "?")[0]


def create_board0(player):
    board0 = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)  # tworzy poziom 1
    engine.board_0_wall_layout(board0)
    # ustawia gracza na mapie
    engine.put_player_on_board(board0, player, PLAYER_ICON)
    engine.making_gate(board0, 1)  # tworzy bramy na mapie
    create_objects(board0, 'K')
    baby_demon, skeleton, warrior_demon = enemies.enemies_creator(
        board0, BOARD_WIDTH, BOARD_HEIGHT)
    counter = 0
    return board0, baby_demon, skeleton, warrior_demon, counter


def create_board1(player):
    board1 = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)  # tworzy poziom 2
    engine.board_0_wall_layout(board1)
    engine.making_gate(board1, 2)  # tworzy bramy na mapie
    create_objects(board1, 'K1')
    baby_demon1, skeleton1, warrior_demon1 = enemies.enemies_creator(
        board1, BOARD_WIDTH, BOARD_HEIGHT)
    engine.put_strong_sword(board1)
    counter = 0
    return board1, baby_demon1, skeleton1, warrior_demon1, counter


def create_board2(player):  # mapa z bosem
    board2 = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)  # tworzy poziom 2
    engine.create_hole(board2)
    engine.making_gate(board2, 3)  # tworzy bramy na mapie
    counter = 0
    return board2, counter


def boss_level(board, dragon_count, dragon_all_positions):
    dragon_all_positions1 = enemies.dragon_movement(
        board, dragon_all_positions)
    return dragon_all_positions1


def all_enemy_movement(baby_demon, skeleton, warrior_demon, current_board, counter):
    enemies.enemies_movement(baby_demon, current_board, counter)
    enemies.enemies_movement(skeleton, current_board, counter)
    enemies.enemies_movement(warrior_demon, current_board, counter)


def main():
    player_menu.welcome_screen()
    player = player_menu.player_statistics()
    board0, baby_demon, skeleton, warrior_demon, counter = create_board0(
        player)
    board1, baby_demon1, skeleton1, warrior_demon1, counter = create_board1(
        player)
    board2, counter = create_board2(player)
    dragon = {}
    util.clear_screen()
    is_running = True
    current_board = board0
    map_level = 0
    dragon_count = 0
    while is_running:
        ui.display_board(current_board)
        player_menu.player_statistics_display(player)
        key = util.key_pressed()
        if key == 'q':  # opcja wychodzenia z gry
            want_to_quit = input("Do you want to quit? (y/n) ").upper()
            if want_to_quit == "Y":
                fight.game_over()
                is_running = False
        if key == 'i':  # wyświetlanie inventory
            print(tabulate.tabulate(
                player['inventory'], headers='keys', tablefmt='fancy_grid', showindex=True))
            input('Press enter to exit inventory')
        if key == "c":  # cheat menu
            cheat = input("Enter cheatcode: ")
            if cheat == "DragonSlayer":
                player["health"] = 100
                player["strength"] = 1000
                player["luck"] = 1000
                player["armor"] = 1000
        else:
            correct_movement = False
            interaction_performed = False
            while not correct_movement:  # loop until correct move
                correct_movement, interaction, previous_position = engine.player_movement(
                    key, player, current_board)
                if interaction in ['!', '&', '*', 'D', ]:
                    # load previus position (incorrect move)
                    monster_position = player['start_position']
                    player['start_position'] = previous_position
                    util.clear_screen()
                    # choos actions depend on which field you interact
                    if map_level == 0:
                        player_won = engine.perform_action(
                            interaction, player, baby_demon, skeleton, warrior_demon, dragon, map_level)
                    if map_level in [1, 2]:
                        player_won = engine.perform_action(
                            interaction, player, baby_demon1, skeleton1, warrior_demon1, dragon, map_level)
                    if not player_won:
                        is_running = False
                    if player_won:
                        if interaction == 'D':
                            fight.game_finished()
                            is_running = False
                        current_board[monster_position[0]
                                      ][monster_position[1]] = '.'
                    interaction_performed = True
                    break
                if interaction == '?':
                    # npc interaction
                    engine.perform_action(
                        interaction, player, baby_demon, skeleton, warrior_demon, dragon, map_level)
                if not correct_movement:
                    # load previus position (incorrect move)
                    player['start_position'] = previous_position
                    key = util.key_pressed()
            if not interaction_performed:
                # delete player marker from previous position
                engine.put_player_on_board(
                    current_board, previous_position, '.')
                # update player marker on new position
                engine.put_player_on_board(current_board, player, PLAYER_ICON)
                if map_level == 2:
                    if dragon_count == 0:
                        dragon_all_positions, dragon = enemies.boss_creator(
                            current_board)
                        dragon_count += 1
                    dragon_all_positions = boss_level(current_board, dragon_count,
                                                      dragon_all_positions)
                # interactions with items
                if interaction in ['F', 'E', 'K', 'K1', 'K2', 'M']:
                    engine.perform_action(
                        interaction, player, baby_demon, skeleton, warrior_demon, dragon, map_level)
                # interactions with gates (load next levels)
                if interaction in ['G0', 'G1', 'G2', 'G3']:
                    if interaction == 'G0' and map_level == 0:
                        player['start_position'] = [-2, 15]
                        board1[-2][15] = '@'
                        board0[-1][15] = 'G0'
                        current_board = board1
                        map_level = 1
                    if interaction == 'G1' and map_level == 1:
                        player['start_position'] = [-2, 15]
                        board0[-2][15] = '@'
                        board1[-1][15] = 'G1'
                        current_board = board0
                        map_level = 0
                    if interaction == 'G2' and map_level == 1:
                        player['start_position'] = [1, 18]
                        board2[1][18] = '@'
                        board1[0][18] = 'G2'
                        current_board = board2
                        map_level = 2
                    if interaction == 'G3' and map_level == 2:
                        player['start_position'] = [1, 18]
                        board1[1][18] = '@'
                        board2[0][18] = 'G3'
                        current_board = board1
                        map_level = 1
                # enemies movement depends on current map/level
                if map_level == 0:
                    all_enemy_movement(baby_demon, skeleton,
                                       warrior_demon, current_board, counter)
                if map_level == 1:
                    all_enemy_movement(baby_demon1, skeleton1,
                                       warrior_demon1, current_board, counter)

        util.clear_screen()
        counter += 1


if __name__ == '__main__':
    main()
