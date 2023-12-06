#!/home/arvinder/.pyenv/shims/python
# day 5 part 1

from typing import Dict, List


def read_input(filename: str):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f))
    
class Mapping:
    def __init__(self, i: str, o: str):
        self.coming_in: str = i
        self.going_out: str = o
        self.map: List[int] = []
        
    def update_map(self, destination:int, source: int, rng: int):
        self.map.append([destination, source, rng])
            
    def use_map(self, input:int):
        result = input
        for part in self.map:
            dest, src, rng = part
            if (result >= src) and (result < (src+rng)):
                diff = input - src
                result = dest + diff
                return result
        return input
    
class Almanac:
    def __init__(self, seeds: List[int] = []):
        self.seeds: List[int] = seeds
        self.maps: Dict[str, Mapping] = {}
        
    def seed_to_location(self, seed: int):
        result = seed
        map_string = 'seed'
        while map_string != 'location':
            # print(map_string, result)
            result = self.maps[map_string].use_map(result)
            map_string = self.maps[map_string].going_out
        return result
    
    def process_seeds(self):
        return [self.seed_to_location(seed) for seed in self.seeds]
            
    
def parse_almanac_seeds_line(al_seeds: str):
    return [int(s) for s in al_seeds.split()[1:]]

def parse_map_name(al_line: str):
    return al_line.split()[0].split('-')[0:3:2]

def parse_map_numbers(map_line: str):
    return [int(s) for s in map_line.split()]
        
def parse_almanac(al: List[str]):
    almanac = Almanac()
    input_name = ''
    output_name = ''
    for line in al:
        if "seeds: " in line:
            almanac.seeds = parse_almanac_seeds_line(line)
        elif len(line) == 0:
            pass
        elif "map:" in line:
            input_name, output_name = parse_map_name(line)
            # print(input_name, output_name)
            almanac.maps[input_name] = Mapping(input_name, output_name)
        else:
            dest, src, rng = parse_map_numbers(line)
            almanac.maps[input_name].update_map(source=src, destination=dest, rng=rng)
    return almanac

if __name__ == '__main__':
    # almanac_input = read_input('input_example.txt')
    almanac_input = read_input('input.txt')
    almanac = parse_almanac(almanac_input)
    # print(almanac.seeds, almanac.maps['seed'].map.keys())
    locations = almanac.process_seeds()
    # print(locations)
    answer1 = min(locations)
    print(locations)
    print('Day 5 part 1 answer:', answer1)
