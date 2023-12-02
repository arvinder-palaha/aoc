# day 2 - part 1    

with open('input.txt', 'r') as f:
    games = list(map(str.rstrip, f))
    
def process_game(game: str):
    # print(game)
    game_id_str, rounds_str = game.split(':')
    game_id = int(game_id_str.lower().replace('game ',''))
    rounds = rounds_str.lower().split(';')
    most_seen_col = dict()
    for round in rounds:
        reveals = round.lstrip().split(', ')
        # print(reveals)
        for reveal in reveals:
            num_str, col = reveal.split()
            num = int(num_str)
            if most_seen_col.get(col,0) < num:
                most_seen_col[col] = num
    # print(most_seen_col)
    return game_id, most_seen_col

def was_game_possible(most_seen_col, bag_contains):
    # print(most_seen_col, bag_contains)
    for col, num in most_seen_col.items():
        if num > bag_contains.get(col,0):
            return False
    return True

def sum_ids_for_bag_containing(games, bag_contains):
    sum_ids = 0
    for game in games:
        id, min_cols = process_game(game)
        if was_game_possible(min_cols, bag_contains):
            sum_ids += id
    return sum_ids

# part 2
def power_min_required_cubes(game):
    id, min_cols = process_game(game)
    power = 1
    for col, num in min_cols.items():
        power *= num
    return power

def sum_power_min_req_cubes(games):
    sum_power = 0
    for game in games:
        sum_power += power_min_required_cubes(game)
    return sum_power

# for game in games:
#     print(game)
# id, cols = process_game(games[0])
# print(was_game_possible(cols, {'blue':12, 'green': 5, 'red':6, 'magenta':20}))

bag = {'red':12, 'green':13, 'blue': 14}
answer1 = sum_ids_for_bag_containing(games,bag)
print('day 2 part 1 answer:', answer1)

answer2 = sum_power_min_req_cubes(games)
print('day 2 part 2 answer:', answer2)