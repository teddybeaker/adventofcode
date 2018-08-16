class Firewall:

    def __init__(self, layers):
        self._layers = layers
        self._max_key = list(self._layers.keys())[-1]

    def calculate_severity(self):
        severity = 0
        for depth in range(0, self._max_key+1):
            if depth in self._layers:
                position_in_range = depth % (2*self._layers[depth] - 2)
                if position_in_range == 0:
                    severity += depth * self._layers[depth]
                    print('hit on layer %s (%s)' % (depth, self._layers[depth]))
                # print('depth %s, range %s position_in_range %s' % (depth, self._layers[depth], position_in_range))

        return severity

    def get_safe_path(self):
        offset = 0
        while True:
            if self._is_hit(offset):
                offset += 1
            else:
                return offset
            if offset > 20000000:  # manually incremented to prevent infinte loop
                return -1

    def _is_hit(self, offset):
        for depth in range(0, self._max_key+1):
            if depth in self._layers:
                position_in_range = (depth + offset) % (2*self._layers[depth] - 2)
                if position_in_range == 0:
                    # print('hit on layer %s with offset %s' % (depth, offset))
                    return True
        return False


def parse_layers(file_content):
    layers = {}
    for line in file_content.split('\n'):
        # don't call this range! will owerwrite function range
        dep, rng = line.split(': ')
        layers[int(dep)] = int(rng)
    return layers


if __name__ == '__main__':
    with open('./input.txt') as f:
        content = f.read().strip()
        firewall = Firewall(parse_layers(content))
        sev = firewall.calculate_severity()
        print('severity is %s' % sev)
        delay = firewall.get_safe_path()
        print('offset for safe passage is %s' % delay)
