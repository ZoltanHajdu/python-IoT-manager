from device import sensor
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


    def analyze_sensor_data(self, raw_data):
        try:
            self.median = statistics.median([x[2] for x in raw_data])
            self.sum = sum([x[2] for x in raw_data])
            self.mean = statistics.mean([x[2] for x in raw_data])
            return [self.median, self.sum, self.mean]
        except ArithmeticError as e:
            print(f"Error occurred while analizing data: {e}")
            return []

