import requests
from urllib.parse import urljoin
from colorama import Fore, Style, init

init(autoreset=True)
print("""
    ____  _______   ______  ____  ___________
   / __ )/ ____/ | / / __ )/ __ )/ ____/ ___/
  / __  / __/ /  |/ / __  / __  / __/  \__ \ 
 / /_/ / /___/ /|  / /_/ / /_/ / /___ ___/ / 
/_____/_____/_/ |_/_____/_____/_____//____/  
                                             
""")
print("""
    ___    __  ____  _____________ 
   /   |  / / / /  |/  / ____/ __ \
  / /| | / /_/ / /|_/ / __/ / / / /
 / ___ |/ __  / /  / / /___/ /_/ / 
/_/  |_/_/ /_/_/  /_/_____/_____/  
                                   
""")
print("""
__  _____   ___________   ________
\ \/ /   | / ____/  _/ | / / ____/
 \  / /| |/ /    / //  |/ / __/   
 / / ___ / /____/ // /|  / /___   
/_/_/  |_\____/___/_/ |_/_____/   
                                  
""")
print("""███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
""")
file_name = "common.txt"
base_url = input("Enter the link: \n")

try:
    with open(file_name, "r") as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print("There is a problem with the text file. please try again")
    exit()

for word in words:
    url = urljoin(base_url, word)
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}The link is True: {url}")
        else:
            print(f"{Fore.RED}The link is False: {url}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}There is a problem with the link : {url} - {e}")
