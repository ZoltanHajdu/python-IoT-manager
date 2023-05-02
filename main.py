from device import Device
from dashboard import Dashboard

def main():
    device = Device("LG television", "https://central-server.example.com")
    dashboard = Dashboard()

    def simulation():
        device.collect_data(10)
        device.process_data()
        dashboard.display_data(device.data)

    simulation()

if __name__ == "__main__":
    main()