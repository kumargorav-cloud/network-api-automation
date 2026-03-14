from auth import get_auth_token
from device_inventory import get_device_inventory
from validator import analyze_devices
from reports_generator import generate_reports

def main():
    token = get_auth_token()
    device_data = get_device_inventory(token)
    devices = analyze_devices(device_data)
    generate_reports(devices)


if __name__ == "__main__":
    main()
