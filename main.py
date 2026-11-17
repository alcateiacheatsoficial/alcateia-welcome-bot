import os
import logging
import discord

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("alcateia-welcome-bot")

TOKEN = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL_NAME = os.getenv("WELCOME_CHANNEL_NAME", "Entrada")
SERVER_NAME = os.getenv("SERVER_NAME", "Alcateia Cheats 2.0")

if not TOKEN:
    raise RuntimeError("A variável DISCORD_TOKEN não foi configurada.")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    log.info("Bot conectado como %s (ID: %s)", client.user, client.user.id)
    for guild in client.guilds:
        log.info("Servidor disponível: %s (ID: %s)", guild.name, guild.id)


@client.event
async def on_member_join(member: discord.Member):
    channel = discord.utils.find(
        lambda item: isinstance(item, discord.TextChannel)
        and item.name.casefold() == WELCOME_CHANNEL_NAME.casefold(),
        member.guild.text_channels,
    )
    if channel is None:
        log.warning("Canal #%s não encontrado em %s.", WELCOME_CHANNEL_NAME, member.guild.name)
        return

    message = (
        f"🐺 Bem-vindo à matilha, {member.mention}!\\n"
        f"Você acaba de chegar à **{SERVER_NAME}**.\\n"
        "Leia as regras e aproveite o servidor! 🐺"
    )
    try:
        await channel.send(message)
        log.info("Boas-vindas enviadas para %s.", member)
    except discord.Forbidden:
        log.exception("Sem permissão para enviar mensagens em #%s.", channel.name)
    except discord.HTTPException:
        log.exception("Falha ao enviar a mensagem de boas-vindas.")


client.run(TOKEN)
