import time
from datetime import datetime

import discord

from data import DATA
from name_to_id import name_to_id


class Data:
    def __init__(self, name, start_hour, start_minute, day, duration, description):
        self.name = name
        self.start_hour = Data.number_to_hour(start_hour)
        self.start_minute = Data.number_to_hour(start_minute)
        self.day = day
        self.duration = duration
        self.description = description

    @staticmethod
    def number_to_hour(number):
        if number < 10:
            return f"0{number}"
        return str(number)


async def send_notifications(channel):
    data = get_data()

    for row in data:
        row = Data(*row)
        user_id = name_to_id[row.name]
        user = await channel.guild.fetch_member(user_id)

        message = f"{user.mention} jutrzejsze zajęcia o {row.start_hour}:{row.start_minute} - jeśli nie będziesz w stanie uczestniczyć, proszę o informację."
        await channel.send(message)
        print(message)


def get_data() -> list[list]:
    tomorrow = datetime.today().weekday() + 1

    if tomorrow == 7:
        tomorrow = 0

    tomorrow += 1  # 1-indexed
    return [["test", 2, 3, 4, 5, 6],]
    return filter(lambda x: x[3] == tomorrow, DATA)

