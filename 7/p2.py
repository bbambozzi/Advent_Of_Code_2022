from math import inf
class TreeNode:
    def __init__(self,name: str, parent):
        self.name = name
        self.children = []
        self.files = set()
        self.parent = parent

    def add_child(self, child_name):
        self.children.append(TreeNode(child_name, self))

    def has_child(self, child_name) -> bool:
        if not self.children:
            return False
        for child in self.children:
            if child.name == child_name:
                return True
    def add_file(self, file: list):
        self.files.add(file)
    
    def size(self):
        if not self.files:
            return 0
        count = sum([x[0] for x in self.files])
        return count 
    
class Tree:
    def __init__(self, rootName):
        self.current = TreeNode(rootName, None)
    
    def become_parent(self):
        if self.current.parent is None:
            return
        self.current = self.current.parent

    def become_son(self, son_name): 
        for son in self.current.children:
            if son.name == son_name:
                self.current = son
                return
        self.current.add_child(son_name)
        for son in self.current.children:
            if son.name == son_name:
                self.current = son
                return

candidates = set()
def dfs(node: TreeNode, space_to_clear):
    if node is None:
        return
    local = node.size()
    sons = 0
    for son in node.children:
        sons += dfs(son, space_to_clear)
    if (sons + local) >= space_to_clear:
        candidates.add(sons+local)
    return local + sons

with open('input.txt', 'r') as f:
    f.readline()
    tree = Tree('/')
    for line in f.readlines():
        cur = line.strip().split()
        if cur[0] == '$':
            match cur[1]:
                case 'cd':
                    if cur[2] == '/':
                        while tree.current.parent != None:
                            tree.become_parent()
                        continue 
                    if cur[2] == '..':
                        tree.become_parent()
                        continue
                    tree.become_son(cur[2])
                case 'ls':
                    continue
                case default:
                    print('This should never evaluate.')
            continue
        if cur[0] == 'dir':
            if tree.current.has_child(cur[1]):
                continue
            tree.current.add_child(cur[1])
            continue
        tree.current.add_file((int(cur[0]), cur[1]))

    while tree.current.parent != None:
        tree.become_parent()
    used_space = dfs(tree.current, inf)
    max_space = 70000000
    unused_space = max_space-used_space
    needed_space = 30000000
    space_to_clear = abs(needed_space-unused_space)
    dfs(tree.current, space_to_clear)
    print(min(candidates))
    
            
