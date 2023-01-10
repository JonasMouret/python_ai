import pyttsx3
import speech_recognition as sr


class AI:
    __name = "AI"
    __version = "1.0.0"
    __skills = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()