from flask import Flask, jsonify, request

app = Flask(__name__)
# simulated device database
devices = [
    {
        "hostname": "router1",
        "ip": "10.0.0.1",
        "model": "ISR4331",
        "status": "active"
    },
    {
        "hostname": "switch1",
        "ip": "10.0.0.2",
        "model": "Catalyst9300",
        "status": "active"
    },
    {
        "hostname": "router2",
        "ip": "10.0.0.3",
        "model": "ISR4321",
        "status": "inactive"
    }
]

@app.route("/login",methods=['POST'])
def login():
    data = request.json
    if data['username']=='admin' and data['password']=='password':
        return jsonify({'token':'mock-api-token'})
    return jsonify({'error':'Invalid Credentials'}) , 401

@app.route("/devices",methods=['GET'])
def get_devices():
    auth_header = request.headers.get("Authorization")
    if auth_header != "Bearer mock-api-token":
        return jsonify({'error':'Unauthorized'}), 401

    return jsonify({'devices':devices})

if __name__ == "__main__":
    app.run(port=5000)
