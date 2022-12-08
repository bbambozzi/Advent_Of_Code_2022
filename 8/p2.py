with open('sample.txt', 'r') as f:
    grid = []
    for line in f.readlines():
        cur = []
        for character in line.strip():
            cur.append(int(character))
        grid.append(cur)
    total_rows, total_cols = len(grid), len(grid[0])

    def search(r , c , origin: int, direction: str, count=0) -> int:
        if (r < 0 or r >= total_rows or c < 0 or c >= total_cols):
            return count
        if grid[r][c] >= origin:
            return count + 1
        match direction:
            case 'up':
                if (r - 1) < 0:
                    return count + 1
                return search(r - 1 , c , origin, direction, count + 1)
            case 'down':
                if (r + 1) >= total_rows:
                    return count + 1
                return search(r + 1 , c , origin, direction, count + 1)
            case 'right':
                if (c + 1) >= total_cols:
                    return count + 1
                return search(r , c + 1 , origin, direction, count + 1)
            case 'left':
                if (c - 1) < 0:
                    return count + 1
                return search(r , c - 1 , origin, direction, count + 1)
            case default:
                LookupError("Incorrect direction provided.")
    max_seen = 0

    for r in range(total_rows):
        for c in range(total_cols):
            l = search(r , c - 1, grid[r][c], 'left')
            right = search(r , c + 1, grid[r][c], 'right')
            d = search(r + 1, c , grid[r][c], 'down')
            u = search(r - 1 , c, grid[r][c], 'up')
            ## if (l * r * d * u) > 0:
            max_seen = max(max_seen , (l * right * d * u))

    print(max_seen)

    
    