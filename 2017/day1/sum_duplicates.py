def sum_duplicates(digitString, offset):
    length = len(digitString)
    sum = 0
    for i, char in enumerate(digitString):
      if (char.isdigit()):
        index = (i + offset) % length;
        if char == digitString[index]:
          sum += int(char)

    return sum

def sibling_duplicates(digitString):
    return sum_duplicates(digitString, -1)

def halfway_around_duplicates(digitString):
    offset = int(len(digitString)/2);
    return sum_duplicates(digitString, offset);


def readFromFile(filename):
    print('opening file %s' % filename)
    file = open(filename)
    content = file.read()
    file.close()
    return content.strip()


if __name__ == "__main__":
    content = readFromFile('./input.txt')
    print('found numbers: %d' % len(content))

    result = sibling_duplicates(content)
    print('the sum of sibling duplicates is: %d' % result)

    result2 = halfway_around_duplicates(content)
    print('the sum of halfway-around duplicates is %d' % result2)
