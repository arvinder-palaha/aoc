# day 3 - part 1

with open('input.txt', 'r') as f:
    engine_map = list(map(str.rstrip, f))
    
def is_symbol(c: str):
    if c.isdigit() or (c == '.'):
        return False
    return True

def symbol_pos_in_row(row: str):
    symbols = list()
    for i,c in enumerate(row):
        if is_symbol(c):
            symbols.append(i)
    return symbols

def check_row_around_position(position: int, engine_row: str):
    # print(engine_row[position-1:position+2])
    width = len(engine_row)
    l, c, r = False, False, False
    if position != 0:
        l = engine_row[position-1].isnumeric()
    c = engine_row[position].isnumeric()
    if position < (width-1):
        r = engine_row[position+1].isnumeric()
    return [l, c, r]

def find_number_from_position(position: int, engine_row: str):
    number_str = engine_row[position]
    # print(number_str, position, engine_row)
    assert number_str.isnumeric()
    # check right
    for c in engine_row[position+1:]:
        if not c.isnumeric():
            break
        number_str += c
    # check left
    for c in reversed(engine_row[:position]):
        if not c.isnumeric():
            break
        number_str = str(c) + number_str
    # print(number_str)
    return int(number_str)

def extract_numbers_from_check(l: bool, c: bool, r: bool, pos:int, row:str):
    # print(l, c, r, pos, row[pos-1:pos+2])
    sum = 0
    if not any([l, c, r]):
        return 0
    if all([l, c, r]) or c:
        return find_number_from_position(pos, row)
    if l:
        sum += find_number_from_position(pos-1, row)
    if r:
        sum += find_number_from_position(pos+1, row)
    return sum

def part_1(map):
    # scan row for symbols -> list of positions (position)
    sum = 0
    for ir, row in enumerate(map):
        positions = symbol_pos_in_row(row)
        # for each symbol, check for numbers around it (3x3 boolean)
        for position in positions:
            # print(position)
            # above:
            if ir != 0:
                ul, uc, ur = check_row_around_position(position, map[ir-1])
                # extract numbers from above, either side and below
                upper = extract_numbers_from_check(ul, uc, ur, position, map[ir-1])
                # sum the numbers
                sum += upper
            # around:
            ml, mc, mr = check_row_around_position(position, row)
            middle = extract_numbers_from_check(ml, mc, mr, position, row)
            sum += middle
            # above:
            if ir < len(map):
                ll, lc, lr = check_row_around_position(position, map[ir+1])
                lower = extract_numbers_from_check(ll, lc, lr, position, map[ir+1])
                sum += lower
    return sum

# def is_adj_to_symbol(ir, ic, map):
#     if ir>0:
#         if ic>0:
#             if is_symbol(map[ir-1][ic-1]):
#                 return True
#         if is_symbol(map[ir-1][ic]):
#             return True
#         if ic<len(map[0])-1:
#             if is_symbol(map[ir-1][ic+1]):
#                 return True
#     if ic>0:
#         if is_symbol(map[ir][ic-1]):
#             return True
#     if is_symbol(map[ir][ic]):
#         return True
#     if ic<len(map[0])-1:
#         if is_symbol(map[ir][ic+1]):
#             return True
#     if ir<len(map)-1:
#         if ic>0:
#             if is_symbol(map[ir+1][ic-1]):
#                 return True
#         if is_symbol(map[ir+1][ic]):
#             return True    
#         if ic<len(map[0])-1:
#             if is_symbol(map[ir+1][ic+1]):
#                 return True
#     return False

# def update_b_map(b_map, l, c, r, ir, position):
#     if position>0:
#         b_map[ir][position-1] = l
#     b_map[ir][position] = c
#     if position<len(b_map[ir])-1:
#         b_map[ir][position+1] = r
#     return b_map
                
# def part_1_a(map):
#     pass
#     # create boolean copy of 'map'
#     b_map = [[False] * len(map[0]) for n in range(len(map))]
#     # true if position is number and adjacent to symbol
#     for ir, row in enumerate(map):
#         # find symbols in row
#         symbol_positions = symbol_pos_in_row(row)
#         # for each symbol, check if adjacent to number
#         for position in symbol_positions:
#             # above
#             if ir>0:
#                 ul, uc, ur = check_row_around_position(position, map[ir-1])
#                 b_map = update_b_map(b_map, ul, uc, ur, ir-1, position)
#             # around
#             ml, mc, mr = check_row_around_position(position, row)
#             b_map = update_b_map(b_map, ml, mc, mr, ir, position)
#             # below
#             if ir<len(map)-1:
#                 ll, lc, lr = check_row_around_position(position, map[ir+1])
#                 b_map = update_b_map(b_map, ll, lc, lr, ir+1, position)
    # print(b_map)
    # 
        # for ic, c in enumerate(row):
        #     print(is_adj_to_symbol(ir,ic,map))
    # sum all numbers that have a true in their position range

# part 2
def find_possible_gear(row):
    result = []
    for i,c in enumerate(row):
        if c == '*':
            result.append(i)
    return result

def find_numbers_from_check(l, c, r, ic, row):
    # print(l,c,r,ic,row)
    nums = []
    if c or all([l,r,c]):
        nums.append(find_number_from_position(ic, row))
    else:
        if l:
            nums.append(find_number_from_position(ic-1, row))
        if r:
            nums.append(find_number_from_position(ic+1, row))
    # print(nums)
    return nums

def gear_ratio(map, ir, ic):
    nums = []
    # above
    if ir>0:
        ul, uc, ur = check_row_around_position(ic,map[ir-1])
        nums += find_numbers_from_check(ul, uc, ur, ic, map[ir-1])
    # middle
    ml, mc, mr = check_row_around_position(ic, map[ir])
    nums += find_numbers_from_check(ml, mc, mr, ic, map[ir])
    # below
    if ir<len(map)-1:
        ll, lc, lr = check_row_around_position(ic, map[ir+1])
        nums += find_numbers_from_check(ll, lc, lr, ic, map[ir+1])
    # print('gear_ratio found', nums)
    if len(nums) == 2:
        return nums[0]*nums[1]
    return 0

def part_2(map):
    sum = 0
    for ir, row in enumerate(map):
        possible_gears = find_possible_gear(row)
        # print(possible_gears, row)
        for possible_gear in possible_gears:
            ratio = gear_ratio(map, ir, possible_gear)
            sum += ratio
    return sum
    
        
# for row in engine_rows:
#     print(row)
# print(engine_map[6][1:3])
# for c in engine_map[1]:
#     if is_symbol(c):
#         print(c) 

# tests on complete input
# print(symbol_pos_in_row(engine_map[0])) # should be empty
# print(symbol_pos_in_row(engine_map[1])) # should have % at 41
# print(check_row_around_position(41, engine_map[0])) # should be T T F
# print(check_row_around_position(41, engine_map[1])) # should be F F F
# print(check_row_around_position(41, engine_map[2])) # should be F F F
# print(find_number_from_position(11, engine_map[1])) # should be 53
# print(find_number_from_position(12, engine_map[1])) # should be 53
# print(find_number_from_position(14, engine_map[1])) # should be 497
answer1 = part_1(engine_map)
print('day 3 part 1 answer: ', answer1)

# part_1_a(engine_map)
answer2 = part_2(engine_map)
print('day 3 part 2 answer:', answer2)