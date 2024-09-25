from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'r+', encoding = 'utf-8')
    value = file.read()
    counts = value.count('\n')
    strings_positions = {}
    for string in strings:
        counts += 1
        strings_positions[(counts, file.tell())] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

