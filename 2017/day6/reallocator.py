class Reallocator:

    def __init__(self, memory):
        self._memory = memory
        self._nof_banks = len(memory)
        self._cache = []
        self._cycles = 0

    def run(self):
        while self._cycles < 10000:
            state = ''.join(str(x) for x in self._memory)
            if (state in self._cache):
                self._last_state = state
                return
            self._cache.append(state)
            index = self._memory.index(max(self._memory))
            blocks = self._memory[index]
            self._memory[index] = 0
            for i in range(1, blocks+1):
                self._memory[(index + i)%self._nof_banks] += 1

            self._cycles += 1

    def get_cycles(self):
        return self._cycles

    def get_loop_size(self):
        return len(self._cache) - self._cache.index(self._last_state)


if __name__ == '__main__':
    banks = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
    reallocator = Reallocator(banks[:])
    reallocator.run()
    print("reallocator stopped after %d cycles, loop is %d" % (reallocator.get_cycles(), reallocator.get_loop_size()))
