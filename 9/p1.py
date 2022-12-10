with open('input.txt', 'r') as f:
    head = [0 , 0]
    tail = [0 , 0]
    coordinates = [[1, 0], [-1 , 0], [0 , 1], [0 , -1], [1, -1], [-1, 1], [1 , 1] , [-1, -1]]

    def get_coordy(ta: list, he: list):
        if ta[0] != he[0] and ta[1] == he[1]:
            return [[1, 0], [-1, 0]]
        if ta[1] != he[1] and ta[0] == he[0]:
            return [[0 , 1], [0 , -1]]
        return [[1, 1] , [-1, -1], [1, -1], [-1, 1]]

    
    def pulse(ta: list, he: list, dirs=None):
        if dirs is None:
            dirs = coordinates
        if (ta == he):
            return ta
        r , c  = ta
        for x, y in dirs:
            row = r + x
            col = c + y
            if [row, col] == he:
                return ta
        return []
        
    def move_head(increasex: int, increasey: int, times: int, tai: list, hea: list) -> None:
            for _ in range(times):
                hea = [hea[0]  + increasex , hea[1] + increasey]
                if (hea == tai):
                    continue
                if not (pulse(tai , hea)):
                    for x , y in get_coordy(tai ,hea):
                        ro , co = x+tai[0] , y+tai[1]
                        if pulse([ro , co], hea):
                            tai = [ro , co]
                            print(f"Tail AT {tai}")
                            visited.add((ro , co))
                            break
                else:
                    continue
            return tai

    def update_head(he: list, increasex: int, increasey: int,  times: int) -> list:
        h = he[:]
        for _ in range(times):
            h = [h[0] + increasex, h[1] + increasey]
        return h


    visited = set()
    visited.add(tuple([0 , 0]))
    for line in f.readlines():
        direction, value = line.strip().split()
        value = int(value)
        match direction:
            case 'U':
                tail = move_head(0, 1, value, tail, head)
                head = update_head(head, 0 , 1, value)
            case 'D':
                tail = move_head(0, -1, value, tail, head)
                head = update_head(head, 0 , -1, value)
            case 'R':
                tail = move_head(1, 0, value, tail, head)
                head = update_head(head, 1 , 0, value)
            case 'L':
                tail = move_head(-1, 0, value, tail, head)
                head = update_head(head, -1 , 0, value)
            case default:
                print('This should never evaluate')
    print(len(visited))