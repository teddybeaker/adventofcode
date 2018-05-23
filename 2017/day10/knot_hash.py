
class KnotHash:

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

    def convert_to_ascii(string):
        return ord(string)

    def conver_to_hex(number):
        hex_val = hex(number)[2:4]
        if len(hex_val) <= 1:
            hex_val = '0' + hex_val
        return hex_val

    def bitwise_xor(array):
        result = 0
        for el in array:
            result ^= el
        return result


def part1(input):
    int_input = [int(x) for x in input.split(',')]
    kh = KnotHash(256)
    for length in int_input:
        kh.process(length)
    return kh.circular_list[0]*kh.circular_list[1]

def part2(input):
    ascii_input = [KnotHash.convert_to_ascii(x) for x in input]
    ascii_input += [17, 31, 73, 47, 23]
    kh = KnotHash(256)
    for i in range(0, 64):
        for length in ascii_input:
            kh.process(length)
    hash_list = []
    for i in range(0, 16):
        slice = kh.circular_list[i*16:(i+1)*16]
        hash_list.append(KnotHash.bitwise_xor(slice))
    hash = ''
    for x in hash_list:
        hash += KnotHash.conver_to_hex(x)
    return hash


if __name__ == '__main__':
    input = '165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153'
    total = part1(input)
    print("sum is %s when handled as integers" % total)

    hash = part2(input)
    print("hash is '%s' when handled as ascii" % hash)
