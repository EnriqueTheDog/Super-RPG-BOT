
import discord
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class WeaponSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Ataque melé", description="Ataque cuerpo a cuerpo. Puedes hacerte daño", emoji="⚔️"
            ),
            discord.SelectOption(
                label="Ataque a distancia", description="Ataca a distancia, desde un lugar seguro", emoji="🏹"
            ),
            discord.SelectOption(
                label="Magia", description="Utiliza magia. Es muy inestable", emoji="✨"
            ),
            discord.SelectOption(
                label="Milagro ofensivo", description="Poderes de los dioses antiguos. Te hará daño", emoji="🩸"
            ),
            discord.SelectOption(
                label="Milagro curativo", description="Pides ayuda a los dioses para curarte", emoji="🙌"
            ),
        ]
        super().__init__(
            placeholder="Elige...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        choices = {
            "melee": 0,
            "ranged": 1,
            "magic": 2,
            "miracle_off": 3,
            "miracle_heal": 4,
        }
        user_choice = self.values[0].lower()

        result_embed = discord.Embed(color=0x9C84EF)
        result_embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.avatar.url
        )

        result_embed.description = f"usaste **{user_choice}**!! Foah!!"
        result_embed.colour = 0xF59E42

        await interaction.response.edit_message(
            embed=result_embed, content=None, view=None
        )


class WeaponSelectionView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(WeaponSelect())


class Quest(commands.Cog, name="quest"):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(
        name="fight", description="Fight with a mob"
    )
    @checks.not_blacklisted()
    async def fight(self, context: Context) -> None:
        """
        Play the rock paper scissors game against the bot.

        :param context: The hybrid command context.
        """
        view = WeaponSelectionView()
        await context.send("Qué quieres hacer??", view=view)


async def setup(bot):
    await bot.add_cog(Quest(bot))
