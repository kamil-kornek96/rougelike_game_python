import random
import tabulate


def all_items(mark):
    simple_sword = {'name': 'Prismatic Sword',
                    'strength': 5, 'armor': 0, 'health': 0, 'luck': 2, 'type': 'weapon'}
    sword = {'name': 'Sacrafice Blood Sword',
             'strength': 15, 'armor': 0, 'health': 0, 'luck': 5, 'type': 'weapon'}
    simple_armor = {'name': 'Prismatic Armor',
                    'strength': 0, 'armor': 5, 'health': 5, 'luck': 4, 'type': 'body_armor'}
    armor = {'name': 'Sacrafice Blood Armor',
             'strength': 0, 'armor': 15, 'health': 10, 'luck': 7, 'type': 'body_armor'}
    simple_amulet = {'name': 'Prismatic Amulet',
                     'strength': 2, 'armor': 2, 'health': 0, 'luck': 5, 'type': 'necklace'}
    amulet = {'name': 'Sacrafice Blood Amulet',
              'strength': 5, 'armor': 5, 'health': 5, 'luck': 15, 'type': 'necklace'}
    simple_helmet = {'name': 'Prismatic Helmet',
                     'strength': 0, 'armor': 5, 'health': 5, 'luck': 3, 'type': 'helmet'}
    helmet = {'name': 'Sacrafice Blood Helmet',
              'strength': 0, 'armor': 10, 'health': 10, 'luck': 6, 'type': 'helmet'}
    simple_legs = {'name': 'Prismatic Legs',
                   'strength': 0, 'armor': 5, 'health': 5, 'luck': 5, 'type': 'legs'}
    legs = {'name': 'Sacrafice Blood Legs', 'strength': 0,
            'armor': 10, 'health': 10, 'luck': 9, 'type': 'legs'}
    simple_boots = {'name': 'Prismatic Boots',
                    'strength': 0, 'armor': 5, 'health': 5, 'luck': 2, 'type': 'boots'}
    boots = {'name': 'Sacrafice Blood Boots',
             'strength': 0, 'armor': 10, 'health': 10, 'luck': 5, 'type': 'boots'}
    ham = {'name': 'Deer Ham', 'strength': 0,
           'armor': 0, 'health': 25, 'luck': 0, 'type': 'cure'}
    small_potion = {'name': 'Small Potion', 'strength': 0,
                    'armor': 0, 'health': 40, 'luck': 0, 'type': 'cure'}
    potion = {'name': 'Potion', 'strength': 0,
              'armor': 0, 'health': 85, 'luck': 0, 'type': 'cure'}
    key = {'name': "Forgotten Key", 'strength': 0,
           'armor': 0, 'health': 0, 'luck': 0, 'type': 'quest'}
    key_1 = {'name': "Silver Key", 'strength': 0,
             'armor': 0, 'health': 0, 'luck': 0, 'type': 'quest'}
    key_2 = {'name': "Golden Key", 'strength': 0,
             'armor': 0, 'health': 0, 'luck': 0, 'type': 'quest'}

    equipment_items = (simple_sword, sword, simple_armor, armor, simple_amulet, amulet, simple_helmet,
                       helmet, simple_legs, legs, simple_boots, boots,)
    food_items = (ham, small_potion, potion,)
    if mark == "K":
        key_item = key
        return key_item
    elif mark == "K1":
        key_1_item = key_1
        return key_1_item
    elif mark == "K2":
        key_2_item = key_2
        return key_2_item
    elif mark == "E":
        random_equip = random.choice(equipment_items)
        return random_equip
    elif mark == "F":
        random_food = random.choice(food_items)
        return random_food


def update_stats(player, random_item, item):
    player["strength"] -= item["strength"]
    player["luck"] -= item["luck"]
    player["armor"] -= item["armor"]
    player["health"] -= item["health"]
    player["strength"] += random_item["strength"]
    player["luck"] += random_item["luck"]
    player["armor"] += random_item["armor"]
    player["health"] += random_item["health"]
    if player["health"] > 100:
        player["health"] = 100


def add_strong_sword(interaction, player):
    strong_sword = {'name': 'Magic Long Sword',
                    'strength': 60, 'armor': 30, 'health': 0, 'luck': 5, 'type': 'weapon'}
    player["inventory"].append(strong_sword)
    print('You picked up:\n')
    print(tabulate.tabulate([strong_sword],
          headers='keys', tablefmt='fancy_grid',))
    input('Press enter to continue')
    player["strength"] += strong_sword["strength"]
    player["luck"] += strong_sword["luck"]
    player["armor"] += strong_sword["armor"]
    player["health"] += strong_sword["health"]
    if player["health"] > 100:
        player["health"] = 100


def compare_items(random_item, item, player, attribute):
    if random_item[attribute] >= item[attribute]:
        update_stats(player, random_item, item)
        player["inventory"].remove(item)
        player["inventory"].append(random_item)
        items_added = True
        print('You picked up:\n')
        print(tabulate.tabulate([random_item],
                                headers='keys', tablefmt='fancy_grid',))
        print(
            'Because it was better than or the same(these will be removed from your inventory):')
        print(tabulate.tabulate([item],
                                headers='keys', tablefmt='fancy_grid',))
        input('Press enter to continue')
        return items_added


def add_items(mark, player):
    random_item = all_items(mark)
    items_added = False
    for item in player['inventory']:
        if random_item['type'] in ['boots', 'helmet', 'legs', 'weapon', 'necklace', 'body_armor']:
            if random_item['type'] == item['type']:
                items_added = compare_items(
                    random_item, item, player, 'strength')
                if items_added:
                    break
                items_added = compare_items(random_item, item, player, 'armor')
    if not items_added:
        player["inventory"].append(random_item)
        print('You picked up:\n')
        print(tabulate.tabulate([random_item],
              headers='keys', tablefmt='fancy_grid',))
        input('Press enter to continue')
    if random_item["type"] != "cure" and not items_added:
        player["strength"] += random_item["strength"]
        player["luck"] += random_item["luck"]
        player["armor"] += random_item["armor"]
        player["health"] += random_item["health"]
        if player["health"] > 100:
            player["health"] = 100
