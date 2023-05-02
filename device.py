import Communication
import data_processor
import sensor


class Device:

    def __init__(self, device_name, server_url):
        if not device_name:
            raise ValueError("Device name cannot be empty.\n")
        if not server_url:
            raise ValueError("Server url cannot be empty\n")

        self.sensor = sensor.Sensor(device_name)
        self.communication = Communication.Communication(server_url)
        self.data_processor = data_processor.DataProcessor(device_name)
        self.data = []

    def collect_data(self, num_samples):
        try:
            self.data_processor.collect_sensor_data(num_samples)
        except Exception as e:
            print(f"Error occurred while collecting data: {e}")

    def process_data(self):
        try:
            self.data.append(self.data_processor.get_analyzed_sensor_data())
        except Exception as e:
            print(f"Error occurred while processing data: {e}")

    def send_data_to_server(self):
        try:
            self.communication.send_data(self.data)
        except Exception as e:
            print(f"Error occurred while sending data to the server: {e}")

    def get_data_from_server(self):
        try:
            self.communication.get_data()
        except Exception as e:
            print(f"An error occurred while receiving data from the server: {e}")