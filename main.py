import subprocess
import time
import keyboard
import pyautogui
from pyautogui import *
from keyauth import api
import hashlib
import gratient
import pwinput
from easygui import *
import ctypes
from datetime import datetime
import pytesseract as tess
import os
from PIL import Image

sala = 0
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ctypes.windll.kernel32.SetConsoleTitleW("Automated Mediator by Keller")
os.system('mode 73,14')


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "Keller Mediator",
    ownerid = "hRj51EH3lN",
    secret = "79846ccc593acda2f747db1d2361b042c9ec346108173dadf9e044b58e517607",
    version = "1.0",
    hash_to_check = getchecksum()
)

PROCNAME = "cmd.exe"


def menu():
    print("""
                  [37;1mMenu[0m                 [0m[97m▄█████▄  
          [0m[97m ┌─────────────────┐       ▄█▌ ▄ ▄ ▐█▄
       [97m    │[ 1 ] [35mLogin.[0m[97m     │       ██▌▀▀▄▀▀▐██
       [97m    │[ 2 ] [35mSair.[0m[97m      │       ██▌ ▄▄▄ ▐██
          [0m[97m └─────────────────┘       ▀██▌▐█▌▐██▀
             made by keller       ▄██████ ▀ ██████▄\n\n
     """)


def login():
    try:
        print("""
                  [37;1mMenu[0m                 [0m[97m▄█████▄  
          [0m[97m ┌─────────────────┐       ▄█▌ ▄ ▄ ▐█▄
       [97m    │[ 1 ] [35mLogin.[0m[97m     │       ██▌▀▀▄▀▀▐██
       [97m    │[ 2 ] [35mSair.[0m[97m      │       ██▌ ▄▄▄ ▐██
          [0m[97m └─────────────────┘       ▀██▌▐█▌▐██▀
             made by keller       ▄██████ ▀ ██████▄\n\n\n\n\n
        """)
        ans = input("Selecione a opção: ")
        if ans == "1":
            os.system('cls')
            menu()
            user = input('Insira o usuário: ')
            password = pwinput.pwinput(prompt='Insira a senha: ', mask='*')
            keyauthapp.login(user, password)
            time.sleep(1)
            os.system('cls')
        elif ans == "2":
            os._exit(1)
        else:
            print("\nOpção inválida")
            time.sleep(1)
            os.system('cls')
            login()
    except KeyboardInterrupt:
        os._exit(1)


login()


def main():
    ctypes.windll.kernel32.SetConsoleTitleW("Automated Mediator by Keller | Salas criadas:")


keller = r"""
 ___  __    _______   ___       ___       _______   ________     
|\  \|\  \ |\  ___ \ |\  \     |\  \     |\  ___ \ |\   __  \    
\ \  \/  /|\ \   __/|\ \  \    \ \  \    \ \   __/|\ \  \|\  \   
 \ \   ___  \ \  \_|/_\ \  \    \ \  \    \ \  \_|/_\ \   _  _\  
  \ \  \\ \  \ \  \_|\ \ \  \____\ \  \____\ \  \_|\ \ \  \\   \| 
   \ \__\\ \__\ \_______\ \_______\ \_______\ \_______\ \__\\ _\ 
    \|__| \|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|

                       automated mediator
                       press f4 for exit                                                                                                
"""
keller_texto = gratient.black(keller)
print(keller_texto)
print("                \u001b[1mSeu login expira em:\u001b[0m " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%d/%m/%Y'))


# informacoes


def informacoes1():
    global textoinfo
    textoda = "Informações da aposta:"
    informacoes = ["SALA", "VALOR"]
    titulo = "Keller"
    textopronto = ["", "==pt"]
    output = multenterbox(textoda, titulo, informacoes, textopronto)
    message = str(output)
    textoinfo = '\n'.join(output)


def informacoes1_2():
    global textoinfo
    pyautogui.typewrite(textoinfo)

# informacoes

# criacao de sala

def criaremu1():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 878 475']) # criar sala
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 750 340'])  # clica telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input swipe 750 420 750 288'])  # desliza meio telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 750 447'])  # clica 1 telador
    time.sleep(0.25)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 372 115']) # clicar senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input text "09"']) # senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 440 136']) # loja competitivo
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 388 235']) # rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 388 300']) # 13 rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 756 235']) # ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 756 300']) # 1500 ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input swipe 530 273 530 182']) # deslizar tela ate drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 780 405']) # desligar drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554','shell', 'input tap 535 475']) # clicar confirmar


