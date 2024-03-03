''' Должен получиться итератор, который принимает список списков
    и возвращает их плоское представление  '''


class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
    
    def __iter__(self):
        print('START')
        self.count = 0
        self.i_count = -1
        
        return self
    
    def __next__(self):
        self.i_count += 1             # ШАГ (вариант шага №1): переход к элементу вложенного списка
        
        i_limit = len(self.list_of_list[self.count])
        if self.i_count >= i_limit:
            self.count += 1            # ШАГ (вариант шага №2): переход к следующему вложенному списку
            self.i_count = 0
            
        if self.count == len(self.list_of_list):   # выход из итератора
            print('STOP')
            raise StopIteration
        else:
            if self.i_count < i_limit:  # работаем внутри влож.списка из list_of_list: получаем item
                item = self.list_of_list[self.count][self.i_count]
                
                
        print(f'{item=}')
        return item


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