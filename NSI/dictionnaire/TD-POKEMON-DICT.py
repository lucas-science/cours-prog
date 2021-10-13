import random
import keyboard

Carapuce = {
    "nom":"carapuce",
    "HP":100,
    "Puissance_attaque":80,
    "Viesse_combat":15,
    "type":"eau",
    "Efficacité_defense":"30"
}
Evoli = {
    "nom":"evoli",
    "HP":90,
    "Puissance_attaque":60,
    "Viesse_combat":25,
    "type":"normal",
    "Efficacité_defense":20
}

for i in range(10):
    print(random.random())

def Calcul_Defense_Attaque(poke1:dict,poke2:dict):
    poke1["attaque"] = poke1["Puissance_attaque"]*random.random()
    poke2["attaque"] = poke2["Puissance_attaque"]*random.random()

    poke1["defense"] = poke1["Efficacité_defense"]*random.random()
    poke2["defense"] = poke2["Efficacité_defense"]*random.random()





Calcul_Defense_Attaque(Carapuce,Evoli)

i = 0

def combat(poke1,poke2):
    i = 0
    while poke1["HP"]> 9 and poke2["HP"]>9:
        inp = input("click espace bar and enter to continue : ")
        while inp != " ":
            inp = input("click espace bar and enter to continue : ")
        i+=1
