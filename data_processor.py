import sensor
import time
import statistics


class DataProcessor:
    def __init__(self, sensor_name):
        self.median = 0
        self.mean = 0
        self.sum = 0
        self.sensor = sensor.Sensor(sensor_name)
        self.sensor_data = []

    def print_sensor_data(self):
        for s in self.sensor_data:
            print("")

    def print_analysis_result(self):
        print("Data analysis finished\n")
        print("median: {median}\nsum: {sum}\nmean: {mean}"
              .format(median=self.median, sum=self.sum, mean=self.mean))

    def collect_sensor_data(self, n):
        x = 0
        while x < n:
            self.sensor_data.append(self.sensor.get_sensor_data())
            x = x + 1

    def get_analyzed_sensor_data(self):
        self.median = statistics.median([x[2] for x in self.sensor_data])
        self.sum = sum([x[2] for x in self.sensor_data])
        self.mean = statistics.mean([x[2] for x in self.sensor_data])
        s = "Median: {median}, Sum: {sum}, Mean: {mean}".format(median=self.median, sum=self.sum, mean=self.mean)
        return s
