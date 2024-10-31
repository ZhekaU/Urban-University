def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    index = 1
    for i in strings:
        position = file.tell()
        file.write(i + '\n')
        strings_positions[(index, position)] = i
        index += 1
    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('file_name.txt', info)
for elem in result.items():
  print(elem)

