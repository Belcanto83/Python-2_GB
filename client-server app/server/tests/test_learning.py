"""

class Sum(tuple):

    def __new__(cls, *args, **kwargs):
        return tuple.__new__(cls, args)


print(Sum(1, 2, 3))
print(type(Sum(1, 2, 3)))
print(type((1, 2, 3)))

"""

###########################################

import multiprocessing
import time


# Получает элементы из канала
def consumer(pipe):
    print('Потребитель запущен')
    output_p, input_p = pipe
    input_p.close()  # Закрыть конец канала, доступный для записи
    while True:
        try:
            item = output_p.recv()
            print('Потребитель: item collecting: ', item)
        except EOFError:
            break
        print('Потребитель: item processing: ', item**2)  # Обработать элемент. Замените print фактической обработкой
    # Завершение
    print("Потребитель завершил работу")


# Создает элементы и помещает их в канал
# sequence - итерируемый объект с элементами, которые требуется обработать
def producer(sequence, input_p):
    for item in sequence:
        print('Главный процесс (Производитель): item sending: ', item)
        input_p.send(item)  # Послать элемент в канал


if __name__ == '__main__':
    output_p, input_p = multiprocessing.Pipe()
    # Запустить процесс-потребитель
    cons_p = multiprocessing.Process(target=consumer, args=((output_p, input_p), ))
    cons_p.start()
    print('Запущен Потребитель (процесс "cons_p"). Главный процесс сейчас засыпает')

    time.sleep(5)
    print('Главный процесс просыпается')

    # Закрыть в поставщике конец канала, доступный для чтения
    output_p.close()
    # Отправить элементы
    sequence = [2, 3, 4, 5]
    producer(sequence, input_p)
    input_p.close()  # Сообщить об окончании, закрыв конец канала, доступный для записи
    cons_p.join()  # Дождаться, пока завершится процесс-потребитель
    print('Главный процесс завершил работу')
