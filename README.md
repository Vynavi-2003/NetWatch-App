# 📡 Connected Devices Dashboard
A web-based dashboard built with Flask that scans your local network to display connected devices, their IP address, MAC address, hostname, vendor, and timestamp. Includes real-time refresh and CSV export features.

## 🚀 Features
🌐 Scans your local network using arp -a

🖥 Displays IP, MAC, Hostname, Vendor & Timestamp

🔄 Live refresh via /refresh API

⬇️ Export connected devices as .csv

🌗 Light/Dark mode responsive styling

🧪 Vendor detection via MAC Vendors API

## 🛠 Tech Stack
Backend: Python, Flask

Frontend: HTML, Bootstrap 5, JavaScript

Styling: Custom CSS with dark mode support

APIs: macvendors.com

## 📂 Project Structure
```csharp
project/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # HTML template
└── static/
    └── style.css          
```
### ✅ Requirements
Python 3.8+

arp command must be available (works natively on Linux/macOS/Windows)

Internet access for MAC vendor API

Install dependencies:

```bash
pip install -r requirements.txt
```
## ▶️ How to Run
```bash
python app.py
```
Then open in your browser:

```cpp
http://127.0.0.1:5000/
```
## 📦 API Endpoints
/ – Home dashboard with scanned devices

/refresh – Returns fresh device scan as JSON (used by frontend to refresh the table)

## 📤 Export Feature
Click the ⬇️ Export CSV button to download the latest device list.





