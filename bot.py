import discord
import re
from discord.ext import commands
from urllist import UrlList

urls = UrlList()  # manages the urls

help_msg = "This discord bot extracts urls/links from user messages and these links" \
           "be accessed easily via the bot.\n\n" \
           "Commands:\n\n" \
           "$last5links : \n returns the last 5 urls/links sent on the server\n\n" \
           "$getlinks number_of_links :\n returns a specified amount of links if available. An error message is " \
           "returned" \
           "if there isn't\n\n" \
           "$getlinktype number_of_links ext :\n returns links based on the extension(e.g: .pdf). If the link" \
           "amount exceeds what is available, then whatever is available is returned"
client = commands.Bot(command_prefix='$')
client.remove_command('help')  # removes the default help command


# function that displays a list's contents in a single string
def list_to_str(url_list):
    message = ''
    for url in url_list:
        message += url + '\n\n'
    return message


@client.event  # variable is client, so decorator must be client.____
async def on_ready():  # causes the bot to go online
    print('bot is ready.')


# reads messages and extracts links
@client.event
async def on_message(message):
    if not message.author.bot:  # ignores messages from bots
        msg = message.content
        url_list = re.findall(r'(https?://\S+)', msg)  # extracts all links into a list
        urls.add_elem(url_list)
    await client.process_commands(message)


@client.command(name='getlinks')
async def _get_links(ctx, arg: int):
    """
    Gets a certain amount of links based on the number provided
    -if number exceeds amount of urls, on_command_error() gets called
    arg:number of links requested
    """
    url = list_to_str(urls.get_n_elem(arg))
    await ctx.send(url)


@client.command(name='getlinktype')
async def _get_link_ext(ctx, num: int, ext: str):
    """
        Gets links based on the extension type(e.g .pdf, .html, .png)
        arg - number of links requested.
        ext- the extension used to filter

        If arg exceeds the number of links with a particular extension, the all the links with that extension are sent
    """
    url = list_to_str(urls.get_by_ext(num, ext))
    await ctx.send(url)


# returns the last 5 links sent in the discord chat
@client.command(name='last5links')
async def last_5_links(ctx):
    msg = list_to_str(urls.last_5())
    await ctx.send(msg)


@client.command(pass_context=True)
async def help(ctx):
    user = ctx.message.author
    await user.send(help_msg)


# message that gets sent when a command is called incorrectly
@client.event
async def on_command_error(ctx, error):
    await ctx.send("Invalid arguments")


client.run('NjY5NjMyNTA2MDcyNjYyMDQx.XjjJww.2Ys8t4C5EjUsBO0KjAQQT_26g8o')
