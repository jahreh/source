#IMPORTS


#PREFIX
def get_prefix(client, message):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)

@client.event
async def on_guild_join(guild):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '..'

    with open('./path/to/prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('./path/to/prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command(aliases=['cp'])
async def changeprefix(ctx, prefix):
    with open('./path/to/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('./path/to/prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
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
