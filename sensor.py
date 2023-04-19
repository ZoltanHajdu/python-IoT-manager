import random
import datetime


class Sensor:

    lower_bound = 0
    upper_bound = 100
    steps = 1
    round = 5

    def __init__(self, name):
        self.name = name

    def __str__(self):
        sensor_date = datetime.datetime.now().strftime("%H:%M:%S")
        sensor_data1 = random.randrange(self.lower_bound, self.upper_bound, self.steps)
        sensor_data2 = round(random.SystemRandom().uniform(self.lower_bound, self.upper_bound), self.round)
        return "{name}: {date} {data1} {data2}".\
            format(name=self.name, date=sensor_date, data1=sensor_data1, data2=sensor_data2)


sensor = Sensor('tv')
print(sensor)
print(sensor)
