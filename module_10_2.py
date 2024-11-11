import threading
import time


class Knight(threading.Thread):

    def __init__(self, name=str, power=int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        enemies = 100
        while enemies > 0:
            enemies -= self.power
            time.sleep(1)
            days += 1
            print(f'{self.name} сражается {days}..., осталось {enemies} воинов.')
            if enemies < self.power:
                enemies = 0
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')