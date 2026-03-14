import os

def generate_reports(devices):
    os.makedirs("reports", exist_ok=True)
    with open("reports/device_report.txt","w") as report:
        for device in devices:
            report.write(f"Hostname: {device['hostname']}\n")
            report.write(f"IP: {device['ip']}\n")
            report.write(f"Status: {device['status']}\n")
            report.write("\n")