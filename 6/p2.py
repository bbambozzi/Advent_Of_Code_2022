for _ in range(1000):
    with open('input.txt') as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
            lines = line.strip()
        count = 0
        for i in range(len(line)):
            if len(set(line[i:i+14])) == len(line[i:i+14]):
                break






    
    
