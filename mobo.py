from ai import AI
import pyjokes
import random


mobo = AI()
command = ""

list_blagues = [
    "Qu'est-ce qui est jaune et qui attend ?\nUn bus qui a raté son arrêt.",
    "Combien de développeurs faut-t-il pour remplacer une ampoule grillée ?\nAucun, c'est un problème de hardware.",
    "Comment un développeur tente-t-il de réparer sa voiture lorsqu'elle a un problème ?Il sort de la voiture, ferme toutes les fenêtres, retourne dans la voiture, et essaie de redémarrer.",
    "Quel est le point commun entre un développeur et un ordinateur ?\nIls ont tous les deux une mémoire de 1 Go.",
    "Un physicien, un mathématicien, et un développeur vérifient l'assertion Tous les nombres impairs sont premiers :- Le physicien : 1, 3, 5, 7, 9... heu... 11, 13... bon, aux erreurs expérimentales près, c'est bon - Le mathématicien : 1 c'est bon, 3 c'est bon, 5 c'est bon, 7 c'est bon, 9 c'est pas bon. Je suis désolé, mais ca ne va pas. - Le développeur commence alors : 1 c'est bon, 3 c'est bon, 5 c'est bon, 7 c'est bon, 9 c'est pas bon, 9 c'est pas bon, 9 c'est pas bon, 9 c'est pas bon, 9 c'est pas bon, 9 c'est pas bon ...",
    "Une requête TCP entre dans un bar et dit :- Je veux une bière - Vous voulez une bière ? - Oui, je veux une bière - Très bien"
]

def blagues():
    blague = random.choice(list_blagues)
    print(blague)
    mobo.say(blague)
    

while True and command != "au revoir":
    command = mobo.listen()
    print("cammande reçue : ", command)

    if command == "blague":
        blagues()

mobo.say("Mise en veille De MOBO, au revoir Monsieur MOURET")