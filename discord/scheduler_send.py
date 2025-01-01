import discord
from discord.ext import commands


async def clear_messages(channel):
    def is_not_pinned(message):
        return not message.pinned

    deleted = await channel.purge(limit=None, check=is_not_pinned)
    print(f'Deleted {len(deleted)} messages from {channel.name}')


async def send_image(channel):
    with open('../result.png', 'rb') as f:
        picture = discord.File(f)
        await channel.send(file=picture)
    print(f'Sent image to {channel.name}')


async def send_annotation(channel):
    with open('../annotated_image.png', 'rb') as f:
        picture = discord.File(f)
        await channel.send(file=picture)
    print(f'Sent annotation to {channel.name}')