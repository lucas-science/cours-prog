"""import discord

client = discord.Client()


@client.event
async def on_ready():
    print("le bot est en marche")


@client.event
async def on_message(message):
    if message.content.lower() == "paul":
        await message.channel.send("paul est gay")
    if 'quoi' in message.content:
        lis = list(message.content.split(" "))
        if lis[-1] == "quoi":
            await message.channel.send("feur :upside_down::upside_down_face:")
    elif 'naifen' in message.content:
        await message.channel.send("*Nathan")
    elif message.content.lower() == "paul est t il gay ?":
        await message.channel.send("oui il est gay et il se fait booster")

    elif message.content.lower() == "def of louis":
        await message.channel.send("louis est une personne qui affirmait vouloir creer une bible pour montrer le droit chemin aux autres personnes perdu, cependant je n'ai tjr pas vu de bible.pdf arriver dans le channel depuis l'annonce de cette oeuvre ayant pour but de boulverser les plus grands esprits."+'\n'+"Louis aurait il besoin d'un rappel ? @Louis#9086")

client.run("ODg2NjQ4ODQ0MTU3MzMzNTg2.YT4qFQ.iMBP6ca1BV-nmhu7rN-8o7Mvou4")"""


def fact(N):
    if N <= 1:
        return 1
    else:
        return N*fact(N-1)


def fact_iter(N):
    x = 1
    for i in range(N):
        x = x*(N-i)
    return x

print(fact(5))
print(fact_iter(5))