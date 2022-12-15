from collections import deque, defaultdict
import math
operator_dict = {'*': lambda x, y: x * y, '+': lambda x, y: x + y}
examined_dict = defaultdict(int)


class Monke:
    def __init__(self, name: str, items: list, worry_operator, worry_number: str,  test_division: int, true_target: str, false_target: str):
        self.name = name
        self.items = deque(items)
        print(f"Constructed monke with {items}")
        self.worry_operator = worry_operator
        self.worry_number = worry_number
        self.test_division = test_division
        self.true_target = true_target.capitalize()
        self.false_target = false_target.capitalize()
        self.times_examined = 0
        self.magic_modulo = None
    
    def set_magic_module(self, x: int) -> None:
        self.magic_modulo = x

    def has_items(self) -> bool:
        return len(self.items) > 0

    def examine(self) -> list:
        if not self.items:
            return []
        answer = []
        while self.items:
            examined_dict[self.name] += 1
            item = self.items.popleft()
            worry_num = self.worry_number
            if self.worry_number == 'old':
                worry_num = int(item)
            worry_num = int(worry_num)
            operator_function = operator_dict[self.worry_operator]
            new_item = operator_function(item, worry_num)
            self.times_examined += 1
            new_item = new_item % self.magic_modulo
            if new_item % self.test_division == 0:
                answer.append(
                    [math.lcm(new_item, self.test_division), self.true_target])
                continue
            new_item = new_item % (self.test_division * new_item)
            answer.append([new_item, self.false_target])
        return answer

    def receive(self, x: int):
        self.items.append(x)
        return x

    @staticmethod
    def shout():
        print('UAAHH')


def monkey_factory(mdict: defaultdict) -> object:
    return Monke(mdict['name'], mdict['items'], mdict['worry_operator'], mdict['worry_number'],
                 mdict['test_division'], mdict["true_target"], mdict['false_target'])


with open('input.txt', 'r') as f:
    monkeys = []
    count = 0
    monkey = defaultdict(str)
    for line in f.readlines():
        sline = line.strip().split(' ')
        match count:
            case 0:
                monkey['name'] = sline[0] + str((sline[1][0]))
            case 1:
                monkey_items = []
                for num in range(2, len(sline)):
                    monkey_items.append(int(sline[num].removesuffix(',')))
                monkey['items'] = monkey_items
            case 2:
                # TODO: Handle edge case of old * old in the Monke class
                monkey['worry_operator'] = sline[-2]
                monkey['worry_number'] = (sline[-1])
            case 3:
                monkey['test_division'] = int(sline[-1])
            case 4:
                monkey_target = ''.join([sline[-2], sline[-1]]).capitalize()
                monkey['true_target'] = monkey_target
            case 5:
                monkey_target = ''.join([sline[-2], sline[-1]]).capitalize()
                monkey['false_target'] = monkey_target
            case 6:
                count = 0
                monkeys.append(monkey_factory(monkey))
                monkey = defaultdict(str)
                continue
            case default:
                raise ValueError("This should never evaluate.")
        count += 1


    magic_modulo = 1
    for monk in monkeys:
        magic_modulo *= monk.test_division
    for monk in monkeys:
        monk.set_magic_module(magic_modulo)

    for _ in range(10000):
        for monke in monkeys:
            if monke.has_items():
                items_to_throw = monke.examine()
                for item, target in items_to_throw:
                    monkeys[int(target[-1])].receive(item)


    print(examined_dict)
    examinations = []
    for key, value in examined_dict.items():
        examinations.append([key, value])
    examinations = sorted(examinations, key=lambda x: x[1])
    print(examinations[-1][1] * examinations[-2][1])
