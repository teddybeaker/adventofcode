import unittest

from stream_processing import StreamProcessing

class TestStreamProcessing(unittest.TestCase):

    def test_single_group(self):
        processor = StreamProcessing('{}')
        processor.process()
        self.assertEqual(1, processor.group_count())
        self.assertEqual(1, processor.total_score())

    def test_three_groups(self):
        processor = StreamProcessing('{{{}}}')
        processor.process()
        self.assertEqual(3, processor.group_count())
        self.assertEqual(6, processor.total_score())

    def test_three_groups2(self):
        processor = StreamProcessing('{{},{}}')
        processor.process()
        self.assertEqual(3, processor.group_count())
        self.assertEqual(5, processor.total_score())

    def test_six_groups(self):
        processor = StreamProcessing('{{{},{},{{}}}}')
        processor.process()
        self.assertEqual(6, processor.group_count())
        self.assertEqual(16, processor.total_score())

    def test_one_group_with_garbage(self):
        processor = StreamProcessing('{<{},{},{{}}>}')
        processor.process()
        self.assertEqual(1, processor.group_count())
        self.assertEqual(1, processor.total_score())

    def test_one_group_with_garbage2(self):
        processor = StreamProcessing('{<a>,<a>,<a>,<a>}')
        processor.process()
        self.assertEqual(1, processor.group_count())
        self.assertEqual(1, processor.total_score())

    def test_five_groups_with_garbage(self):
        processor = StreamProcessing('{{<a>},{<a>},{<a>},{<a>}}')
        processor.process()
        self.assertEqual(5, processor.group_count())
        self.assertEqual(9, processor.total_score())

    def test_five_groups_with_garbage_cancel(self):
        processor = StreamProcessing('{{<!!>},{<!!>},{<!!>},{<!!>}}')
        processor.process()
        self.assertEqual(5, processor.group_count())
        self.assertEqual(4, processor.total_score())

    def test_two_groups_with_garbage(self):
        processor = StreamProcessing('{{<!>},{<!>},{<!>},{<a>}}')
        processor.process()
        self.assertEqual(2, processor.group_count())
        self.assertEqual(3, processor.total_score())

    def test_two_groups_with_garbage2(self):
        processor = StreamProcessing('{{<a!>},{<a!>},{<a!>},{<ab>}}')
        processor.process()
        self.assertEqual(2, processor.group_count())
        self.assertEqual(3, processor.total_score())

    def test_garbage(self):
        processor = StreamProcessing('<>')
        processor.process()
        self.assertEqual(0, processor.group_count())

    def test_garbage2(self):
        processor = StreamProcessing('<<<<>')
        processor.process()
        self.assertEqual(0, processor.group_count())

    def test_garbage_canceled_group(self):
        processor = StreamProcessing('<{!>}>')
        processor.process()
        self.assertEqual(0, processor.group_count())

    def test_garbage_canceled_cancel(self):
        processor = StreamProcessing('<!!>')
        processor.process()
        self.assertEqual(0, processor.group_count())

    def test_garbage_canceled_cancel2(self):
        processor = StreamProcessing('<!!!>>')
        processor.process()
        self.assertEqual(0, processor.group_count())

    def test_garbage3(self):
        processor = StreamProcessing('<{o"i!a,<{i<a>')
        processor.process()
        self.assertEqual(0, processor.group_count())


if __name__ == '__main__':
    unittest.main()