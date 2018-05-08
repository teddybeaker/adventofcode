class StreamProcessing:

    GROUP_START = '{'
    GROUP_END = '}'
    GARBAGE_START = '<'
    GARBAGE_END = '>'

    def __init__(self, stream):
        self._stream = stream
        self._current_position = -1
        self._in_garbage = False
        self._group_count = 0
        self._total_score = 0
        self._next_score = 1

    def process(self):
        for self._current_position in range(0, len(self._stream)):
            if self._group_start():
                self._group_count += 1
                self._total_score += self._next_score
                self._next_score += 1
            elif self._group_end():
                self._next_score -= 1
            elif self._garbage_start():
                self._in_garbage = True
            elif self._garbage_end():
                self._in_garbage = False

    def _group_start(self):
        if self._in_garbage:
            return False
        return self._is_at(StreamProcessing.GROUP_START)

    def _group_end(self):
        if self._in_garbage:
            return False
        return self._is_at(StreamProcessing.GROUP_END)

    def _garbage_start(self):
        if self._in_garbage:
            return False
        return self._is_at(StreamProcessing.GARBAGE_START)

    def _garbage_end(self):
        if not self._in_garbage:
            return False
        return self._is_at(StreamProcessing.GARBAGE_END)

    def _is_at(self, character):
        if self._stream[self._current_position] != character:
            return False
        count_cancels = 0
        pos = self._current_position-1
        while self._stream[pos] == '!':
            count_cancels += 1
            pos -= 1
        return count_cancels % 2 == 0

    def group_count(self):
        return self._group_count

    def total_score(self):
        return self._total_score


if __name__ == '__main__':
    with open('./input.txt') as f:
        processor = StreamProcessing(f.read())
        processor.process()
        print("score of input is %s " % processor.total_score())
