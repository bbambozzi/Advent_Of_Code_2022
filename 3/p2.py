from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
with open('input.txt', 'r') as f:
    value_dict = defaultdict(int)
    for i , k in enumerate(ascii_lowercase):
        value_dict[k] = i + 1
    for i , k in enumerate(ascii_uppercase):
        value_dict[k] = i + 27
    
    total = 0
    cur = []
    elves = []
    for line in f.readlines():
        cur.append(line.strip())
        if len(cur) == 3:
            elves.append(cur)
            cur = []
            continue
    for sacks in elves:
        seen = defaultdict(int)
        for knap in sacks:
            for char in set(knap):
                seen[char] += 1
        for key, value in seen.items():
            if value == 3:
                total += value_dict[key]
                print(f"Found {key} value {value_dict[key]}")
                break
    print(total)




