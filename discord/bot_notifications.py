import discord
from discord.ext import commands

from scheduler_send import clear_messages
from notification_send import send_notifications

intents = discord.Intents.default()
intents.messages = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    guild = discord.utils.get(bot.guilds)
    if guild:
        print(f'Connected to guild: {guild.name} (ID: {guild.id})')
        # channel = discord.utils.get(guild.channels, name="grafik")
        channel = discord.utils.get(guild.channels, name="bot-test")
        if channel:
            print(f'Found channel: {channel.name} (ID: {channel.id})')
            await clear_messages(channel)
            await send_notifications(channel)
        else:
            print('Channel "powiadomienia" not found')
    else:
        print('No guilds found')
    await bot.close()


def run():
    with open('private_token.txt') as f:
        token = f.read().strip()
        bot.run(token)


if __name__ == "__main__":
    run()
