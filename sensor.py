import random
import datetime


class Sensor:

    sensor_data = random.randrange(0, 100, 1)
    sensor_date = datetime.datetime.now().strftime("%H:%M:%S")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{name}: {date} {data}".format(name=self.name, date=Sensor.sensor_date, data=Sensor.sensor_data)


sensor = Sensor('tv')
print(sensor)
