"""
Реализовать приведение строк "разработка", "сокет", "декоратор" к типу bytes используя нативные методы строк;
Реализовать приведение полученных экземпляров типа bytes к типу str;
Реализовать приведение полученных строк и байтовых последовательностей с использование различных кодировок utf-8 latin-1
"""

import subprocess

# import chardet
#
# string = 'некая строка'
# bytes_string = string.encode('utf-8')
# print(bytes_string)
# print(chardet.detect(bytes_string))

print('Кодирование строк в байты:')
original_strings = ('develop', 'сокет', 'декоратор', 'decorator')
byte_strings = (string.encode('utf-8') for string in original_strings)
for i in range(len(original_strings)):
    print(original_strings[i], ':', byte_strings.__next__())

print()
print('Декодирование байтов в строки:')
byte_strings = (string.encode('utf-8') for string in original_strings)
decoded_strings = (string.decode('latin-1') for string in byte_strings)
for i in range(len(original_strings)):
    print(original_strings[i], ':', decoded_strings.__next__())

hostname = 'yandex.ru'
response = subprocess.Popen(f'ping {hostname}', stdout=subprocess.PIPE)
for line in response.stdout:
    print(line.decode('cp866'), end='')
