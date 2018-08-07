import re

class DigitalPlumber:

    regex = r'(\d+)\s+<\->\s(.*)'

    def __init__(self, filename):
        self._filename = filename

    def parse(self):
        self._programs = {}
        with open(self._filename) as f:
            for line in f.read().strip().split('\n'):
                tuple = self._split_line(line)
                self._programs[tuple[0]] = tuple[1]

    def process(self):
        self._groups = {}
        for key in self._programs:
            if self._already_processed(key):
                continue
            else:
                self._groups[key] = set()
                self._add(key, self._groups[key])
        return self._groups

    def _already_processed(self, key):
        for groupmembers in self._groups.values():
            if key in groupmembers:
                return True
        return False

    def _add(self, program_id, group):
        group.add(program_id)
        connected = self._programs[program_id]
        for c in connected.split(','):
            c = c.strip()
            if not c in group:
                self._add(c, group)

    def _split_line(self, line):
        match = re.match(self.regex, line)
        return (match.group(1), match.group(2))


if __name__ == '__main__':
    dp = DigitalPlumber('input.txt')
    dp.parse()
    groups = dp.process()
    group0 = groups['0']
    print('there are %s programms in the group with 0' % len(group0))
    print('there are %s groups of programs' % len(groups))
