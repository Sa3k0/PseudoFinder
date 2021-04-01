import requests
import time
import os
import pylint 
from time import sleep
import warnings
from urllib3.exceptions import  InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

os.system('clear')

class bcolors:
    Redd         = "\033[31m"
    Greenn        = "\033[32m"
    White        = "\033[97m"

username = input('\033[92m[✓] Entrer le pseudonyme : ')


instagram = f'https://www.instagram.com/{username}'

facebook = f'https://www.facebook.com/{username}'

twitter = f'https://www.twitter.com/{username}'

youtube = f'https://www.youtube.com/{username}'

google_plus = f'https://plus.google.com/s/{username}/top'

reddit = f'https://www.reddit.com/user/{username}'

wordpress = f'https://{username}.wordpress.com'

pinterest = f'https://www.pinterest.com/{username}'

github = f'https://www.github.com/{username}'

steam = f'https://steamcommunity.com/id/{username}'

imgur = f'https://imgur.com/user/{username}'

spotify = f'https://open.spotify.com/user/{username}'

badoo = f'https://www.badoo.com/en/{username}'

dailymotion = f'https://www.dailymotion.com/{username}'

keybase = f'https://keybase.io/{username}'

pastebin = f'https://pastebin.com/u/{username}'

roblox = f'https://www.roblox.com/user.aspx?username={username}'

tripadvisor = f'https://tripadvisor.com/members/{username}'

wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

hackernews = f'https://news.ycombinator.com/user?id={username}'

ebay = f'https://www.ebay.com/usr/{username}'

WEBSITES = [
instagram, facebook, twitter, youtube, google_plus, reddit,
wordpress, pinterest, github, steam, imgur, spotify,
badoo, dailymotion, keybase, pastebin, roblox, 
tripadvisor, wikipedia, hackernews, ebay,
]

def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[31m')
PURPLE =    outer_func('\033[95m')
DarkGray = outer_func('\033[90m')

def banner():
    print(bcolors.Redd + 
"""

▓█████▄  ▒█████  ▒██   ██▒▓█████  ██▀███  
▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██░  ██▒░░  █   ░▒███   ▓██ ░▄█ ▒
░▓█▄   ▌▒██   ██░ ░ █ █ ▒ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░ ████▓▒░▒██▒ ▒██▒░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░ ░ ░ ░ ▒   ░    ░     ░     ░░   ░ 
   ░        ░ ░   ░    ░     ░  ░   ░     
 ░                                        
                                                                        
        \033[33m DOX3R outil de recherche avancée \033[33m  
        \033[33m Developpeur : \032 https://github.com/Sa3k0 
        """)

def search():
    RED(f'[✓] Lancement du scan sur : {username}')
    time.sleep(0.5)
    print('[✓] Analyse en cours veuillez patienter...')
    time.sleep(0.5)

    time.sleep(3)

    count = 0
    match = True 
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                GREEN('[✓] Résultat des informations !')
                match = False
            PURPLE(f'\n{url} - {r.status_code} - [✓]')
            if username in r.text:
                GREEN(f'[DOX3R] TROUVER : Username : {username} - Utilisateur trouver dans ce site web ')
            else:
                GREEN(f'[DOX3R] INTROUVABLE : Username :{username} - \033[91m Utilisateur introuvable')

    print(bcolors.Redd + f'Fin de la recherche pour {username}.')

if __name__=='__main__':
    banner()
    search()
