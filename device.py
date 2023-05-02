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
        self.raw_data = []

    def collect_data(self, num_samples):
        try:
            for _ in range(num_samples):
                self.raw_data.append(self.sensor.get_sensor_data())
        except Exception as e:
            print(f"Error occurred while collecting data: {e}")

    def process_data(self):
        try:
            return self.data_processor.analyze_sensor_data(self.raw_data)
        except Exception as e:
            print(f"Error occurred while processing data: {e}")

    def send_data_to_server(self, processed_data):
        try:
            self.communication.send_data(processed_data)
        except Exception as e:
            print(f"Error occurred while sending data to the server: {e}")

    def get_data_from_server(self):
        try:
            self.communication.get_data()
        except Exception as e:
            print(f"An error occurred while receiving data from the server: {e}")