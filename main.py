import discord
from discord.ext import commands
from discord.ext.commands import Context
import config
from typing import Union

class SimpleBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix = "!",
            help_command = None,
            intents = discord.Intents.default(),
            case_insensitive = True,
        )

bot: SimpleBot = SimpleBot()

@bot.command(name="help", description = "Shows a list of commands.")
async def help(ctx: Context) -> None:
    embed = discord.Embed()
    embed.title = f"{bot.user.name} Help Menu"
    embed.description = (
        f"**I am open sourced on [Github](#)** \n"
        f"I am a Utility bot with the following commands. \n\n"
        f"`1.` Avatar - Shows a user avatar. \n"
        f"`2.` Banner - Shows a user banner. \n"
        f"`3.` Userinfo - Shows a user info. \n"
        f"`4.` Serverinfo - Shows the server info. \n"
        f"`5.` Botinfo - Shows the information related to me. \n" 
    )

    await ctx.send(embed=embed)

@bot.command(name = "avatar", description = "Shows a user avatar.", aliases = ["av"])
async def avatar(ctx: Context, user: Union[discord.User, discord.Member] = None) -> None:
    if user is None:
        user = ctx.author
    
    embed = discord.Embed()
    embed.title = "Avatar"
    embed.set_image(url=user.display_avatar.url)

    await ctx.send(embed=embed)

@bot.command(name="banner", description = "Shows a user banner.")
async def banner(ctx: Context, user: Union[discord.User, discord.Member] = None):
    if user is None:
        user = ctx.author

    user = bot.fetch_user(user.id)

    if user.banner:
        embed = discord.Embed()
        embed.title = "Banner"
        embed.set_image(url=user.banner.url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed()
        embed.set_author(name = "User doesn't have any banner.", icon_url = user.display_avatar.url)
        await ctx.send(embed=embed)

@bot.command()
async def serverbanner(ctx: Context) -> None:
    pass

bot.run(token=config.Bot_Token)

