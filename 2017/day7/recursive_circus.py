import re;


class RecursiveCircus:

    def __init__(self, filename):
        self._parse_input(filename)

    def _parse_input(self, filename):
        with open(filename) as f:
            regex = r'(\w+)\s\((\d+)\)(?:[^\w]+(.*))?'
            self._programs = {}
            for line in f.read().split('\n'):
                if len(line.strip()):
                    match = re.match(regex, line)
                    if match is None:
                        print("can not handle %s" % line)
                        break
                    name = match.group(1)
                    weight = int(match.group(2))
                    child_names = []
                    if match.group(3) is not None:
                        child_names = [child.strip() for child in match.group(3).split(',')]
                    self._programs[name] = Program(name, weight, child_names)

    def find_root(self):
        root = next(iter(self._programs.values()))
        parent = self._find_parent(root)
        while parent is not None:
            root = parent
            parent = self._find_parent(root)
        return root

    def _find_parent(self, program):
        for candidate in self._programs.values():
            if program.name in candidate.childNames:
                return candidate

    def _attach_children(self, root):
        if len(root.childNames) < 1:
            return
        for name in root.childNames:
            child = self._programs[name]
            root.add_child(child)
            self._attach_children(child)

    def find_unbalanced(self):
        root = self.find_root()
        self._attach_children(root)
        if root.is_balanced():
            print("tree is fully balanced")
            return
        node = root
        while not node.is_balanced() and not node.get_unbalanced_child().is_balanced():
            node = node.get_unbalanced_child()
        return node

    def find_new_weight(self):
        last_unbalanced = self.find_unbalanced()
        child_to_fix = last_unbalanced.get_unbalanced_child()
        target_weight = [c.cumulated_weight() for c in last_unbalanced.children if c is not child_to_fix][0]
        diff = target_weight - child_to_fix.cumulated_weight()
        return child_to_fix, child_to_fix.weight + diff


class Program:
    def __init__(self, name, weight, childNames=[]):
        self.name = name
        self.weight = weight
        self.childNames = childNames
        self.children = []
        self._cumulated_weight_cache = None

    def add_child(self, program):
        self.children.append(program)

    def cumulated_weight(self):
        if self._cumulated_weight_cache is None:
            sum = self.weight
            for child in self.children:
                sum += child.cumulated_weight()
            self._cumulated_weight_cache = sum
        return self._cumulated_weight_cache

    def is_balanced(self):
        child_weights = [child.cumulated_weight() for child in self.children]
        return min(child_weights) == max(child_weights)

    def get_unbalanced_child(self):
        child_weights = [child.cumulated_weight() for child in self.children]
        weight_counts = dict([(child_weights.count(w), w) for w in set(child_weights)])
        odd_weight = weight_counts[1]
        child_index = child_weights.index(odd_weight)
        return self.children[child_index]

    def __str__(self):
        return '{name} ({weight}) -> {childNames}'.format(**self.__dict__)


if __name__ == '__main__':
    circus = RecursiveCircus('./input.txt')
    print("root name is %s" % circus.find_root().name)
    (to_fix, new_weight) = circus.find_new_weight()
    print("new weight of %s should be %s" % (to_fix.name, new_weight))
