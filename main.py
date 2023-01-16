import discord, os, random, base64
from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
            os.system("cls")
            await client.wait_until_ready()
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("yes")) # change this to whatever you want
            print("------Information------")
            print(f"Logged in as:")
            print(f"Name: {client.user}.")
            print(f"ID: {client.user.id}.")
            print("Credits to lunar")
            print("----------------------")

client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name="mines", description="Use this command to predict your mines game!")
async def geekskid(interaction: discord.Interaction, round_id : str):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await interaction.response.send_message("you are gay lmao L")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣", "💣"
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = "⭐"
        elif a == 2:
            mine2 = "⭐"
        elif a == 3:
            mine3 = "⭐"
        elif a == 4:
            mine4 = "⭐"
        elif a == 5:
            mine5 = "⭐"
        elif a == 6:
            mine6 = "⭐"
        elif a == 7:
            mine7 = "⭐"
        elif a == 8:
            mine8 = "⭐"
        if b == 9:
            mine9 = "⭐"
        elif b == 10:
            mine10 = "⭐"
        elif b == 11:
            mine11 = "⭐"
        elif b == 12:
            mine12 = "⭐"
        elif b == 13:
            mine13 = "⭐"
        if c == 14:
            mine14 = "⭐"
        elif c == 15:
            mine15 = "⭐"
        elif c == 16:
            mine16 = "⭐"
        elif c == 17:
            mine17 = "⭐"
        if d == 18:
            mine18 = "⭐"
        elif d == 19:
            mine19 = "⭐"
        elif d == 20:
            mine20 = "⭐"
        elif d == 21:
            mine21 = "⭐"
        elif d == 22:
            mine22 = "⭐"
        elif d == 23:
            mine23 = "⭐"
        elif d == 24:
            mine24 = "⭐"
        elif d == 25:
            mine25 = "⭐"
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        grid = row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n"+ row5

        cool = random.randint(1, 4)
        shouldclick = f"**Should Click: **[{cool}]"
        tileamt = f"**Correct Tiles:** [4] "
        dashes = "------------------"
        information = f"**Information:**" + "\n" + f"```⭐ is a safe tile```" + "\n" + f"```💣 is a bomb/unknown area```"
        trust = f"**Don't trust the click information? Then just don't.**"

        em = discord.Embed(color=0x7400FF)
        em.add_field(name=base64.b64decode(b'IlNoYWRvdyBQcmVkaWN0b3Ii').decode('utf-8'),value=f"```{grid}```" + "\n" + f"**Game Data:**" + "\n" + "\n" + shouldclick + "\n" + tileamt + "\n" + dashes + "\n" + information + "\n" + trust)
        em.set_footer(text=base64.b64decode(b'c2tpZGRlZCBieSBsdW5hciMxNjc5').decode('utf-8'))
        await interaction.response.send_message(embed=em)

@tree.command(name='towers', description='play your fucking towers game')
async def geekskidder(interaction: discord.Interaction, round_id : str):
    correct = "⭐"
    bomb = "💣"
    round_length = len(round_id)
    if round_length < 36:
        await interaction.response.send_message("Invalid round id")
    elif round_length == 36:
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb,bomb
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)

        if a == 1:
            tower1 = correct
        elif a == 2:
            towe2 = correct
        elif a ==3:
            tower3 = correct
        if b == 1:
            tower4 = correct
        elif b == 2:
            tower5 = correct
        elif b ==3:  
            tower6 = correct
        if c == 1:
            tower7 = correct
        elif c == 2:
            tower8 = correct
        elif c ==3:
            tower9 = correct
        if d == 1:
            tower10 = correct
        elif d == 2:
            tower11 = correct
        elif d ==3:
            tower12 = correct
        if e == 1:
            tower13 = correct
        elif e == 2:
            tower14 = correct
        elif e ==3:
            tower15 = correct
        if f == 1:
            tower16 = correct
        elif f == 2:
            tower17 = correct
        elif f ==3:
            tower18 = correct
        if g == 1:
            tower19 = correct
        elif g == 2:
            tower20 = correct
        elif g ==3:
            tower21 = correct
        if h == 1:
            tower22 = correct
        elif h == 2:
            tower23 = correct
        elif h ==3:
            tower24 = correct

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24


        gridtowers = row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8 + "\n"


        cool = random.randint(1, 4)
        shouldclick = f"**Should Click: **[{cool}]"
        tileamt = f"**Correct Tiles: [{cool}]** "
        dashes = "---------------------"
        information = f"**Information:**" + "\n" + f"```⭐ is a safe tile```" + "\n" + f"```💣 is a incorrect spot/unknown area```"
        trust = f"**Don't trust the click information? Then just don't.**"

        em = discord.Embed(color=0x7400FF)
        em.add_field(name=base64.b64decode(b'IlNoYWRvdyBQcmVkaWN0b3Ii').decode('utf-8'),value=f"```{gridtowers}```" + "\n" + f"**Game Data:**" + "\n" + "\n" + shouldclick + "\n" + tileamt + "\n" + dashes + "\n" + information + "\n" + trust)
        em.set_footer(text=base64.b64decode(b'c2tpZGRlZCBieSBsdW5hciMxNjc5').decode('utf-8'))
        await interaction.response.send_message(embed=em)



client.run('')
