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
    await bot.send_message(discord.Object(id='459871164974628886'), "BEEP BOOP")
   
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
        await bot.send_message(henry, "The user {0.author.mention} has reported someone".format(message))
        rehan = await bot.get_user_info('310045671094747136')
        await bot.send_message(rehan, "The user {0.author.mention} has reported someone".format(message))

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

    #if message.content.upper().startswith('.RULE4'):
        #await bot.send_message(message.channel,"#4 Please do not spam in the server. It is rude and unnecessary.")

    #if message.content.upper().startswith('RULE 4'):
        #await bot.send_message(message.channel,"##4 Please do not spam in the server. It is rude and unnecessary.")

    if message.content.upper().startswith('.YT'):
        await bot.send_message(message.channel,"https://www.youtube.com/channel/UCel2B-6wZhvQHRAKXmpm1Ew")

    if message.content.upper().startswith('.YOUTUBE'):
        await bot.send_message(message.channel,"https://www.youtube.com/channel/UCel2B-6wZhvQHRAKXmpm1Ew")

    if message.content.upper().startswith('.PING'):
        await bot.send_message(message.channel,"PONG {0.author.mention}".format(message))
        
    if message.content.upper().startswith('.COMMANDS'):
        await bot.send_message(message.channel," .help: Shows this \n .rules : Displays the rules \n .rules(number of rule): Displays specific rules \n .yt: Link to Eddie's channel! \n .boop: Boops someone \n .info: Shows info about the bot")
        
    #if message.content.upper().startswith(''):
        #await bot.send_message(message.channel,"")
#( ͡° ͜ʖ ͡°)

    await bot.process_commands(message)

@bot.command(pass_context=True)
async def boop(ctx, message):
    """Boops someone"""
    await client.send_message(ctx.message.author, 'Booped!')                           
@bot.command(pass_context=True)
async def info(ctx):
    """Information about the bot"""
    embed=discord.Embed(title="The first Saucefam bot!", description="Functions: Being fun and playing music.", color=0x00FF00)
    embed.set_author(name="WIREDuardo")
    embed.set_footer(text="Created by Robert Jefferson")
    await bot.say(embed=embed)
    print("Information accesed")
@bot.command
async def rules(ctx):
    """Shows da rulez"""

@bot.command
@bot.command

#if __name__ == "__main__":
        #for extension in startup_extensions:
            #try:
                #bot.load_extension(extension)
            #except Exception as e:
                #exc = '(): ()'.format(type(e).__name__, e)
                #print('Failed to load extension ()\n()'.format(extension, exc))
                
bot.run("NDYwOTQwNTg3NTUwNTA3MDY3.DhMgGQ.3CVkea3M2zYl5Wul4E3Fd6ER-iE")
