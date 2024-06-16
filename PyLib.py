import time, os, sys, threading, requests, subprocess
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from colorama import init, Fore, Back, Style


blue = Fore.BLUE
yellow = Fore.YELLOW
green = Fore.GREEN
purple = Fore.MAGENTA
white = Fore.WHITE
red = Fore.RED

auth_key = "AutoClickerByCRXTICO&7ASRL2shegHP4bK"
os.system("cls")


auth = input(f"{white}There was an error opening PyLib.py...\n\n")
if auth == auth_key:

    os.system("cls")
    time.sleep(1)
    print(f"{green}Authenticated Successfully! \n\n")

    print(f"""{white}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⣠⣶⣶⣶⣦⡀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠠⣄⡀⠀⠀⢀⡿⠀⣀⠀⢿⣿⣉⣿⣿⣿⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⠙⠛⣻⡟⠀⣾⣿⡆⠘⢿⣛⡛⠉⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢤⣾⢶⣤⣀⣀⣙⣛⣁⣀⣀⣡⣽⣷⡄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣆⡀⠈⠻⢯⣉⡏⠙⡏⠉⣿⢙⡧⠟⠁⣀⣾⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠛⠻⢿⣿⣿⡿⣿⣿⣿⣆⠈⠻⢿⣦⣄⣀⠉⠙⢛⢛⣛⠛⢉⣁⣠⣴⡟⠉⣤⣾⡿⣿⡟⠻⣿⠿⠛⠉⠉⢹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣤⣀⣀⣀⣁⣴⠾⣣⣿⣿⣿⣷⣦⣈⠛⢿⣿⡙⠛⠛⠏⣿⣿⣿⢟⣉⣤⣾⣿⣿⣷⣌⢻⣶⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣆⣿⣿⣷⣾⣿⣿⣿⣽⣶⣿⣿⠶⠤⣼⣯⣡⣶⣾⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡩⢿⣿⣿⣿⣿⣿⣿⠉⢿⣉⣛⡰⣶⣽⡇⠀⠀⢹⣇⣤⢺⣿⠿⣿⣠⡾⣿⣿⣿⣿⣿⣿⣟⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⠿⠿⠿⣿⣿⣿⣿⣿⡇⢸⠶⡇⠀⠀⢸⡧⢶⡾⣍⣿⣿⣿⣷⢬⣙⣟⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⡏⣿⣿⣿⣿⣿⡟⡶⣷⣀⣀⣸⡷⡆⣣⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠹⣿⣿⣿⣧⣀⣀⣿⣿⣿⣿⣄⣉⣭⣯⣝⣉⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⣿⠙⣾⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣶⡟⢠⣿⣿⣿⣿⣿⠇⣿⠟⣿⣿⣿⠀⠸⣿⣿⣿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢿⡇⢸⣿⣿⣿⣿⣿⢻⣿⡀⣿⣿⣿⡇⠸⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣾⣭⣭⣭⣭⣽⣿⣿⣿⣯⣭⣭⣧⣤⣭⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⠙⠻⣍⢉⣿⣿⣿⣿⣿⣿⣿⣟⠁⠉⠉⣩⠿⠛⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣽⣯⣽⣿⣿⣿⣿⣿⣿⣍⣉⣭⣿⣧⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")

    time.sleep(1)
    os.system("cls")
    start_key = input(f"{white}[-] Enter your bind key: ")
    time.sleep(1)
    os.system("cls")

print(f"""{purple}

_________                __  .__               _________ .__  .__        __                 
\_   ___ \_________  ___/  |_|__| ____  ____   \_   ___ \|  | |__| ____ |  | __ ___________ 
/    \  \|_  __ \  \/  |   __\  |/ ___\/  _ \  /    \  \/|  | |  |/ ___\|  |/ // __ \_  __ \
\     \___|  | \/>    < |  | |  \  \__(  <_> ) \     \___|  |_|  \  \___|    <\  ___/|  | \/
 \______  /__|  /__/\_ \|__| |__|\___  >____/   \______  /____/__|\___  >__|_ \\___  >__|   
        \/            \/             \/                \/             \/     \/    \/       

\n""")

print(f"{yellow}Developed by: {blue}https://e-z.bio/crxtico\n")
print(f"{white}[+] Press {start_key} to start clicking!")
print(f'{white}[-] Press "E" to exit.\n')

delay = 1000 / (float(input(f'{red}CPS: {white}')))

button = Button.left

class Clicker(threading.Thread):
    def __init__(self, delay, button):
        super(Clicker, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):
        while self.program_run:
            while self.running:
                print("Clicking...")
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
thread = Clicker(delay, button)
thread.start()


def on_press(key):
    if key == start_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()


with Listener(on_press=on_press) as listener:
    listener.join()


os.system("pause")


