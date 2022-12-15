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

    singles = []
    for first, second in pairs:
        singles.append(first)
        singles.append(second)

    less_2 = 1
    less_6 = 2

    for k in singles:
        if compare(k, [[2]]) < 0:
            less_2 += 1
            less_6 += 1
        else:
            if compare(k, [[6]]) < 0:
                less_6 += 1

    print(less_6 * less_2)
