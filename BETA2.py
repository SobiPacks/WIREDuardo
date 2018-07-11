import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from random import randint

mods = ["400055843787243531"]
rando = randint(1,9)
bypass_list = [""]
chat_filter = ["OOGIEPOOGIENIGGERNOGGER"]
#startup_extensions = ["Music"]
bot = commands.Bot(".")

#459871164974628886 - living room
#436290304606339073 - inkopolis plaza
@bot.event
async def on_ready():
    rando
    print("Bot Online")
    print(rando)
    await bot.change_presence(game=discord.Game(name="Splatoon 2"))
    if rando == '1':
        await bot.send_message(discord.Object(id='436290304606339073'), "Now with extra apples!")
    if rando == '2':
        await bot.send_message(discord.Object(id='436290304606339073'), "My controller is broken from the inside but cold in the outside, like a fish.")
    if rando == '3':
        await bot.send_message(discord.Object(id='436290304606339073'), "Can I get an amen?")
    if rando == '4':
        await bot.send_message(discord.Object(id='436290304606339073'), "I'm baaaaaaack!")
    if rando == '5':
        await bot.send_message(discord.Object(id='436290304606339073'), "Get fire up!")
    if rando == '6':
        await bot.send_message(discord.Object(id='436290304606339073'), "I don't have Discord Nitro :(")
    if rando == '7':
        await bot.send_message(discord.Object(id='436290304606339073'), "Everything made out of buttons and wires.")
    if rando == '8':
        await bot.send_message(discord.Object(id='436290304606339073'), "WHY AM I IN PAIN?")
    if rando == '9':
        await bot.send_message(discord.Object(id='436290304606339073'), "I have a big red dog kids.")

#class Main_Commands():
    #def __init__(self, bot):
        #self.bot = bot

@bot.command(pass_context=True)
async def poke(ctx, member: discord.Member):
    await bot.send_message(mods, 'boop')
    print("BOOP")
@bot.event
async def on_message(message):
    if message.content.upper().startswith('.REPORT'):
        if message.author == bot.user:
            return
        rob = await bot.get_user_info('400055843787243531')
        await bot.send_message(rob, "The user {0.author.mention} has reported someone".format(message))
        henry = await bot.get_user_info('258675615194939392')
        await bot.send_message(henry, "Henry, alguien hizo .report".format(message))
        rehan = await bot.get_user_info('310045671094747136')
        await bot.send_message(rehan, "A user has sent a report request!".format(message))

    if message.content.upper().startswith('.RULES'):
        await bot.send_message(message.channel," #1 - Be respectul and kind towards others here. Anyone caught harassing or insulting others will receive a warning followed by a kick. \n #2 Dont advertise. Just dont. Its rude and annoying. \n #3 Keep all adult and nudity content away from here. Immediate ban for anyone posting obscenities. ")

    if message.content.upper().startswith('.RULE1'):
        await bot.send_message(message.channel,"#1 - Be respectul and kind towards others here. Anyone caught harassing or insulting others will receive a warning followed by a kick. ")

    if message.content.upper().startswith('.RULE 1'):
        await bot.send_message(message.channel,"#1 - Be respectul and kind towards others here. Anyone caught harassing or insulting others will receive a warning followed by a kick. ")

    if message.content.upper().startswith('.RULE2'):
        await bot.send_message(message.channel,"#2 Dont advertise. Just dont. Its rude and annoying.")

    if message.content.upper().startswith('.RULE 2'):
        await bot.send_message(message.channel,"#2 Dont advertise. Just dont. Its rude and annoying.")

    if message.content.upper().startswith('.RULE3'):
        await bot.send_message(message.channel,"#3 Keep all adult and nudity content away from here. Immediate ban for anyone posting obscenities. ")

    if message.content.upper().startswith('.RULE 3'):
        await bot.send_message(message.channel,"#3 Keep all adult and nudity content away from here. Immediate ban for anyone posting obscenities. ")

    if message.content.upper().startswith('.RULE4'):
        await bot.send_message(message.channel,"#4 Please do not spam in the server. It is rude and unnecessary.")

    if message.content.upper().startswith('RULE 4'):
        await bot.send_message(message.channel,"##4 Please do not spam in the server. It is rude and unnecessary.")

    if message.content.upper().startswith('.YT'):
        await bot.send_message(message.channel,"https://www.youtube.com/channel/UCel2B-6wZhvQHRAKXmpm1Ew")

    if message.content.upper().startswith('.YOUTUBE'):
        await bot.send_message(message.channel,"https://www.youtube.com/channel/UCel2B-6wZhvQHRAKXmpm1Ew")

    if message.content.upper().startswith('.PING'):
        await bot.send_message(message.channel,"PONG {0.author.mention}".format(message))
        
    #if message.content.upper().startswith(''):
        #await bot.send_message(message.channel,"")
#( ͡° ͜ʖ ͡°)

    await bot.process_commands(message)

#@bot.command(pass_context=True)
#async def info(ctx):
    #"""Information about the bot"""
    #embed=discord.Embed(title="The first Saucefam bot!", description="Functions: Being fun and playing music.", color=0x00FF00)
    #embed.set_author(name="WIREDuardo")
    #embed.set_footer(text="Created by Robert Jefferson")
    #await bot.say(embed=embed)
    #print("Information accesed")

#if __name__ == "__main__":
        #for extension in startup_extensions:
            #try:
                #bot.load_extension(extension)
            #except Exception as e:
                #exc = '(): ()'.format(type(e).__name__, e)
                #print('Failed to load extension ()\n()'.format(extension, exc))
                
bot.run("NDYwOTQwNTg3NTUwNTA3MDY3.DhMgGQ.3CVkea3M2zYl5Wul4E3Fd6ER-iE")
