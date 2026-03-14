def analyze_devices(device_data):
    results = []
    for device in device_data["devices"]:
        hostname = device["hostname"]
        ip = device["ip"]
        status = device["status"]
        
        results.append(
            {
                "hostname":hostname,
                "ip":ip,
                "status":status
            }
        )
    return results