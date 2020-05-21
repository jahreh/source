#IMPORTS


#PREFIX
def get_prefix(client, message):
    with open('./path/to/file.json', 'r') as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)

@client.event
async def on_guild_join(guild):
    with open('./path/to/file.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '..'

    with open('./path/to/file.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('./path/to/file.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('./path/to/file.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command(aliases=['cp'])
async def changeprefix(ctx, prefix):
    with open('./path/to/file.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('./path/to/file.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix: **``{prefix}``**')
