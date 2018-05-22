
class KnowHash:

    def __init__(self, size):
        self.size = size
        self.circular_list = [i for i in range(0, size)]
        self.current_position = 0
        self.skip_size = 0

    def process(self, length):
        if length > self.size:
            raise Exception("length can't be more than list size")
        new_list = [x for x in self.circular_list]
        for i in range(0, length):
            write_index = (self.current_position + i) % self.size
            read_index = ((self.current_position + length - 1) % self.size) - i
            new_list[write_index] = self.circular_list[read_index]
        self.circular_list = new_list
        self.current_position = (self.current_position + length + self.skip_size) % self.size
        self.skip_size += 1

if __name__ == '__main__':
    input = [int(x) for x in '165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153'.split(',')]
    kh = KnowHash(256)
    for length in input:
        kh.process(length)
    total = kh.circular_list[0]*kh.circular_list[1]
    print("sum is %s" % total)
