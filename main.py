from device import device
from dashboard import dashboard

def main():
    device1 = device.Device("LG television", "https://central-server.example.com")
    device2 = device.Device("Samsung television", "https://central-server.example.com")
    dashboard1 = dashboard.Dashboard()

    def simulation(dev):
        dev.collect_data(10)
        processed_data = dev.process_data()
        dashboard1.display_raw_data(dev.raw_data)
        dashboard1.display_processed_data(processed_data)
        dev.send_data_to_server(processed_data)

    simulation(device1)
    simulation(device2)


if __name__ == "__main__":
    main()
