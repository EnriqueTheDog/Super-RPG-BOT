import discord
from discord.ext import commands
from discord.ext.commands import Context

from command_management.command_manager import UniqueSelectionView
from game.classes.mob import Mob
from helpers import checks

from xml.dom.minidom import parse
import xml.dom.minidom


# TODO : [IMPORTANT] Add packages to requirements file (when the game is playable)


class Quest(commands.Cog, name="quest"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="fight", description="Fight with a mob"
    )
    @checks.not_blacklisted()
    async def fight(self, context: Context) -> None:
        """
        FIGHT!!!
        """
        # TODO : [IMPORTANT] Move all this code to "game" folder - cog files should only contain command names and defs

        mob = Mob(3)
        # TODO : [MUST] All this literature must be generated
        mob_appears_embed = discord.Embed(
            description=f'De repente aparece un {mob.name}!'
        )
        await context.send(embed=mob_appears_embed)
        max_mob_hp = mob.hp
        # TODO : [TRIVIAL] Can we paint an hp bar?
        hp_embed = discord.Embed(
            description=f'HP: {mob.hp}/{max_mob_hp}!'
        )
        await context.send(embed=hp_embed)

        while mob.hp > 0:
            # TODO : get this path out of here
            literature = xml.dom.minidom.parse(
                'C:\\Users\\orteg\\Documents\\Code\\Super-RPG-BOT\\game\\language\\literature\\command_literature.xml')
            collection = literature.documentElement
            txt_options = collection.getElementsByTagName('fight-option')
            options = []
            for option in txt_options:
                options.append(discord.SelectOption(
                    label=option.getElementsByTagName('label')[0].childNodes[0].nodeValue,
                    description=option.getElementsByTagName('description')[0].childNodes[0].nodeValue,
                    emoji=option.getElementsByTagName('emoji')[0].childNodes[0].nodeValue,
                    value=option.getElementsByTagName('value')[0].childNodes[0].nodeValue
                ))
            view = UniqueSelectionView(options)
            await context.send("Qué quieres hacer??", view=view)
            # deal dmg
            player_dmg = 10
            await context.send(embed=discord.Embed(
                description=f'Usó hachazo y hace {player_dmg}!'
            ))
            mob.hp -= player_dmg
            hp_embed = hp_embed = discord.Embed(
                description=f'HP: {mob.hp}/{max_mob_hp}!'
            )
            # mob attacks
            if mob.hp > 0:
                mob_dmg = mob.attack()
                mob_desc = discord.Embed(
                    description=f'{mob.name} usó lengüetazo e hizo {mob_dmg} de daño!'
                )
            else:
                mob_desc = discord.Embed(description=f'{mob.name} murió')
            await context.send(embed=mob_desc)


async def setup(bot):
    await bot.add_cog(Quest(bot))
