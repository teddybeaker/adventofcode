import operator
import re


class FileParser:

    line_regex = r'(\w+)\s+(inc|dec)\s+([\-\d]+)\s+if\s+(.*)'
    condition_regex = r'(\w+)\s+(<|>|<=|>=|==|!=)\s+([\-\d]+)'

    def __init__(self, filename):
        self._filename = filename
        self._registers = {}
        self._max_register_value = 0

    def run(self):
        self._registers = {}
        self._max_register_value = 0
        with open(self._filename) as f:
            for line in f.read().split('\n'):
                self._execute_line(line)

    def _execute_line(self, line):
        if len(line.strip()) < 1:
            return
        match = re.match(self.line_regex, line)
        if match is None:
            raise Exception('can not handle line "%s"' % line)
        register = match.group(1)
        operation = match.group(2)
        amount = int(match.group(3))
        condition = match.group(4)
        if self._condition_applies(condition):
            self._set_register(register, operation, amount)
            pass
            # set register to value

    def _condition_applies(self, condition):
        match = re.match(self.condition_regex, condition)
        if match is None:
            raise Exception('can not handle condition "%s"' % condition)
        register = match.group(1)
        comparison = match.group(2)
        expected_value = int(match.group(3))
        # print('split condition %s into reg: %s, comp %s exp: %s' % (condition, register, comparison, expected_value))
        actual_value = self._get_or_init_register(register)
        if comparison == '<':
            return actual_value < expected_value
        elif comparison == '<=':
            return actual_value <= expected_value
        elif comparison == '>':
            return actual_value > expected_value
        elif comparison == '>=':
            return actual_value >= expected_value
        elif comparison == '==':
            return actual_value == expected_value
        elif comparison == '!=':
            return actual_value != expected_value
        else:
            raise Exception('can not handle comparison %s' % comparison)

    def _get_or_init_register(self, register):
        if register not in self._registers:
            self._registers[register] = 0
        return self._registers[register]

    def _set_register(self, register, operation, amount):
        if register not in self._registers:
            self._registers[register] = 0
        if operation == 'dec':
            amount *= -1
        self._registers[register] += amount
        self._max_register_value = max(self._max_register_value, self._registers[register])

    def get_max_register_end_value(self):
        if len(self._registers) < 1:
            return None
        return max(self._registers.items(), key=operator.itemgetter(1))[1]

    def get_max_register_value(self):
        return self._max_register_value


if __name__ == '__main__':
    parser = FileParser('./input.txt')
    parser.run()
    max_register_end_value = parser.get_max_register_end_value()
    print('max_register_value is %s' % max_register_end_value)
    max_register_value = parser.get_max_register_value()
    print('max_register_value is %s' % max_register_value)
