# module json для работы конфигурации заданных параметров интервалов
# module time - таймер, sleep для интервалов и вывода времени
# module os - для проверки на сущ. файлов
# module sys - для абсолют. пути к файлу
# module playsound - для воспроизведения уведомлений

import os
import sys
import time
import json
from playsound import playsound

# аналог отдельных функций the_work, break_big, break_min
class Time_modes:

    def the_work(self, count, id_time, notice, all_tomato):
        # основной интервал работы
        print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print('интервал: ' + str(count + 1 + all_tomato) + " | время: " + time.strftime('%H:%M'))
        print('занятия: ' + str(int(id_time / 60)) + ' мин.')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        playsound(notice)
        time.sleep(id_time)
        count += 1
        return count


    def breaks (self, id_time, break_mode):
        # большой/маленький перерыв
        print(break_mode + str(int(id_time / 60)) + ' мин.')
        print('=====================================')
        time.sleep(id_time)
        return 0


# аналог функции verify_data
class Data_check:

    # проверка на наличие муз. файлов
    def check_music(self, notice_array):
        for ifile in notice_array:
            if os.path.isfile(notice_array[ifile]) == False:
                print( 'Звукового файла [' + ifile + '] нету\nКонец программы' )
                exit(1)
        return 0

    # проверка на наличие конфиг. файла / создание если нет.
    def check_config(self):
        if os.path.isfile("./config/config.json"):
            self.count_json = json.load(open("./config/config.json", 'r'))
        else:
            print('''\nФайл конфигурации ./config/config.json не обнаружен!
                Записываю конфигурацию по умолчанию\n''')
            json.dump(self.count_json, open('./config/config.json', 'w'))
        return 0


# аналог функции intervals
class Intervals(Time_modes,Data_check):
    def __init__(self):
        # счетчик интервалов
        self.count_id = 0

        # массив с параметрами интервалов (сохр. в файле config.json)
        self.count_json = {
            "intervals": 4,
            "work": 25,
            "break-min": 5,
            "break-big": 10
        }

        # массив с путями к муз. файлов для уведомлений
        self.notice_array = {
            'start': sys.path[0] + '/sound/start.mp3',
            'pause-min': sys.path[0] + '/sound/pause-min.mp3',
            'pause-big': sys.path[0] + '/sound/pause-big.mp3',
            'the-end': sys.path[0] + '/sound/the-end.mp3'
        }

    # цикл интервалов
    def while_main(self, count_tomato):
        # from Data_check
        self.check_music(self.notice_array)
        self.check_config()

        # суть интервалов.
        while self.count_id < self.count_json['intervals']:
            # заголовок интервала
            self.count_id = self.the_work(self.count_id, self.count_json['work'] * 60, self.notice_array['start'], count_tomato)
            if self.count_id == self.count_json['intervals']:
                self.while_message('pause-big', 'break-big', count_tomato, 'бол. перерыв ')
            else:
                self.while_message('pause-min','break-min',count_tomato, 'мал. перерыв ')

        playsound(self.notice_array['the-end'])
        return self.count_id + count_tomato


    # сообщение о цикле
    def while_message(self, notice_index,count_jcon_index, count_tomato,break_mode):
        playsound(self.notice_array[notice_index])
        print('\n=====================================')
        print("интервал: " + str(self.count_id + count_tomato) + " | время: " + time.strftime('%H:%M'))
        self.breaks(self.count_json[count_jcon_index] * 60,break_mode)

    # чистка
    def count_id_clear(self):
        self.count_id = 0