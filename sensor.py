import random
import datetime


class Sensor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        sensor_data = random.randrange(0, 100, 1)
        sensor_date = datetime.datetime.now().strftime("%H:%M:%S")
        return "{name}: {date} {data}".format(name=self.name, date=sensor_date, data=sensor_data)


sensor = Sensor('tv')
print(sensor)
print(sensor)
