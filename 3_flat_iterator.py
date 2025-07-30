class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = [list_of_list]

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.stack) > 0:
            current = self.stack.pop()
            if isinstance(current, list):
                self.stack.extend(reversed(current))
            else:
                return current

        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
