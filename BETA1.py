import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from random import randint

rando = randint(0,10)

startup_extensions = ["Music"]
bot = commands.Bot(".")

@bot.event
async def on_ready():
    print("Bot Online")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot
class Information:
    @bot.command(pass_context=True)
    async def rules(ctx):
        """Shows Da Rulez"""
        await bot.say(" #1 - Be respectul and kind towards others here. Anyone caught harassing or insulting others will receive a warning followed by a kick. \n #2 Dont advertise. Just dont. Its rude and annoying. \n #3 Keep all adult and nudity content away from here. Immediate ban for anyone posting obscenities.")
        print("Rules requested")

    @bot.command(pass_context=True)
    async def info(ctx):
        """Information about the bot"""
        embed=discord.Embed(title="The first Saucefam bot!", description="Functions: Being fun and playing music.", color=0x00FF00)
        embed.set_author(name="WIREDuardo")
        embed.set_footer(text="Created by Sammy the Destroyer")
        await bot.say(embed=embed)
        print("Information accesed")
class Fun:
    @bot.command(pass_context=True)
    async def gay(ctx):
        """No U"""
        await bot.say("https://cdn.discordapp.com/attachments/436290304606339073/461027818474700800/image.jpg")
        print("No U initialized")

    @bot.command(pass_context=True)
    async def Snoopy_legacy(ctx):
        """May he rest in peace"""
        await bot.say("Snoopy's memory echoes with the wind...")
        await bot.say("Poopy-di scoop\nScoop-diddy-whoop\nWhoop-di-scoop-di-poop\nPoop-di-scoopty\nScoopty-whoop\nWhoopity-scoop, whoop-poop\nPoop-diddy, whoop-scoop\nPoop, poop\nScoop-diddy-whoop\nWhoop-diddy-scoop\nWhoop-diddy-scoop, poop")
        print("Snoopy's memory echoes with the wind...")

    @bot.command(pass_context=True)
    async def lenny(ctx):
        """It's dangerous to go alone. Take this."""
        await bot.say("It's dangerous to go alone! Take this.")
        await bot.say("( ͡° ͜ʖ ͡°)")
        print("Have a Lenny!")

    @bot.command(pass_context=True)
    async def edgy(ctx):
        """You and your goth stuff..."""
        await bot.say("Well SOMEONE is being edgy!")
        print("Edgy stuff")
        
    @bot.command(pass_context=True)
    async def legendofrehan(ctx):
        """A tale from a long forgotten tribe of a species called Rehan."""
        await bot.say('**The Legend Of Rehan, a tale from a long forgotten tribe of a species from long ago. The story goes as the ancient one once described:** \n \n "All the little Rehans go to sleep at bedtime. Mommy Rehan reads little Rehan a story. Once upon a time, there was a little Rehan that wanted to explore the world. His mom told him: "Rehan, you need to be big and strong to travel the world", so Rehan ate all of his veggies and excercised very hard until he became very strong. He wanted to become the best adventurer! Once ready, he said goodbye to his mom and went exploring. He traveled far and wide and met many amazing people. One of those people was Nick. Nick was a virgin with asian decent. They both became friends immediately. Rehan asked him if he wanted to go explore with him, and he said yes. After many adventures they fell in love and got married. They fucked and lived happily ever after. The End."')
        print("You don't know what you have done...")

    @bot.command(pass_context=True)
    async def xd(ctx):
        """xd"""
        await bot.say("xd")
        print("Are you fucking nine?")

    @bot.command(pass_context=True)
    async def rank(ctx):
            """Rank your stuff"""
            await bot.say("10/10")
            print("Rank my peepee pls")
            
    @bot.command(pass_context=True)
    async def pr0n(ctx):
        """Nice"""
        await bot.say("https://cdn.discordapp.com/attachments/436290304606339073/461028851011551233/image.jpg")
        print("sexy")
    

if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '(): ()'.format(type(e).__name__, e)
                print('Failed to load extension ()\n()'.format(extension, exc))

bot.run("NDYwOTQwNTg3NTUwNTA3MDY3.DhMgGQ.3CVkea3M2zYl5Wul4E3Fd6ER-iE")

