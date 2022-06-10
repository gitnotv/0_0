import discord
from discord.ext import commands

class context():

    # Needs upgrading slow atm (0.05)
    async def wait_for_message(client : commands.Bot, time : int, author : discord.Member = None, channel : discord.TextChannel = None, guild : discord.Guild = None):

        # All arguments provided
        if author != None and channel != None and guild != None:
            return await client.wait_for("message", check = lambda m: m.author == author and m.channel == channel and m.guild == guild, timeout=time)

        # Author only match
        elif author != None and channel == None and guild == None:
            return await client.wait_for("message", check = lambda m: m.author == author, timeout=time)

        # Author and channel
        elif author != None and channel != None and guild == None:
            return await client.wait_for("message", check = lambda m: m.author == author and m.channel == channel, timeout=time)

        # Channel only match
        elif author == None and channel != None and guild == None:
            return await client.wait_for("message", check = lambda m: m.channel == channel, timeout=time)

        # Channel and guild
        elif author == None and channel != None and guild != None:
            return await client.wait_for("message", check = lambda m: m.author == author and m.channel == channel and m.guild == guild, timeout=time)

        # Guild only match
        elif author == None and channel == None and guild != None:
            return await client.wait_for("message", check = lambda m: m.guild == guild, timeout=time)

        # Author and guild
        elif author != None and channel == None and guild != None:
            return await client.wait_for("message", check = lambda m: m.author == author and m.guild == guild, timeout=time)
        
        # No args
        else:
            return await client.wait_for("message", timeout=time)


