def sum_duplicates(digit_string, offset):
    length = len(digit_string)
    sum = 0
    for i, char in enumerate(digit_string):
      if char.isdigit():
        index = (i + offset) % length;
        if char == digit_string[index]:
          sum += int(char)

    return sum


def sibling_duplicates(digit_string):
    return sum_duplicates(digit_string, -1)


def halfway_around_duplicates(digit_string):
    offset = int(len(digit_string) / 2);
    return sum_duplicates(digit_string, offset);


def read_from_file(filename):
    print('opening file %s' % filename)
    file = open(filename)
    file_input = file.read()
    file.close()
    return file_input.strip()


if __name__ == "__main__":
    content = read_from_file('./input.txt')
    print('found numbers: %d' % len(content))

    result = sibling_duplicates(content)
    print('the sum of sibling duplicates is: %d' % result)

    result2 = halfway_around_duplicates(content)
    print('the sum of halfway-around duplicates is %d' % result2)
