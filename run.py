#!/usr/bin/env python3

''' версии программы
0.1 - исправления ошибок

0.2 - кореектное оформление сообщений

0.5 - добавил в каждое сообещние по времени, сменил слека оформление и отступы,
      добавил продолжение интервалов цикл за циклом а не сначала.

0.6 - переписал код в ООП стиле. ранее было на функциях:
    # intervals() - управление интервалами ( default: 4 )
    # verify_data() - проверка данных конфигурации и путей к звуковым файлам
    # the_work(id_interval) - рабочее время ( default: 25 min)
    # break_big() - большой перерыв через n интервалов ( default: 15 min )
    # break_min() - маленький перевы между интервалами ( default: 5 min )
'''

from bin.intervals import Intervals
intervals = Intervals()

print('* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ *')
print('* Метод "Помидорка" для контроля временем. *')
print('* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ *')

count_tomato = 0
while True:
    answer = input('\n1/0 -  начать/закрыть: ')
    if answer == '0':
        del intervals
        exit(0)
    elif answer == '1':
        intervals.count_id_clear()
        count_tomato = intervals.while_main(count_tomato)
    else:
        print("ошибка ввода\n")