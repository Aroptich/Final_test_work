# Итоговая проверочная работа

## Условие задачи

* Написать программу, которая из имеющегося массива строк формирует массив из строк, длина которых меньше либо равна 
 3 символа.

* __В данной работе реализовано решение на языке программирования Python__

### Исходный код
    def creating_an_array_by_the_length_of_objects(array):
    '''Generates an array of strings that are less than or equal to 3 characters long.'''
    print(f'Первоначальный массив строк: {array}')
    array_with_objects_of_3_or_less_characters = []
    for i in array:
        if len(i) <= 3:
            array_with_objects_of_3_or_less_characters.append(i)
    print(f'Сформированный массив из строк, длина которых меньше либо равна 3 символов:'
          f' {array_with_objects_of_3_or_less_characters}')
    return array_with_objects_of_3_or_less_characters

### Блок-схема алгоритма

![Блок-схема][https://github.com/Aroptich/Final_test_work/blob/60cd181078ef381bd5671f41758e3f29f669c6be/%D0%91%D0%BB%D0%BE%D0%BA-%D1%81%D1%85%D0%B5%D0%BC%D0%B0.png]
