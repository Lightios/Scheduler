import discord


async def send_notifications(channel):
    names = get_names()

    user_id = 465866795648024576
    user = await channel.guild.fetch_member(user_id)
    await channel.send(f"{user.mention}")


def get_names() -> list[str]:
    pass