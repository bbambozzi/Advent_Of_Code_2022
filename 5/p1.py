
crates = ["WTHPJCF", "HBJZFVRG", "RTPH","THPNSZ",'DCJHZFVN',"ZDWFGMP","PDJSWZVM", "SDN", "MFSSZD"]
crates = [x[::-1] for x in crates]

from collections import deque
with open('input.txt', 'r') as f:
    ## Generate the queues first.
    queues = [deque() for _ in range(9)]
    for i, box in enumerate(crates):
        for char in box:
            queues[i].append(char)
    for line in f.readlines():
       line_array = line.strip().split(' ')
       amount, from_queue , to_queue = int(line_array[1]), int(line_array[3])-1 , int(line_array[5])-1
       popped = []
       for _ in range(amount):
        popped_element = queues[from_queue].pop()
        popped.append(popped_element)
        while popped:
            queues[to_queue].append(popped.pop())
    ans = []
    for k in queues:
        ans.append(k.pop())
    print(''.join(ans))
        

