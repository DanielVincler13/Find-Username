import requests as req
import colorama
from colorama import Fore, Back, Style
import urllib3
import time

# Desabilitar a verificação de certificado SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print(Fore.GREEN,'''
███████╗██╗███╗░░██╗██████╗░░░░░░░██╗░░░██╗░██████╗███████╗██████╗░
██╔════╝██║████╗░██║██╔══██╗░░░░░░██║░░░██║██╔════╝██╔════╝██╔══██╗
█████╗░░██║██╔██╗██║██║░░██║█████╗██║░░░██║╚█████╗░█████╗░░██████╔╝
██╔══╝░░██║██║╚████║██║░░██║╚════╝██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗
██║░░░░░██║██║░╚███║██████╔╝░░░░░░╚██████╔╝██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░░░░░░░░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
''')

username = input("Coloque o usuario: ")

# Estou pedindo para abrir a wordlist e nomeando como urls
with open("wordlist.txt") as urls:
    sites = urls.readlines()
    for site in sites:
        site = site.strip()

        url_full = f"{site}{username}"

        response = req.get(url_full, verify=False)
        time.sleep(1.5)
        code = response.status_code

        if code >= 200 and code <= 299:
            print(Fore.GREEN,f"[ + ] USER FOUND => {url_full}")
        elif code >= 400 and code <= 499:
            print(Fore.RED,f"[ + ] USER NOT FOUND => {url_full}")
        else:
            pass
    