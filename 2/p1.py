x = 3


def match_result(enemy, player) -> str:
    if (enemy == 'A' and player =='X') or (enemy == 'B' and player =='Y') or (enemy == 'C' and player == "Z"):
        return 'draw'
    if (enemy == 'B' and player == 'X'):
        return 'lose'
    if (enemy == 'A' and player == 'Z'):
        return 'lose'
    if (enemy == 'C' and player == 'Y'):
        return 'lose'
    return 'win'

def translate_score(result: str) -> int:
    match result:
        case 'draw':
            return 3
        case 'lose':
            return 0
        case 'win':
            return 6
        case default:
            UserWarning('Input error')

def return_score(arr: list) -> int:
    opponent , me = arr[0] , arr[1]
    score = 0
    match me:
        case 'X':
            score += 1
            score += translate_score(match_result(opponent, me))
            return score
        case 'Y':
            score += 2
            score += translate_score(match_result(opponent, me))
            return score
        case 'Z':
            score += 3
            score += translate_score(match_result(opponent, me))
            return score
        case default:
            UserWarning('Input error')
            return
    return score



with open('input.txt', 'r') as f:
    lines = []
    total_score = 0
    for line in f.readlines():
        lines.append(line.strip().split(' '))

    for line in lines:
        cur = return_score(line)
        print(f"line {line} score {cur}")
        total_score += cur
    print(total_score)

    

