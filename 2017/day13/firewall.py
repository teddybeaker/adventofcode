class Firewall:

    def __init__(self, layers):

        self._layers = layers

    def calculate_severity(self):

        max_key = list(self._layers.keys())[-1]

        severity = 0

        # ignore level 0 since it doesn't contribute to severity (multiplication by 0)
        if 0 in self._layers:
            print('hit on layer 0')

        for depth in range(1, max_key+1):
            if depth in self._layers:
                position_in_range = depth % (2*self._layers[depth] - 2)
                if position_in_range == 0:
                    severity += depth * self._layers[depth]
                    print('hit on layer %s (%s)' % (depth, self._layers[depth]))
                # print('depth %s, range %s position_in_range %s' % (depth, self._layers[depth], position_in_range))

        return severity

if __name__ == '__main__':
    with open('./input.txt') as f:
        content = f.read().strip()
        layers = {}
        for line in content.split('\n'):
            # don't call this range! will owerwrite function range
            depth, rng = line.split(': ')
            layers[int(depth)] = int(rng)
        firewall = Firewall(layers)
        severity = firewall.calculate_severity()
        print('severity is %s' % severity)
