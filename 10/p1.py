import heapq
from collections import defaultdict
heap = []
cycle = [1]
x = [1]
registers = defaultdict(int)
with open('input.txt', 'r') as f:
    for line in f.readlines():
        cur = line.strip().split(' ')
        value = 0
        instruction = cur[0]
        if len(cur) > 1:
            value = int(cur[1])
        print(instruction, value)
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
    answer += registers[20] * 20
    for i in range(60, 221, 40):
        answer += registers[i] * i
    print(registers)
    print(answer)




