from flask import Flask, render_template, jsonify
import subprocess
import re
import socket
from datetime import datetime
import requests

app = Flask(__name__)

def get_vendor(mac):
    try:
        # Use an external API for MAC vendor (optional)
        response = requests.get(f"https://api.macvendors.com/{mac}")
        return response.text if response.status_code == 200 else "Unknown"
    except:
        return "Unknown"

def scan_network():
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    devices = []
    for line in result.stdout.splitlines():
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17})", line)
        if match:
            ip = match.group(1)
            mac = match.group(2)
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown"
            vendor = get_vendor(mac)
            devices.append({
                "IP": ip,
                "MAC": mac,
                "Hostname": hostname,
                "Vendor": vendor,
                "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return devices

@app.route("/")
def index():
    devices = scan_network()
    return render_template("index.html", devices=devices)

@app.route("/refresh")
def refresh():
    return jsonify(scan_network())

if __name__ == "__main__":
    app.run(debug=True)
