import heapq
from collections import defaultdict
heap = []
cycle = [1]
x = [1]
registers = defaultdict(int)
crt = [['.' for _ in range(40)] for _ in range(6)]

def draw(cycle: int, x: int) -> None:
    crt_row = cycle // 40
    start_row_cycle = ((cycle // 40) * 40) + 1
    crt_col = abs(cycle - start_row_cycle)
    if (abs(crt_col - x) < 2):
        print(f'cycle {cycle} r{crt_row}, c{crt_col}')
        crt[crt_row][crt_col] = '#'

with open('input.txt', 'r') as f:
    for line in f.readlines():
        cur = line.strip().split(' ')
        value = 0
        instruction = cur[0]
        if len(cur) > 1:
            value = int(cur[1])
        match instruction:
            case 'noop':
                heapq.heappush(heap, [cycle[0] + 1, 0])
            case 'addx':
                heapq.heappush(heap, [cycle[0] + 2, int(value)])
            case default:
                print("This should never evaluate")
        while heap:
            if heap[0][0] == cycle[0]:
                _, val = heapq.heappop(heap)
                x[0] += val
                registers[cycle[0]] = x[0]
                continue
            else:
                cycle[0] += 1
                registers[cycle[0]] = x[0]
    answer = 0
    for i in range(1, 241):
        val = registers[i]
        draw(i, val)
    for i in crt:
        print(i)





