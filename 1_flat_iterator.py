
class FlatIterator:

    def __init__(self, list_of_list):
        self.flat_list = []
        self.flatten(list_of_list)
        self.index = 0

    def flatten(self, lst):
        for element in lst:
            if isinstance(element, list):
                self.flatten(element)
            else:
                self.flat_list.append(element)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.flat_list):
            raise StopIteration
        result = self.flat_list[self.index]
        self.index += 1
        return result



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
