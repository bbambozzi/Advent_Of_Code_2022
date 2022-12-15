from string import ascii_lowercase
from collections import defaultdict
from math import inf
import heapq
# Djikstra's
graph = []
visited = set()
path = []
start = []
lowercase = ascii_lowercase[::-1]
values_dict = defaultdict(int)
for i, char in enumerate(lowercase):
    values_dict[char] = i
values_dict['S'] = values_dict['a']
values_dict['E'] = values_dict['z']
exit = ()
with open('input.txt', 'r') as f:
    for line in f.readlines():
        current = []
        for char in line.strip():
            current.append(values_dict[char])
            if char == 'S' or char == 'a':
                start = [len(graph), len(current) - 1]
                heapq.heappush(path, [0, start])
                visited.add((len(graph) , len(current) - 1))
            if char == 'E':
                exit = (len(graph), len(current) - 1)
        graph.append(current)
total_rows , total_cols = len(graph) , len(graph[0])
for r in graph:
    print(r)
while path:
    cost, coordinates = heapq.heappop(path)
    r , c = coordinates
    if (r ,c) == exit:
        print('Found E!')
        print(cost)
        break
    for row, col in [[r + 1 , c] , [r - 1 , c] , [r , c + 1] , [r ,  c - 1]]:
        if 0<=row<total_rows and 0<=col<total_cols and (row, col) not in visited and graph[row][col] >= (graph[r][c] - 1):
            heapq.heappush(path, [cost + 1 , [row, col]])
            visited.add((row , col))
