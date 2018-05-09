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
        self._garbage_chars_count = 0
        self._total_score = 0
        self._next_score = 1

    def process(self):
        self._filter_canceled()
        for self._current_position in range(0, len(self._stream)):
            if self._in_garbage:
                if self._garbage_end():
                    self._in_garbage = False
                else:
                    self._garbage_chars_count += 1
            elif self._group_start():
                self._group_count += 1
                self._total_score += self._next_score
                self._next_score += 1
            elif self._group_end():
                self._next_score -= 1
            elif self._garbage_start():
                self._in_garbage = True

    def _filter_canceled(self):
        clean = []
        i = 0
        while i < len(self._stream):
            if self._stream[i] == '!':
                i += 2
            else:
                clean.append(self._stream[i])
                i += 1
        self._stream = ''.join(clean)

    def _group_start(self):
        return self._is_at(StreamProcessing.GROUP_START)

    def _group_end(self):
        return self._is_at(StreamProcessing.GROUP_END)

    def _garbage_start(self):
        return self._is_at(StreamProcessing.GARBAGE_START)

    def _garbage_end(self):
        return self._is_at(StreamProcessing.GARBAGE_END)

    def _is_at(self, character):
        return self._stream[self._current_position] == character

    def group_count(self):
        return self._group_count

    def total_score(self):
        return self._total_score

    def garbage_chars_count(self):
        return self._garbage_chars_count


if __name__ == '__main__':
    with open('./input.txt') as f:
        processor = StreamProcessing(f.read())
        processor.process()
        print("score of input is %s " % processor.total_score())
        print("garbage contains %s non-canceled characters" % processor.garbage_chars_count())
