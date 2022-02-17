from nextcord.ext import commands
import nextcord
import os

client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())


def main():
    for cog in os.listdir("./commands"):
        if cog.endswith('.py'):
            print(f"Załadowano {cog}")
            client.load_extension(f"commands.{cog[:-3]}")

    for cog_e in os.listdir("./events"):
        if cog_e.endswith('.py'):
            print(f"Załadowano {cog_e}")
            client.load_extension(f"events.{cog_e[:-3]}")

    client.run("")


if __name__ == "__main__":
    main()
