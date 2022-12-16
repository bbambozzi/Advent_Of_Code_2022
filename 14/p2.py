from collections import defaultdict
with open('input.txt', 'r') as f:
    rocks = defaultdict(bool)
    abyss = defaultdict(bool)

    def draw_abyss(max_y):
        y = max_y + 2
        for x in range(-5, 1000):
            rocks[(x, y)] = True

    def draw_line(x1: int, y1: int, x2: int, y2: int):
        delta_x, delta_y = (x2 - x1), (y2 - y1)
        if delta_x != 0:
            delta_x = 1 if delta_x > 0 else -1
        if delta_y != 0:
            delta_y = 1 if delta_y > 0 else -1
        rocks[(x1, y1)] = True
        rocks[(x2, y2)] = True

        x, y = x1, y1
        while (x, y) != (x2, y2):
            rocks[(x, y)] = True
            x += delta_x
            y += delta_y

    lines = []
    for line in f.readlines():
        splitted = ''.join(line.strip().split(' ')).split('->')
        lines.append(splitted)

    highest_y = 0
    for row in lines:
        for i in range(1, len(row)):
            x1, y1 = row[i - 1].split(',')
            x1, y1 = int(x1), int(y1)
            x2, y2 = row[i].split(',')
            x2, y2 = int(x2), int(y2)
            highest_y = max(highest_y, y1, y2)
            draw_line(x1, y1, x2, y2)

    solid_sand = [0]
    draw_abyss(highest_y)

    def falling_dfs(coords: list, is_first=False):
        x, y = coords
        if is_first:
            if (x, y + 1) in rocks and (x - 1, y + 1) in rocks and (x + 1, y + 1) in rocks:
                return False
        if (x, y + 1) in rocks and (x - 1, y + 1) in rocks and (x + 1, y + 1) in rocks:
            rocks[(x, y)] = True
            solid_sand[0] += 1
            return True
        if (x, y + 1) not in rocks:
            return falling_dfs((x, y + 1))
        elif (x - 1, y + 1) not in rocks:
            return falling_dfs((x - 1, y + 1))
        elif (x + 1, y + 1) not in rocks:
            return falling_dfs((x + 1, y + 1))
        print('Sneed!')

    count = 0
    while falling_dfs((500, 0), True):
        count += 1
    print(count + 1)
    print('Done.')
