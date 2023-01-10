import pyttsx3
import speech_recognition as sr


class AI:
    __name = "AI"
    __skills = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        name = voices[0].name
        print(name)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

        self.engine.say('Bonjour. Bienvenue Monsieur MOURET, Initialisation de la reconnaissance vocale complète.')
        self.engine.runAndWait()
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        sentense = f"Je m'appelle désormais {value}"
        self.__name = value
        self.engine.say(sentense)
        self.engine.runAndWait()

    def say(self, sentense):
        self.engine.say(sentense)
        self.engine.runAndWait()

    def listen(self):
        print("Je vous écoute")
        # self.engine.say("Je vous écoute")
        # self.engine.runAndWait()
        with self.m as source:
            audio = self.r.listen(source)
        print("Bien reçu")

        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="fr_fr")
            sentence = f'Vous avez dit : {phrase}'
            print(f"Vous avez dit : {phrase}")
            self.engine.say(sentence)
            self.engine.runAndWait()
        except Exception as e:
            self.engine.say("Je n'ai pas compris")
            self.engine.runAndWait()
            phrase = ""


        print("Vous avez dit : ",  phrase)
        return phrase