def criaremu1_2():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 570 375']) # confirma criacao
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 390 433']) # clica para telar
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 460 305']) # clica vaga telador
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 560 385']) # confirma vaga telador
    time.sleep(0.15)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'screencap /mnt/sdcard/id.png']) # salva print do id
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'pull', '/mnt/sdcard/id.png', "C:\\Users\mathe\OneDrive\Imagens\Keller"]) # salva print do id no pc
    os.system('cls')
    main()
    informacoes1()
    pyautogui.click(x=897, y=764)  # clica no discord
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '3')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    digitarid()
    pyautogui.typewrite('09')  # senha da sala
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '4')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('shiftright')  # marcar
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('shiftright')
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')  # fim da função marcar
    pyautogui.press('enter')
    pyautogui.hotkey('winleft', '5')  # mensagem para entrar na sala
    pyautogui.press('enter')
    pyautogui.typewrite('s1 ')  # sala do emulador
    informacoes1_2()
    pyautogui.press('enter')
    log()

def criaremu2():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 878 475']) # criar sala
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 750 340'])  # clica telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input swipe 750 420 750 288'])  # desliza meio telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 750 447'])  # clica 1 telador
    time.sleep(0.25)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 372 115']) # clicar senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input text "09"']) # senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 440 136']) # loja competitivo
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 388 235']) # rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 388 300']) # 13 rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 756 235']) # ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 756 300']) # 1500 ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input swipe 530 273 530 182']) # deslizar tela ate drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 780 405']) # desligar drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564','shell', 'input tap 535 475']) # clicar confirmar


def criaremu2_2():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 570 375']) # confirma criacao
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 390 433']) # clica para telar
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 460 305']) # clica vaga telador
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 560 385']) # confirma vaga telador
    time.sleep(0.15)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'screencap /mnt/sdcard/id.png']) # salva print do id
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'pull', '/mnt/sdcard/id.png', "C:\\Users\mathe\OneDrive\Imagens\Keller"]) # salva print do id no pc
    os.system('cls')
    main()
    informacoes1()
    pyautogui.click(x=897, y=764)  # clica no discord
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '3')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    digitarid()
    pyautogui.typewrite('09')  # senha da sala
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '4')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('shiftright')  # marcar
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('shiftright')
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')  # fim da função marcar
    pyautogui.press('enter')
    pyautogui.hotkey('winleft', '5')  # mensagem para entrar na sala
    pyautogui.press('enter')
    pyautogui.typewrite('s2 ')  # sala do emulador
    informacoes1_2()
    pyautogui.press('enter')
    log()

def criaremu3():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 878 475']) # criar sala
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 750 340'])  # clica telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input swipe 750 420 750 288'])  # desliza meio telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 750 447'])  # clica 1 telador
    time.sleep(0.25)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 372 115']) # clicar senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input text "09"']) # senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 440 136']) # loja competitivo
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 388 235']) # rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 388 300']) # 13 rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 756 235']) # ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 756 300']) # 1500 ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input swipe 530 273 530 182']) # deslizar tela ate drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 780 405']) # desligar drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574','shell', 'input tap 535 475']) # clicar confirmar


def criaremu3_2():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 570 375']) # confirma criacao
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 390 433']) # clica para telar
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 460 305']) # clica vaga telador
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 560 385']) # confirma vaga telador
    time.sleep(0.15)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'screencap /mnt/sdcard/id.png']) # salva print do id
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'pull', '/mnt/sdcard/id.png', "C:\\Users\mathe\OneDrive\Imagens\Keller"]) # salva print do id no pc
    os.system('cls')
    main()
    informacoes1()
    pyautogui.click(x=897, y=764)  # clica no discord
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '3')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    digitarid()
    pyautogui.typewrite('09')  # senha da sala
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '4')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('shiftright')  # marcar
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('shiftright')
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')  # fim da função marcar
    pyautogui.press('enter')
    pyautogui.hotkey('winleft', '5')  # mensagem para entrar na sala
    pyautogui.press('enter')
    pyautogui.typewrite('s3 ')  # sala do emulador
    informacoes1_2()
    pyautogui.press('enter')
    log()

def criaremu4():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 878 475']) # criar sala
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 750 340'])  # clica telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input swipe 750 420 750 288'])  # desliza meio telador
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 750 447'])  # clica 1 telador
    time.sleep(0.25)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 372 115']) # clicar senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input text "09"']) # senha
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 60 165']) # clicar na partida
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 440 136']) # loja competitivo
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 388 235']) # rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 388 300']) # 13 rodadas
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 756 235']) # ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 756 300']) # 1500 ouro
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input swipe 530 273 530 182']) # deslizar tela ate drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 780 405']) # desligar drop
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584','shell', 'input tap 535 475']) # clicar confirmar


