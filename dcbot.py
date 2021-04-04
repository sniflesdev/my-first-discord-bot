import asyncio

import discord

client = discord.Client()

from discord import Member

discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Bot online als User {}'.format(client.user.name))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))
        await asyncio.sleep(30)
        #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="snifles, schokodrink"))
        #await asyncio.sleep(30)
        #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Chat der allerechten"))
        #await asyncio.sleep(30)
        #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Meikels Katze"))
        #await asyncio.sleep(30)
        #await client.change_presence(activity=discord.Game('sniflesbot'), status=discord.Status.online)
        #await asyncio.sleep(60)


def is_not_pinned(mess):
    return not mess.pinned


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '!help' in message.content:
        await message.channel.send('**Dies ist der snifBot. Er wurde von snifles geschrieben und ist am 12.03.2021 herausgekommen!**')
        
    if '!snifles' in message.content:
        await message.channel.send('**snifles ist der developer/coder dieses Bots**')   

        
    if '!version' in message.content:
        await message.channel.send('**Der snifBot ist in der official Version 1.0**')
    
    if '!developer' in message.content:
        await message.channel.send('The developer of this bot is **officialsnifles#1234**')

    #if '!bot' in message.content:
     #   await message.channel.send('**!bot** hat noch keine Benutzung! Die Benutzung dieses Comands kommt mit der **Version 0.2** welche am **13.02.2021** Veröffentlich wird.')



    if '!lol' in message.content:
        await message.channel.send('lol')



    if '!test' in message.content:
        await message.channel.send('test')


    if message.content.startswith('!clear'):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1])+1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('{} Nachicht(en) von snifBot gelöscht.'.format(len(deleted)-1))




    if '!kiss' in message.content:
        await message.channel.send('Kiss')




    
        
        


    #if message.content.startswith('!userinfo'):
        #args = message.content.split(' ')
        #if len(args) == 2:
            #member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            #if member:
               # embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                       description='Dies ist die Userinfo für den User {}'.format(member.mention),
                       color =0x22a7f0)
                #embed.add_field(name ='Server beigetreten', value=member.joined_at.strftime('%d/%m/Y, %H:%M:%S'),
                       inline=True)

                #embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/Y, &H:%M:%S'),
                       inline=True)

                #for role in member.roles:
                 #   if not role.is_default():
                       rollen += '{} \r\n'.format(role.mention)
                #if rollen:
                #    embed.add_field(name='Rollen', value=rollen, inline=True)

               # embed.set_thumbnail(url=member.avatar_url)
                #embed.set_footer(text='Ich vin ein EmbedFooter.')
                #await message.channel.send(embed=embed)




client.run('################################################')
