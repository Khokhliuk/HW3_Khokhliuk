
import logging


import time
import random


battery_level = 100
trash_level = 0
water_level = 100
water_level_reducing = 10


class Robovac():
    def __init__(self, battery_level, trash_level, water_level):
        self.battery_level = battery_level
        self.trash_level = trash_level
        self.water_level = water_level

    def move(self):
        while self.battery_level != 0 and self.water_level != 0 and self.trash_level < 100:
            global water_level_reducing
            time.sleep(1)
            self.battery_level -= 10
            self.water_level = self.water_level - water_level_reducing
            self.trash_level = self.trash_level + random.randrange(1, 10)
            print(Robovac.wash(self), Robovac.vacuum_cleaning(self))
            logging.warning("Battery level is:", self.battery_level)
            logging.warning("Trash level is:", self.trash_level)
            logging.warning("Water level is:", self.water_level)

    def wash(self):
        logging.warning("Washing")

    def vacuum_cleaning(self):
        logging.warning("Vacuum cleaning")


if __name__ == "__main__":
    cleaner = Robovac(battery_level, trash_level, water_level)
    cleaner.move()
