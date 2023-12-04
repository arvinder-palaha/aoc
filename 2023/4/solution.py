#!/home/arvinder/.pyenv/shims/python
# day 4 part 1
from typing import List

def read_input(filename: str):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f))

def get_card_nums(card: str):
    winners, numbers = card.split(':')[1].split('|')
    return winners.split(), numbers.split()

def count_winning_numbers(w: List[int], n: List[int]):
    count = len(set(w) & set(n))
    # print(n, w, count)
    return count

def card_points(card:str):
    w,n = get_card_nums(card)
    n_winning_nums = count_winning_numbers(w, n)
    # print('number of winning numbers', n_winning_nums)
    return 2**(n_winning_nums-1) if n_winning_nums else 0

def points_of_card_pile(cards: List[str]):
    sum = 0
    for card in cards:
        points = card_points(card)
        # print('points', points)
        sum += points
    return sum

if __name__ == '__main__':
    cards = read_input('input.txt')
    # cards = read_input('input_example.txt')
    # print('\n'.join([card for card in cards]))
    answer1 = points_of_card_pile(cards)
    print('day 4 part 1 answer:', answer1)
    