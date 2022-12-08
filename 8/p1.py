from math import inf
with open('input.txt', 'r') as f:
    grid = []
    for line in f.readlines():
        cur = []
        for character in line.strip():
            cur.append(int(character))
        grid.append(cur)
    total_rows, total_cols = len(grid), len(grid[0])
    ## Start from the edges, then mark all of the ones that we're allowed to see.
    ## Afterwards, count the amount of trees we can't see.
    visible = set()

    def mark_visible_horizontal(r, c,visited,prev=-inf) -> None:
        if (grid[r][c]) > prev:
            visible.add((r, c))
            prev = max(grid[r][c], prev)
        for row , col in [[r , c + 1] , [r , c - 1]]:
            if 0<=row<total_rows and 0<=col<total_cols and (row, col) not in visited:
                visited.add((row , col))
                mark_visible_horizontal(row, col,visited, prev)

    def mark_visible_vertical(r , c, visited, prev=-inf) -> None:
        if (grid[r][c]) > prev:
            visible.add((r, c))
            prev = max(grid[r][c], prev)
        for row , col in [[r + 1 , c] , [r - 1 , c]]:
            if 0<=row<total_rows and 0<=col<total_cols and (row, col) not in visited:
                visited.add((row, col))
                mark_visible_vertical(row, col, visited, prev)

    for r in range(total_rows):
        c = 0
        v = set()
        visible.add((r , c))
        mark_visible_horizontal(r , c, v)
        mark_visible_vertical(r , c, v)

    for r in range(total_rows):
        v = set()
        c = total_cols-1
        visible.add((r , c))
        mark_visible_horizontal(r , c, v)
        mark_visible_vertical(r , c, v)
    
    for c in range(total_cols):
        r = 0
        v = set()
        visible.add((r , c))
        mark_visible_horizontal(r , c, v)
        mark_visible_vertical(r , c, v)
    
    for c in range(total_cols):
        v = set()
        r = total_rows - 1
        visible.add((r , c))
        mark_visible_horizontal(r , c, v)
        mark_visible_vertical(r , c, v)
    
    total_trees = total_cols * total_rows
    print(len(visible))