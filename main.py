from device import Device
from dashboard import Dashboard


def main():
    device1 = Device("LG television", "https://central-server.example.com")
    device2 = Device("Samsung television", "https://central-server.example.com")
    dashboard = Dashboard()

    def simulation(device):
        device.collect_data(10)
        processed_data = device.process_data()
        dashboard.display_raw_data(device.raw_data)
        dashboard.display_processed_data(processed_data)
        device.send_data_to_server(processed_data)

    simulation(device1)
    simulation(device2)


if __name__ == "__main__":
    main()
