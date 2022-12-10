import heapq
from collections import defaultdict
heap = []
cycle = [0]
x = [1]
registers = defaultdict(int)
with open('shortexample.txt', 'r') as f:
    for line in f.readlines():
        cycle[0] += 1
        val = 0
        cur = line.strip().split(' ')
        while heap:
            if heap[0][0] == cycle[0]:
                _ , to_add = heapq.heappop(heap)
                x[0] += to_add 
                registers[cycle[0]] = x[0]
            else:
                registers[cycle[0]] = x[0]
                break

        if len(cur) > 1: 
            inst, val = cur
            val = int(val)

        inst = cur[0]
        match inst:
            case 'noop':
                heapq.heappush(heap, [cycle[0]+1 , 0])
            case 'addx':
                heapq.heappush(heap, [cycle[0]+2, int(val)])
                print(f"at cycle : {cycle[0]} : Added {val} pops at {cycle[0]+2}")
            case default:
                print("This should never evaluate")
                RuntimeError("Error: Invalid input")



    print(heap)
    cycle[0] += 1
    while heap:
        while heap:
            if heap[0][0] == cycle[0]:
                _ , to_add = heapq.heappop(heap)
                x[0] += to_add 
                registers[cycle[0]] = x[0]
            else:
                registers[cycle[0]] = x[0]
                break
        cycle[0] += 1
    signal_strength = 0
    signal_strength += registers[20] * 20
    """
    for cycle_number in range(20, 240, 40):
        cycle_value = registers[cycle_number]
        signal_strength += cycle_number * cycle_value
    """
    print(heap)
    print(registers)