def criaremu4_2():
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 570 375']) # confirma criacao
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 390 433']) # clica para telar
    time.sleep(1)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 460 305']) # clica vaga telador
    time.sleep(0.5)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 560 385']) # confirma vaga telador
    time.sleep(0.15)
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'screencap /mnt/sdcard/id.png']) # salva print do id
    subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'pull', '/mnt/sdcard/id.png', "C:\\Users\mathe\OneDrive\Imagens\Keller"]) # salva print do id no pc
    os.system('cls')
    main()
    informacoes1()
    pyautogui.click(x=897, y=764)  # clica no discord
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '3')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    digitarid()
    pyautogui.typewrite('09')  # senha da sala
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.hotkey('winleft', '4')  # barras divisórias
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('shiftright')  # marcar
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('shiftright')
    pyautogui.press('@')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')  # fim da função marcar
    pyautogui.press('enter')
    pyautogui.hotkey('winleft', '5')  # mensagem para entrar na sala
    pyautogui.press('enter')
    pyautogui.typewrite('s4 ')  # sala do emulador
    informacoes1_2()
    pyautogui.press('enter')
    log()

# fim criacao de sala

# id


def digitarid():
    printdoid = Image.open(r"C:\Users\mathe\OneDrive\Imagens\Keller\id.png")
    idcortado = printdoid.crop(box=(36, 65, 150, 90))  # largura esquerda id, altura cima, largura direita id, altura baixo
    idcortado.save(r"C:\Users\mathe\OneDrive\Imagens\Keller\idcortado.png")
    img = Image.open(r"C:\Users\mathe\OneDrive\Imagens\Keller\idcortado.png")  # pasta do cliente
    iddasala = tess.image_to_string(img, config='digits')
    time.sleep(0.5)
    pyautogui.typewrite(iddasala)  # id da sala
    pyautogui.press('enter')
    time.sleep(0.2)



# logs

sala = 0


def log():
    os.system('cls')
    print(keller_texto)
    global sala
    agora = datetime.now()
    horario = agora.strftime('%H:%M:%S')
    print(f"\u001b[1m[{horario}]\u001b[0m \u001b[33mSALA\u001b[0m CRIADA")
    sala += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"Automated Mediator by Keller | Salas criadas: {sala}")
    time.sleep(1)


def log_lobby():
    os.system('cls')
    print(keller_texto)
    agora = datetime.now()
    horario = agora.strftime('%H:%M:%S')
    print(f"\u001b[1m[{horario}]\u001b[0m Estou no lobby, criando \u001b[33msala\u001b[0m")


def log_jogando():
    os.system('cls')
    print(keller_texto)
    agora = datetime.now()
    horario = agora.strftime('%H:%M:%S')
    print(f"\u001b[1m[{horario}]\u001b[0m Sala está jogando, fechando \u001b[33msala\u001b[0m")

# logs end


def automatico():
    while True:
        if keyboard.is_pressed('f4'):  # fechar aplicativo
            os._exit(1)

        # lobby detect

        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\lobby1.png') is not None:  # lobby emu 1
            log_lobby()
            criaremu1()

        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\lobby2.png') is not None:  # lobby emu 2
            log_lobby()
            criaremu2()

        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\lobby3.png') is not None:  # lobby emu 3
            log_lobby()
            criaremu3()

        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\lobby4.png') is not None:  # lobby emu 4
            log_lobby()
            criaremu4()





        # lobby detect end

        # playing detect

        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\jogando1.png') is not None:  # jogando emu 1
            log_jogando()
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 933 19']) # clicar no x
            time.sleep(0.75)
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 840 340']) # clicar no ok
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 840 450']) # clicar battle royale
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5554', 'shell', 'input tap 485 480']) # clicar sala personalizada
            criaremu1()


        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\jogando2.png') is not None:  # jogando emu 2
            log_jogando()
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 933 19']) # clicar no x
            time.sleep(0.75)
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 840 340']) # clicar no ok
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 840 450']) # clicar battle royale
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5564', 'shell', 'input tap 485 480']) # clicar sala personalizada
            criaremu2()


        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\jogando3.png') is not None:  # jogando emu 3
            log_jogando()
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 933 19']) # clicar no x
            time.sleep(0.75)
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 840 340']) # clicar no ok
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 840 450']) # clicar battle royale
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5574', 'shell', 'input tap 485 480']) # clicar sala personalizada
            criaremu3()


        if pyautogui.locateOnScreen(r'C:\Users\mathe\OneDrive\Imagens\Keller\jogando4.png') is not None:  # jogando emu 4
            log_jogando()
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 933 19']) # clicar no x
            time.sleep(0.75)
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 840 340']) # clicar no ok
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 840 450']) # clicar battle royale
            subprocess.run([r"C:\Program Files (x86)\platform-tools\adb.exe", '-s', 'emulator-5584', 'shell', 'input tap 485 480']) # clicar sala personalizada
            criaremu4()



        if keyboard.is_pressed('f5'):
            criaremu1_2()

        if keyboard.is_pressed('f6'):
            criaremu2_2()

        if keyboard.is_pressed('f7'):
            criaremu3_2()

        if keyboard.is_pressed('f8'):
            criaremu4_2()



automatico()











































































































































































