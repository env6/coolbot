import discord
import hashlib
import os

TOKEN = 'MTUwNjY3NDEzMjc0ODczNDUyNg.G2TkRl.M2bbjSTasz4gTQYVW6gh2fnf47rI830kgvEIdw'  # Paste your NEW token after resetting
VERIFY_URL = 'https://authgg.rf.gd/'  # Your hosted page URL

class Bot(discord.Client):
    async def on_ready(self):
        print(f'[+] Bot is online as {self.user}')

    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.startswith('!verify'):
            user_hash = hashlib.md5(str(message.author.id).encode()).hexdigest()[:8]
            verify_link = f"{VERIFY_URL}/?uid={user_hash}"
            embed = discord.Embed(
                title="🔐 Server Verification Required",
                description=f"**[Click Here to Verify]({verify_link})**",
                color=0x5865F2
            )
            await message.channel.send(content=f"{message.author.mention}", embed=embed)

client = Bot(intents=discord.Intents.all())
client.run(TOKEN)
