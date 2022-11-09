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

# creating_an_array_by_the_length_of_objects()

arr = [['hello', '2', 'world', ':-)'],
       ['1234', '1567', '-2', 'computer science'],
       ['Russia', 'Denmark', 'Kazan']]
for array in arr:
    creating_an_array_by_the_length_of_objects(array)

