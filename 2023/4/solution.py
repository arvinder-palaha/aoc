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

# part 2
def get_card_number(card: str):
    card_number = int(card.split(':')[0].split()[1])
    return card_number

def count_card_winning_numbers(card: str):
    w, n = get_card_nums(card)
    return count_winning_numbers(w, n)

def score_the_cards(cards: List[str]):
    scores = dict()
    for card in cards:
        ic = get_card_number(card)
        score = count_card_winning_numbers(card)
        scores[ic] = score
    return scores

def update_num_cards_dict(num_cards:dict, ic: int, score:int):
    number_of_first_card = num_cards[ic]
    for i in range(score):
        index = ic+i+1
        num_cards[index] += number_of_first_card
    return num_cards

def process_score_card(scores: dict):
    num_cards = {ic:1 for ic in scores.keys()}
    for ic,score in scores.items():
        # print(ic, score)
        num_cards = update_num_cards_dict(num_cards, ic, score)
    return num_cards

def sum_num_processed_cards(num_cards: dict):
    sum = 0
    for k,v in num_cards.items():
        sum += v
    return sum

def get_total_num_cards_after_scoring(cards: List[str]):
    scores = score_the_cards(cards)
    num_cards = process_score_card(scores)
    return sum_num_processed_cards(num_cards)

if __name__ == '__main__':
    cards = read_input('input.txt')
    # cards = read_input('input_example.txt')
    # print('\n'.join([card for card in cards]))
    
    answer1 = points_of_card_pile(cards)
    print('day 4 part 1 answer:', answer1)
    
    # for card in cards:
    #     print(get_card_number(card))
    # card_scores = score_the_cards(cards)
    # num_cards = process_score_card(card_scores)
    # sum_processed_cards = sum_num_processed_cards(num_cards)
    # print(card_scores, num_cards, sum_processed_cards)
    answer2 = get_total_num_cards_after_scoring(cards)
    print('day 4 part 2 answre:', answer2)
    