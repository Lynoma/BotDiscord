#IMPORTS
import os
import asyncio
import discord
import discord.voice_client
import random
from datetime import datetime, timedelta
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from keep_alive import keep_alive

#DATA

intents = discord.Intents.all()

TOKEN = 'ODY3NjczMzM4NjI0NjA2MjQ4.YPkhxA.QymQlTTCZbVsVWgPgrL-S7JeMD4'
GUILD = 'Comrade Cooked Chicken Party'

client = discord.Client(intents= intents)
bot = commands.Bot(command_prefix='$', intents = intents)

global SentenceActive
SentenceActive = False

global UserAllowed 
UserAllowed = True

def todayAt (timenow, hr, min=0, sec=0, micros=0):
    now = timenow
    return now.replace(hour=hr, minute=min, second=sec) 

global Agrid
Agrid = [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:"]
global marker
marker = ":x:"
global gameEnded
gameEnded = False


def one():
    if(Agrid[0] == ":white_large_square:"):
        Agrid[0] = marker
        swapPlayer()
def two():
    if(Agrid[1] == ":white_large_square:"):
        Agrid[1] = marker
        swapPlayer()
def three():
    if(Agrid[2] == ":white_large_square:"):
        Agrid[2] = marker
        swapPlayer()
def four():
    if(Agrid[3] == ":white_large_square:"):
        Agrid[3] = marker
        swapPlayer()
def five():
    if(Agrid[4] == ":white_large_square:"): 
        Agrid[4] = marker
        swapPlayer()
def six():
    if(Agrid[5] == ":white_large_square:"):
        Agrid[5] = marker
        swapPlayer()
def seven():
    if(Agrid[6] == ":white_large_square:"):
        Agrid[6] = marker
        swapPlayer()
def eight():
    if(Agrid[7] == ":white_large_square:"):
        Agrid[7] = marker
        swapPlayer()
def nine():
    if(Agrid[8] == ":white_large_square:"):
        Agrid[8] = marker
        swapPlayer()

def choosemove(a):
    global marker
    try:
        a = int(a)
        if(a < 1 or a > 9):
            a = 10
    except:
        a = 10
    return a

def swapPlayer():
    global marker
    if marker == ":x:":
        marker = ":o:"
    else:
        marker = ":x:"

def checkEnded():
    if (Agrid[0] == Agrid[1] == Agrid[2] and Agrid[0] != ":white_large_square:"):
        return True
    if (Agrid[3] == Agrid[4] == Agrid[5] and Agrid[3] != ":white_large_square:"):
        return True
    if (Agrid[6] == Agrid[7] == Agrid[8] and Agrid[6] != ":white_large_square:"):
        return True

    if(Agrid[0] == Agrid[3] == Agrid[6] and Agrid[0] != ":white_large_square:"):
        return True
    if(Agrid[1] == Agrid[4] == Agrid[7] and Agrid[1] != ":white_large_square:"):
        return True
    if(Agrid[2] == Agrid[5] == Agrid[8] and Agrid[2] != ":white_large_square:"):
        return True
    
    if(Agrid[0] == Agrid[4] == Agrid[8] and Agrid[0] != ":white_large_square:"):
        return True
    if(Agrid[2] == Agrid[4] == Agrid[6] and Agrid[2] != ":white_large_square:"):
        return True
    
    if(Agrid[0] != ":white_large_square:" and Agrid[1] != ":white_large_square:" and Agrid[2] != ":white_large_square:" and Agrid[3] != ":white_large_square:" and Agrid[4] != ":white_large_square:" and Agrid[5] != ":white_large_square:" and Agrid[6] != ":white_large_square:" and Agrid[7] != ":white_large_square:" and Agrid[8] != ":white_large_square:" ):
        return True
    
    return False

switch_case = {
    1 : one,
    2 : two,
    3 : three,
    4 : four,
    5 : five,
    6 : six,
    7 : seven,
    8 : eight,
    9 : nine
}
        

#EVENTS

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
  
    for member in guild.members:
        print("-" + member.name)
        if (member.name == "ZVP_D4rk"):
            global MemberBully
            MemberBully = member
            print (MemberBully)



@bot.event
async def on_message(message):
    #Permet de faire fonctionner les commandes
    await bot.process_commands(message)
    #Empêche une boucle de messages
    if message.author == bot.user:
        return
    

    if message.content.startswith('$help'):
        return 
    if message.content.startswith('$enable'):
        return 
    if message.content.startswith('$disable'):
        return
    if message.content.startswith('$slap'):
        return
    if message.content.startswith('$flame'):
        return
    if message.content.startswith('$roll'):
        return
    if message.content.startswith('$rickroll'):
        return
    if message.content.startswith('$leave'):
        return
    if message.content.startswith('!bully'):
        global MemberBully
        for i in range(0,10):
            await MemberBully.create_dm()
            await MemberBully.dm_channel.send("Joyeux anniversaire !")
            print('done')


    timenow = datetime.today()
    timenow = timenow + timedelta(hours = 2)
    #Vérifie si le bot est actif ou non
    if (SentenceActive == True):
        if (timenow < todayAt(timenow, 6) or timenow > todayAt(timenow, 23)):
            #await message.channel.send(f'{message.author.mention} va te coucher')
            TheMember = message.author
            await TheMember.create_dm()
            await TheMember.dm_channel.send("Va te coucher")
            print("message envoyé")
        else:
            print("pas de message envoyé, car message doit être envoyé avant ", todayAt(timenow, 6), " ou après ", todayAt(timenow, 23), " . Il est   ", timenow)
    else:
        print("Le bot est inactif")



# $enable
@bot.command(name='enable', help='Active les phrases va te coucher')
async def enableBot(ctx):
    global SentenceActive
    SentenceActive = True
    print("Bot actif")
    await ctx.send("Bot activé !")



# $disable
@bot.command(name='disable', help='Désactive les phrases va te coucher')
async def disableBot(ctx):
    global SentenceActive
    SentenceActive = False
    print("Bot inactif")
    await ctx.send("Bot désactivé !")

#Cooldown message


# $slap
@bot.command(name='slap', help='Slap un utilisateur')
@commands.cooldown(1,3, commands.BucketType.user)
async def slapUser(ctx):
    with open('TextFiles/Slap.txt', 'r') as f:
        print("file openend")
        Lines = f.readlines()
        response = random.choice(Lines)
        print(response)
        await ctx.send(response)


# $flame
@bot.command(name='flame', help='Flame un utilisateur')
@commands.cooldown(1,3, commands.BucketType.user)
async def flameUser(ctx):
  with open('TextFiles/Flame.txt', 'r') as f:
    print("file openend")
    Lines = f.readlines()
    response = random.choice(Lines)
    print(response)
    await ctx.send(response)



# $loli
@bot.command(name='loli', help='O KAWAII KOTO')
@commands.cooldown(1,3, commands.BucketType.user)
async def loli(ctx):
  with open('TextFiles/Loli.txt', 'r') as f:
    print("file openend")
    Lines = f.readlines()
    response = random.choice(Lines)
    print(response)
    await ctx.send(response)



# $sendFBI
@bot.command(name='sendFBI', help='FBI OPEN UP')
@commands.cooldown(1,3, commands.BucketType.user)
async def sendFBI(ctx):
  with open('TextFiles/sendFBI.txt', 'r') as f:
    print("file openend")
    Lines = f.readlines()
    response = random.choice(Lines)
    print(response)
    await ctx.send(response)



# $roll
@bot.command(name='roll', help='$roll choix1,choix2,choixN pour tirer au sort une des options')
@commands.cooldown(1,3, commands.BucketType.user)
async def rollChoice(ctx, ChoiceList):
    Spl = ChoiceList.split(',')
    random_choice = random.choice(Spl)
    print(random_choice)
    await ctx.send("Le choix sélectionné est {0}".format(random_choice))



# $play
@bot.command(name='play', help='Jouer au morpion')
@commands.cooldown(1,3, commands.BucketType.user)
async def play(ctx, yourMove):
    global gameEnded
    if (gameEnded == False):
        firstmove = yourMove
        move = choosemove(firstmove)
        switch_case[move]()
        await ctx.send(Agrid[0] + Agrid[1] + Agrid[2])
        await ctx.send(Agrid[3] +  Agrid[4] + Agrid[5])
        await ctx.send(Agrid[6] + Agrid[7] + Agrid[8])
        if(checkEnded() == True):
            gameEnded = True
            await ctx.send("Jeu Terminé !")

# $morpion
@bot.command(name='morpion', help='Jouer au morpion')
@commands.cooldown(1,3, commands.BucketType.user)
async def play(ctx):
    global gameEnded
    gameEnded = False
    global Agrid 
    Agrid = [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:"]
    await ctx.send("Nouvelle partie !")


@bot.command(help="disconnect bot from channel")
async def leave(ctx):
    await ctx.voice_client.disconnect()
    



keep_alive()
bot.run(TOKEN)
client.run(TOKEN)