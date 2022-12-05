from collections import defaultdict
from string import ascii_lowercase, ascii_uppercase
with open('input.txt', 'r') as f:
    ## Map the letters to the value
    value_dict = defaultdict(int)
    for i , k in enumerate(ascii_lowercase):
        value_dict[k] = i + 1
    for i , k in enumerate(ascii_uppercase):
        value_dict[k] = i + 27
    
    total = 0
    for line in f.readlines():
        nline = line.strip()
        l , r  = set(nline[:len(nline)//2]) , set(nline[len(nline)//2:])
        for lnum in l:
            if lnum in r:
                total += value_dict[lnum]
                break 
    print(total)
