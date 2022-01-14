import random
import requests
import pandas as pd
import json

Carapuce = {
    "nom":"carapuce",
    "HP":100,
    "Puissance_attaque":80,
    "Vitesse_combat":15,
    "type":"eau",
    "Efficacité_defense":30
}
Evoli = {
    "nom":"evoli",
    "HP":90,
    "Puissance_attaque":60,
    "Vitesse_combat":25,
    "type":"normal",
    "Efficacité_defense":20
}

#------------JEU------------

def Calcul_Defense_Attaque(poke1:dict,poke2:dict):
    """
    caclule le point de defense et d'attque pour les 2 pokemon
    """
    poke1["attaque"] = poke1["Puissance_attaque"]*random.random()
    poke2["attaque"] = poke2["Puissance_attaque"]*random.random()

    poke1["defense"] = poke1["Efficacité_defense"]*random.random()
    poke2["defense"] = poke2["Efficacité_defense"]*random.random()
    return [poke1,poke2]
    

def Plus_Rapide(poke1:dict,poke2:dict):
    """
    designe le premier pokemon qui commence sauf dans 20 % des cas ça s'inverse
    """
    alea = random.random()
    if alea > 0.2: #20% des cas où c'est le contraire
        if poke1["Vitesse_combat"] > poke2["Vitesse_combat"]:
            return [poke1,poke2]
        else:
            return [poke2,poke1]
    else:
        if poke1["Vitesse_combat"] > poke2["Vitesse_combat"]:
            return [poke2,poke1]
        else:
            return [poke1,poke2]

def attaque_defense(attaquant:dict,defenseur:dict):
    """
    gestion des degats affligé et verif si Pokemon K.O. ou non.
    """
    initialHP = defenseur["HP"]
    defenseur["HP"] -= attaquant["attaque"]
    defenseur["HP"] += defenseur["defense"]
    if defenseur["HP"] > initialHP:
        defenseur["HP"] = initialHP
        print(f'defenseur : {attaquant["nom"]} \n Il a encore {defenseur["HP"]} HP')
        return [False,""]
    if defenseur["HP"] <= 9:
        print(f'defenseur : {attaquant["nom"]} \n Il est K.O.')
        return [True,f'{defenseur["nom"]}']
    else: 
        print(f'defenseur : {attaquant["nom"]} \n Il a encore {defenseur["HP"]} HP')
        return [False,""]


def combat(poke1:dict,poke2:dict):
    a = {}
    ordre_poke = Plus_Rapide(poke1,poke2)
    print("-------------------------Le COMBAT COMMENCE-------------------------")
    print(f'l ordre de passagge est : {ordre_poke[0]["nom"]} et {ordre_poke[1]["nom"]}')
    stop = [False,""]
    while stop[0] == False:
        inp = input("click espace bar and enter to continue : ")
        while inp != " ":
            inp = input("click espace bar and enter to continue : ")
        stop = attaque_defense(ordre_poke[0],ordre_poke[1])
        a = ordre_poke[1]
        ordre_poke[1] = ordre_poke[0]
        ordre_poke[0] = a

    print(f'\n{stop[1]} est mort face à {ordre_poke[1]["nom"]} \nQuand à lui {ordre_poke[1]["nom"]} à encore {ordre_poke[1]["HP"]} !')


# ---------POKEDEX----------
def creerPokemonStat(pokeChoose:list):
    """
    Cherche les stats des pokemons
    return : les deux dict composer des stats des pokemons
    """
    poke = {}
    Pokemons = []
    for i in range(len(pokeChoose)):
        r2 = requests.get(pokeChoose[i]['url'])
        result_pokemon_stats = r2.content
        result_pokemon_stats_dict = json.loads(result_pokemon_stats)
        statPokemon = result_pokemon_stats_dict["stats"]
        for x in statPokemon:
            poke[x["stat"]["name"]] = x["base_stat"]
        poke["name"] = pokeChoose[i]["name"]
        Pokemons.append(poke)
        poke = {}
    return Pokemons

def CleanData(Pokemons):
    """
    formate les donné de l'api pour etre comptatible avec les fonctions "JEU"
    return : les dict des deux pokemons
    """
    newpoke1 = {
        "nom":Pokemons[0]["name"],
        "HP":Pokemons[0]["hp"],
        "Puissance_attaque":Pokemons[0]["special-attack"],
        "Vitesse_combat":Pokemons[0]["speed"],
        "Efficacité_defense":Pokemons[0]["special-defense"]
    }
    newpoke2 = {
        "nom":Pokemons[1]["name"],
        "HP":Pokemons[1]["hp"],
        "Puissance_attaque":Pokemons[1]["special-attack"],
        "Vitesse_combat":Pokemons[1]["speed"],
        "Efficacité_defense":Pokemons[1]["special-defense"]
    }
    return [newpoke1,newpoke2]

def choose_pokemon():
    """
    Cherche les 151 premiers pokemon, pour que l'utilisateur en choisse 2.
    """
    list_nom_pokemon = []
    list_nom = []

    url_pokemon_choose = []

    url1 = 'https://pokeapi.co/api/v2/pokemon?limit=151'

    r1 = requests.get(url1)
    result_pokemon = r1.content
    result_pokemon_dict = json.loads(result_pokemon)

    for i in range(len(result_pokemon_dict["results"])):
        print(result_pokemon_dict["results"][i]["name"])
        list_nom_pokemon.append([result_pokemon_dict["results"][i]["name"],i])

    chooseByUser1 = input("Choisisez votre premier pokemon présent dans la liste ci dessus : ")
    chooseByUser2 = input("Choisisez votre second pokemon présent dans la liste ci dessus : ")

    for i in result_pokemon_dict["results"]:
        list_nom.append(i["name"])


    if chooseByUser1 in list_nom and chooseByUser2 in list_nom:
        print("les pokemon existe ")
        for i in result_pokemon_dict["results"]: #  cherche l'url pour trouver les stats des 2 pokemons choisi
            if i["name"] == chooseByUser1:
                url_pokemon_choose.append({"name":i["name"], "url":i["url"]})
            if i["name"] == chooseByUser2:
                url_pokemon_choose.append({"name":i["name"], "url":i["url"]}) 

        Pokemon = creerPokemonStat(url_pokemon_choose)
        Pokemon_Clean = CleanData(Pokemon)

        print("-------------------------Les stats des Poke-------------------------")
        print(Pokemon_Clean[0],'\n')
        print(Pokemon_Clean[1])
        print("--------------------------------------------------------------------")
        print('\n')
        Pokemon_finale = Calcul_Defense_Attaque(Pokemon_Clean[0],Pokemon_Clean[1])
        combat(Pokemon_finale[0],Pokemon_finale[1])

    else:
        print("les pokemon existe pas")


choose_pokemon()



#Calcul_Defense_Attaque(Evoli,Carapuce)
#combat(Evoli,Carapuce)


