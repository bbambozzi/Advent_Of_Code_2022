with open('input.txt') as f:
    lines = []
    for line in f.readlines():
        lines = line.strip()
    count = 0
    for i in range(len(line)):
        if len(set(line[i:i+4])) == len(line[i:i+4]):
            break