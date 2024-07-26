class FlatIterator:
    def __init__(self, list_of_lists):
        self.main_list = list_of_lists

    def __iter__(self):
        self.internal_cursor = 0
        self.external_cursor = 0

    def __next__(self):

        if self.internal_cursor > len(self.main_list[self.external_cursor]):
            self.external_cursor += 1
            self.internal_cursor = 0

        self.internal_cursor += 1

        if self.external_cursor == len(self.main_list):
            raise StopIteration

        return self.main_list[self.external_cursor][self.internal_cursor]


def test_1():
    list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]