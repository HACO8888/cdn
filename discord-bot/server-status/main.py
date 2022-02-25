import discord
import psutil
import asyncio
import json
import os
import random
import datetime
import platform
from cpuinfo import get_cpu_info
import time
import ctypes

with open('setting.json', 'r', encoding="utf-8") as jfile:
    jdata = json.load(jfile)


class DCBOT(discord.Client):

    async def on_ready(self):
        print("Bot Is Ready")
        self.loop.create_task(self.status())

    async def status(self):
        try:
            while True:
                use = psutil.cpu_percent()
                ram = psutil.virtual_memory()
                mess = 'RAM使用量' + byte_to_largest(ram.used)
                await self.update('CPU使用量 ' + str(use) + '%')
                await asyncio.sleep(5)
                await self.update(mess)
                await asyncio.sleep(5)
        finally:
            self.loop.create_task(self.status())

    async def update(self, text):
        await self.change_presence(activity=discord.Game(name=text))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == '!狀態':
            msg = await message.channel.send("系統努力加載中........請稍等")

            use = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            mess = '使用量: ' + \
                byte_to_largest(ram.used)
            my_system = platform.uname()
            cpu_name = get_cpu_info()['brand_raw']
            cpu_speed = get_cpu_info()['hz_advertised_friendly']
            lib = ctypes.windll.kernel32
            t = lib.GetTickCount64()
            t = int(str(t)[:-3])
            mins, sec = divmod(t, 60)
            hour, mins = divmod(mins, 60)
            days, hour = divmod(hour, 24)

            embed = discord.Embed(
                title='**主機狀態**', colour=random.randint(0, 0xffffff), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="**主機開機時間**",
                            value=f"{days}天{hour:02}小時{mins:02}分{sec:02}秒\n**CPU**\n名稱: {cpu_name}\n核心數: {psutil.cpu_count()}\n速度: {cpu_speed}\n使用量: " + str(use) + "%\n**RAM**\n" + mess)
            await msg.delete()
            await message.channel.send(embed=embed)

        elif message.content == '！狀態':
            msg = await message.channel.send("系統努力加載中........請稍等")

            use = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            mess = '使用量: ' + \
                byte_to_largest(ram.used)
            my_system = platform.uname()
            cpu_name = get_cpu_info()['brand_raw']
            cpu_speed = get_cpu_info()['hz_advertised_friendly']
            lib = ctypes.windll.kernel32
            t = lib.GetTickCount64()
            t = int(str(t)[:-3])
            mins, sec = divmod(t, 60)
            hour, mins = divmod(mins, 60)
            days, hour = divmod(hour, 24)

            embed = discord.Embed(
                title='**主機狀態**', colour=random.randint(0, 0xffffff), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="**主機開機時間**",
                            value=f"{days}天{hour:02}小時{mins:02}分{sec:02}秒\n**CPU**\n名稱: {cpu_name}\n核心數: {psutil.cpu_count()}\n速度: {cpu_speed}\n使用量: " + str(use) + "%\n**RAM**\n" + mess)
            await msg.delete()
            await message.channel.send(embed=embed)

        elif message.content == '!status':
            msg = await message.channel.send("系統努力加載中........請稍等")

            use = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            mess = '使用量: ' + \
                byte_to_largest(ram.used)
            my_system = platform.uname()
            cpu_name = get_cpu_info()['brand_raw']
            cpu_speed = get_cpu_info()['hz_advertised_friendly']
            lib = ctypes.windll.kernel32
            t = lib.GetTickCount64()
            t = int(str(t)[:-3])
            mins, sec = divmod(t, 60)
            hour, mins = divmod(mins, 60)
            days, hour = divmod(hour, 24)

            embed = discord.Embed(
                title='**主機狀態**', colour=random.randint(0, 0xffffff), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="**主機開機時間**",
                            value=f"{days}天{hour:02}小時{mins:02}分{sec:02}秒\n**CPU**\n名稱: {cpu_name}\n核心數: {psutil.cpu_count()}\n速度: {cpu_speed}\n使用量: " + str(use) + "%\n**RAM**\n" + mess)
            await msg.delete()
            await message.channel.send(embed=embed)
            
        elif message.content == '！status':
            msg = await message.channel.send("系統努力加載中........請稍等")

            use = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            mess = '使用量: ' + \
                byte_to_largest(ram.used)
            my_system = platform.uname()
            cpu_name = get_cpu_info()['brand_raw']
            cpu_speed = get_cpu_info()['hz_advertised_friendly']
            lib = ctypes.windll.kernel32
            t = lib.GetTickCount64()
            t = int(str(t)[:-3])
            mins, sec = divmod(t, 60)
            hour, mins = divmod(mins, 60)
            days, hour = divmod(hour, 24)

            embed = discord.Embed(
                title='**主機狀態**', colour=random.randint(0, 0xffffff), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="**主機開機時間**",
                            value=f"{days}天{hour:02}小時{mins:02}分{sec:02}秒\n**CPU**\n名稱: {cpu_name}\n核心數: {psutil.cpu_count()}\n速度: {cpu_speed}\n使用量: " + str(use) + "%\n**RAM**\n" + mess)
            await msg.delete()
            await message.channel.send(embed=embed)


    async def on_raw_reaction_add(self, emoji):
        print(emoji)


def byte_to_largest(value):
    x = value
    y = 0
    prefix = ['B', 'K', 'M', 'G', 'T', 'P']
    while True:
        if x / 1024 > 1:
            x = x / 1024
            y += 1
        else:
            break
    return str(round(x, 2)) + prefix[y]


client = DCBOT()
client.run(jdata['TOKEN'])
