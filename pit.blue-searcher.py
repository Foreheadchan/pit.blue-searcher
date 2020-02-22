import webbrowser
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
url = "https://pit.blue/profile?lookup="

while True:
    username = input("Give username to search on pit.blue(To exit, type /terminate)\n>> ")
    clear()
    if username != "/terminate":
        webbrowser.open_new(url+username)
    elif username == "/terminate":
        print("Program terminated!")
        quit()
