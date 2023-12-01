# day 1 - part 1
with open('input.txt', 'r') as f:
    codes = list(map(str.rstrip, f))
    
# print(len(codes))
# print(codes[0])
# print([c for i,c in enumerate(codes[0]) if c.isdigit()])

def extract_digits(code):
    return [str(c) for i,c in enumerate(code) if c.isdigit()]

def cat_first_and_last_digits(digits):
    if 0 == len(digits):
        return '00'
    if 1 == len(digits):
        return digits[0]*2
    return digits[0] + digits[-1]

def get_two_digit_nums(codes):
    return [int(cat_first_and_last_digits(extract_digits(code))) for code in codes]

def sum_list_nums(nums):
    result = 0
    for num in nums:
        result += num
    return result

def process_code(code):
    # how to deal with overlapping numbers? e.g. twone
    # only the digits are required for counting, so can add more letters without changing answer
    text_num_map = {
        # 'zero':'0',
        'one':'one1one',
        'two':'two2two',
        'three':'three3three',
        'four':'four4four',
        'five':'five5five',
        'six':'six6six',
        'seven':'seven7seven',
        'eight':'eight8eight',
        'nine':'nine9nine'}
    # print(code)
    new_code = code
    for k,v in text_num_map.items():
        new_code = new_code.replace(k, v)
    # find first occurrence of named number
    # occurrences = { str(key):new_code.find(key) for key in text_num_map.keys() if new_code.find(key)>=0}
    # # print(occurrences)
    # # are any occurrences non-negative?
    # while occurrences:
    #     # find the first occurrence (lowest value in search results dict)
    #     first_occ = min(occurrences, key=occurrences.get)
    #     # print(first_occ, occurrences[first_occ])
    #     # print(new_code)
    #     # replace the first occurrence
    #     new_code = new_code.replace(first_occ, text_num_map[first_occ], 1)
    #     # re-create the occurrences search result on new string
    #     occurrences = { str(key):new_code.find(key) for key in text_num_map.keys() if new_code.find(key)>=0}
        # print(occurrences)
        # print(new_code)
    # print(new_code)
    return new_code
    

# for code in codes:
#     digits = extract_digits(code)
#     num = cat_first_and_last_digits(digits)
#     print(code, num)
answer1 = sum_list_nums(get_two_digit_nums(codes))
print('day 1 part 1:', answer1)
# process_code(codes[0])
print(get_two_digit_nums([process_code(n) for n in [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen'
    ]]))
answer2 = sum_list_nums(
    get_two_digit_nums([process_code(code) for code in codes])
)
print('day 1 part 2:', answer2)