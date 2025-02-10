import sys
import os
import pyfiglet
from colorama import Fore, init
import requests

init(autoreset=True)

def make_request(ip: str):
    if not ip:
        raise ValueError(f"[{Fore.RED}ERROR{Fore.RESET}] IP can't be empty.")
    
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_data(data, ip):
    if not data:
        print(f"[{Fore.RED}ERROR{Fore.RESET}] Failed to retrieve IP information.")
        return
    
    print(f"\n[{Fore.GREEN}INFO{Fore.RESET}] IP Information: {ip}\n")
    for key, value in data.items():
        print(f"\t{Fore.GREEN}{key.capitalize()}{Fore.RESET}: {value}")

def make_raport(ip_data, path):
    if not ip_data:
        raise ValueError(f"[{Fore.RED}ERROR{Fore.RESET}] IP data can't be empty.")

    if path == 'raport.txt':
        filename = 'raport.txt'
    else:
        os.makedirs(path, exist_ok=True) 
        filename = os.path.join(path, 'raport.txt')

    with open(filename, 'a') as f:
        for key, value in ip_data.items():
            f.write(f"{key}: {value}\n") 

    print(f"\n[{Fore.GREEN}INFO{Fore.RESET}] Report saved to {filename}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"\n[{Fore.CYAN}INFO{Fore.RESET}] Incorrect usage: python check.py {Fore.GREEN}<ip> <path>{Fore.RESET}\n")
        sys.exit(1)

    ip = sys.argv[1]
    path = sys.argv[2]

    ascii_art = pyfiglet.figlet_format("IpChecker")
    print(f"\n\t" + Fore.WHITE + " " * 2 + ascii_art)
    print(f"\n[{Fore.GREEN}STARTING{Fore.RESET}] -- Start checking IP: {ip}\n")

    result = make_request(ip)
    print_data(result, ip)

    make_raport(result, path)
