'''Написать итератор, аналогичный итератору из задания 1, но
обрабатывающий списки с любым уровнем вложенности'''


class FlatIterator:
    
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        print('START')
    
    def __iter__(self):
        self.iterator_ = [iter(self.list_of_list)]
        return self
    
    def __next__(self):
        while self.iterator_:
            try:
                item = next(self.iterator_[-1]) # ШАГ - переход к элементу вложенного списка, если это возможно
            except StopIteration:
                self.iterator_.pop()                 # нет элементов во вложенном списке -> удалаяем
                continue
            
            if isinstance(item, list):
                self.iterator_.append(iter(item))    # следующий элемент - список --> рекурсия
            else:
                print(f'{item=}')        # работаем внутри влож.списка: получаем item
                return item
            
        print(f'STOP')
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