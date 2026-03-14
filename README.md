# Network Automation Using REST API

A Python-based network automation tool that interacts with a simulated network controller using REST APIs to retrieve network device inventory, analyze device status, and generate automated operational reports.

This project demonstrates how modern network engineers automate infrastructure tasks using APIs instead of manual CLI configuration.

---

## Architecture
    Python Automation Script
    │
    │ REST API Requests
    ▼
    Mock Network Controller (Flask API)
    │
    ▼
    Simulated Network Devices
    │
    ▼
    Automated Report Generation

---

## Tech Stack

- Python
- REST APIs
- JSON
- Flask
- Requests Library
- Linux / WSL

---

## Project Structure
    network-api-automation/
    │
    ├── config.py
    ├── auth.py
    ├── api_client.py
    ├── device_inventory.py
    ├── validator.py
    ├── reports_generator.py
    ├── main.py
    │
    ├── mock_api_server.py
    └── reports/

---

## Features

- API authentication workflow
- Automated device inventory collection
- JSON response parsing
- Network device status validation
- Automated operational report generation

---

## Setup

Clone repository
```
git clone https://github.com/yourusername/network-api-automation.git
```
Move to Project directory
```
cd network-api-automation
```

Create virtual environment
```
python3 -m venv venv
```
Activate the environment
```
source venv/bin/activate
```

Install dependencies
```
pip install flask requsts
```

---

## Run the Mock API Server
```
python mock_api_server.py
```

Server runs on:
http://127.0.0.1:5000

---

## Run the Automation Script
```
python main.py
```

Workflow:

1. Authenticate to API  
2. Retrieve network device inventory  
3. Analyze device status  
4. Generate report

---

## Example Output
Hostname: router1
IP: 10.0.0.1
Status: active

Hostname: router2
IP: 10.0.0.3
Status: inactive

Generated file:
```
reports/device_report.txt
```

---

## Learning Outcomes

- REST API integration with Python
- Network automation workflows
- JSON data processing
- Automated infrastructure reporting

---

## Author

Kumar Gorav  
Network Automation | Cloud | DevOps
