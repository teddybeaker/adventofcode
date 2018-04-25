import re;

class RecursiveCircus:

    def __init__(self, filename):
        self._parse_input(filename)

    def _parse_input(self, filename):
        with open(filename) as f:
            regex = r'(\w+)\s\((\d+)\)(?:[^\w]+(.*))?'
            self._programs = []
            for line in f.read().split('\n'):
                if (len(line.strip())):
                    match = re.match(regex, line)
                    if match is None:
                        print("can not handle %s" % line)
                        break
                    children = []
                    if match.group(3) is not None:
                        children = [child.strip() for child in match.group(3).split(',')]
                    self._programs.append(Program(match.group(1), match.group(2), children))
        #print(self._programs)


    def find_root(self):
        root = self._programs[0]
        parent = self._find_parent(root)
        while (parent is not None):
            root = parent
            parent = self._find_parent(root)
        return root

    def _find_parent(self, program):
        for candidate in self._programs:
            if program.name in candidate.children:
                return candidate



class Program:
    def __init__(self, name, weight, children=[]):
        self.name = name
        self.weight = weight
        self.children = children

    def __str__(self):
        return ('{name} ({weight}) -> {children}').format(**self.__dict__)


if __name__ == '__main__':
    circus = RecursiveCircus('./input.txt')
    print("root name is %s" % circus.find_root().name)
