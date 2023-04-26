import sensor
import time
import statistics


class DataProcessor:
    median = 0
    sum = 0
    mean = 0

    def __init__(self, sensor_name):
        self.sensor = sensor.Sensor(sensor_name)
        self.sensor_data = []

    def print_sensor_data(self):
        for s in self.sensor_data:
            print(s)

    def print_analysis_result(self):
        print("Data analysis finished\n")
        print("median: {median}\nsum: {sum}\nmean: {mean}"
              .format(median=self.median, sum=self.sum, mean=self.mean))

    def collect_sensor_data(self):
        x = 0
        while x < 10:
            self.sensor.update_sensor_data()
            self.sensor_data.append(self.sensor.get_sensor_data())
            x = x + 1

    def analyze_sensor_data(self):
        self.median = statistics.median([x[2] for x in self.sensor_data])
        self.sum = sum([x[2] for x in self.sensor_data])
        self.mean = statistics.mean([x[2] for x in self.sensor_data])


processor = DataProcessor('tv')
processor.collect_sensor_data()
processor.analyze_sensor_data()
processor.print_analysis_result()
