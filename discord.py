#IMPORTS


#PREFIX
#This is to open and load/read the prefix designated for the server from
#a Prefix JSON File
def get_prefix(client, message):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

#Client or Bot will call on the loaded prefix
client = commands.Bot(command_prefix=get_prefix)

#When joining Guild/Server, Prefix JSON File is loaded/read and
#a pre-made prefix is dumped/written referenced as Guild ID
@client.event
async def on_guild_join(guild):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '..'

    with open('./path/to/prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#When removed from Guild/Server, Prefix JSON File is loaded/read
@client.event
async def on_guild_remove(guild):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))
#Prefix referenced to Guild ID is "removed" or dumped/written empty
    with open('./path/to/prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#With command, Prefix JSON File is loaded/read
@client.command(aliases=['cp'])
async def changeprefix(ctx, prefix):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix
#The chosen "prefix" will be dumped/written, replacing pre-made prefix
    with open('./path/to/prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
#Prefix is sent to author
    await ctx.send(f'Prefix: **``{prefix}``**')

#INVITE
@commands.command(aliases=['link'])
async def invite(ctx):
    invite_link = '[INVITE URL]'
    await ctx.send(invite_link)

#SAVE/UPLOAD
@commands.command(aliases=['upl'])
async def save(ctx, index, *, content):
    with open('./path/to/images.json', 'r') as p:
        contents = json.load(p)

    contents[str(index)] = content

    with open('./path/to/images.json', 'w') as p:
        json.dump(contents, p, sort_keys=True,
                  indent=4, separators=(',', ': '))

    emoji = '✅'

    await ctx.send(f"Done {emoji}")

#OPEN
@commands.command(aliases=['opn'])
async def open(ctx, index):
    with open('./path/to/images.json', 'r') as p:
        contents = json.load(p)
    contents[str(index)]
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_image(url=contents[str(index)])

    await ctx.send(embed=embed)
