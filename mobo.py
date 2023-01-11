from ai import AI
import random
from skills.todo import Todo, Item
from skills.weather import Weather
from skills.astronomy import Astronomy
from datetime import datetime


mobo = AI()
todo = Todo()

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


def add_todo() -> bool:
    item = Item()
    mobo.say("Quel est le titre de votre tâche ?")
    try:
        item.title = mobo.listen()
        todo.new_item(item)
        message = f"La tâche {item.title} a bien été ajoutée"
        mobo.say(message)
        return True
    except Exception as e:
        mobo.say("Une erreur est survenue, veuillez réessayer")
        return False


def list_todos():
    if len(todo) > 0:
        mobo.say("Voici vos tâches à faire :")
        for item in todo:
            mobo.say(f"{item.title} - {item.status}")
    else:
        mobo.say("Vous n'avez aucune tâche")


def remove_todo():
    mobo.say("Quel est le titre de la tâche à supprimer ?")
    title = mobo.listen()
    if todo.remove_item(title=title):
        mobo.say(f"La tâche {title} a bien été supprimée")
        return True
    else:
        mobo.say("Aucune tâche ne correspond à ce titre")
        return False

def weather():
    myweather = Weather()
    mobo.say(myweather.forcast)

def astronomy_update():
    mobo.say("Initialisation de la séquance de mise à jour des objets stélaires")
    astronomy = Astronomy()
    mobo.say("Je vous informerais lorsque la mise à jour sera terminée")
    mobo.say(astronomy.update_objects_observation)

command = ""

while command != "au revoir":
    try:
        command = mobo.listen()
        command = command.lower()
    except Exception as e:
        print(e)
        command = ""
    # ============================= COMMANDES ============================= #
    if command in {"blague", "blagues", "raconte une blague", "raconte une blagues", "raconte une blague s'il te plait", "raconte une blagues s'il te plait", "raconte une blague s'il te plait MOBO", "raconte une blagues s'il te plait MOBO", "raconte une blague MOBO", "raconte une blagues MOBO"}:
        blagues()

    if command in {'ajoute une tâche', 'ajouter une tâche'}:
        add_todo()
        command = ""

    if command in {
        'liste des tâches',
        'affiche les tâches',
        'affiche la liste des tâches',
        'liste des tâches à faire',
        'affiche les tâches à faire',
        'affiche la liste des tâches à faire'
    }:
        list_todos()
        command = ""

    if command in {'supprime', 'supprimer', 'supprimer une tâche', 'supprime une tâche'}:
        remove_todo()
        command = ""

    if command in {'météo', 'temps', 'quel temps fait-il', 'quel temps fait il', 'quel temps fait-il MOBO', 'quel temps fait il MOBO'}:
        weather()
        command = ""

    if command in {'bonjour', 'salut', 'bonjour mobo', 'salut mobo', 'bonsoir', 'bonsoir mobo'}:
        now = datetime.now()
        if now.hour < 17:
            mess = "Bonjour Monsieur MOURET comment allez vous ?"
        else:
            mess = "Bonsoir Monsieur MOURET comment allez vous ?"

        message = f'Bien le {mess}'
        mobo.say(message)
        list_todos()
        weather()
    
    if command in {
        'mise à jour',
        'mise à jour des objets stellaires',
        'mise à jour des objets stellaires MOBO',
    }:
        astronomy_update()
        command = ""


mobo.say("Mise en veille De MOBO, au revoir Monsieur MOURET")
