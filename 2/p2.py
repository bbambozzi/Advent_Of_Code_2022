def match_result(enemy, need) -> str:
    result = 0
    match need:
        case 'X':
            if (enemy == 'A'):
                return 3
            if (enemy == 'B'):
                return 1
            return 2
        case 'Y':
            if (enemy == 'A'):
                return 3+1
            if (enemy == 'B'):
                return 3+2
            return 3+3
        case 'Z':
            if (enemy == 'A'):
                return 6+2
            if (enemy == 'B'):
                return 6+3
            return 6+1
        case default:
            UserWarning('Input Error')
    return result

def return_score(arr: list) -> int:
    opponent , me = arr[0] , arr[1]
    score = 0
    return match_result(opponent, me) 


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

    

