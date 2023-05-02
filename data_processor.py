import sensor
import time
import statistics


class DataProcessor:
    def __init__(self, sensor_name):
        self.median = 0
        self.mean = 0
        self.sum = 0
        self.sensor = sensor.Sensor(sensor_name)


    def print_analysis_result(self):
        print("Data analysis finished\n")
        print("median: {median}\nsum: {sum}\nmean: {mean}"
              .format(median=self.median, sum=self.sum, mean=self.mean))

    def collect_sensor_data(self, n):
        x = 0
        while x < n:
            self.sensor_data.append(self.sensor.get_sensor_data())
            x = x + 1

    def analyze_sensor_data(self, raw_data):
        self.median = statistics.median([x[2] for x in raw_data])
        self.sum = sum([x[2] for x in raw_data])
        self.mean = statistics.mean([x[2] for x in raw_data])
        return [self.median, self.sum, self.mean]
