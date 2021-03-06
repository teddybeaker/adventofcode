import csv


def checksum_row_minmax(row):
    min_val = min(row)
    max_val = max(row)
    return max_val - min_val


def checksum_row_evenly_divisible(row):
    for i in range(0, len(row)):
        for j in range(0, len(row)):
            if i != j:
                if row[i] % row[j] == 0:
                    return row[i]/row[j]
    raise Exception('no match found')


def checksum_matrix(matrix, checksum_row):
    total = 0
    for row in matrix:
        total += checksum_row(row)
    return total


if __name__ == '__main__':
    matrx = []
    with open('input.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='\t')
        for line in filereader:
            sanitized_row = []
            for val in line:
                sanitized_row.append(int(val))
            matrx.append(sanitized_row)
    checksum1 = checksum_matrix(matrx, checksum_row_minmax)
    checksum2 = checksum_matrix(matrx, checksum_row_evenly_divisible)
    print('read file from input.csv')
    print('checksum with min-max is %d' % checksum1)
    print('checksum2 with even devision is %d' % checksum2)
