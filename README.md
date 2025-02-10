# 🌍 IP Checker

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Description
**IP Checker** is a simple Python script that retrieves IP address details using [ip-api.com](http://ip-api.com/).  
It prints the results in color and saves a report to a file.

## 🚀 Features
✔️ Fetches **geolocation details** of an IP address  
✔️ Displays results in **colorized output** (via `colorama`)  
✔️ Saves the report to a **text file**  
✔️ Supports **custom file paths**  

## 🔧 Installation
1. **Clone the repository**  
    ```bash
    git clone https://github.com/gnatykdm/ipchecker.git
    cd ipchecker/checker/src
    ```
2. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage
```bash
python check.py <ip> <path>
```
🔹 Example: Save the report in the current directory
```bash
python check.py 62.40.98.72 raport.txt
```
🔹 Example: Save the report in a custom folder
```bash
python check.py 62.40.98.72 /home/user/reports
```

## 📜 Example Output
```yaml
[INFO] IP Information: 62.40.98.72

     Country: United Kingdom
     City: Cambridge
     ISP: GEANT European Backbone
     Latitude: 52.1917
     Longitude: 0.133608

[INFO] Report saved to reports/raport.txt
```

## 📄 License
This project is licensed under the [MIT License](LICENSE).
