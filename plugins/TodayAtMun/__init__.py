import discord
from os import path
from discord.ext import commands
from plugins.TodayAtMun.Month import month
from datetime import datetime
from json import load

from Plugin import AutomataPlugin


class TodayAtMun(AutomataPlugin):
    """
        Provides Info Of Significant Dates on the Mun Calendar
    """

    def __init__(self, manifest, bot):
        super().__init__(manifest, bot)
        with open(path.join(self.manifest["path"], "diary.json"), "r") as f:
            self.info = load(f)


    def getCurrDate(self):
        """ Provides Current Date formatted to Muns style."""

        date = str(datetime.now().strftime("%Y-%#m-%#d-%A")).split("-")

        currYear = date[0]
        currMonth = int(date[1])
        currDay = date[2]
        currDayOfWeek = date[3]

        return f"{month[currMonth]} {currDay}, {currYear}, {currDayOfWeek}"

    @commands.command()
    async def today(self, ctx):
        date = self.getCurrDate()
        print(f"Today is: {date}.")
