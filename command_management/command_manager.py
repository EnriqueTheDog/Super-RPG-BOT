import discord


class UniqueSelect(discord.ui.Select):
    def __init__(self, options: [discord.SelectOption]):
        super().__init__(
            placeholder="Elige...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        # TODO : [MUST] block any other command for the user while one command is not closed
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


class UniqueSelectionView(discord.ui.View):
    def __init__(self, options: [discord.SelectOption]):
        super().__init__()
        self.add_item(UniqueSelect(options))
