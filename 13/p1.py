def compare(a: list or int, b: list or int) -> int or list:
    # 0 continue
    # -1 correct
    # 1 false
    if type(a) is int:
        if type(b) is list:
            return compare([a], b)
        else:
            return a - b
    else:
        if type(b) is int:
            return compare(a, [b])
        # If both are lists:

    for x, y in zip(a, b):
        evaluated = compare(x, y)
        if evaluated != 0:
            return evaluated

    return len(a) - len(b)


with open('input.txt', 'r') as f:
    pairs = []
    pair = []
    for line in f.readlines():
        if len(pair) == 2:
            print(f"l{pair[0]} , r{pair[1]}")
            pairs.append(pair)
            pair = []
            continue
        pair.append(eval(line))

    answer = 0
    for i, k in enumerate(pairs):
        if compare(k[0], k[1]) < 0:
            answer += (i + 1)
    print(answer)
