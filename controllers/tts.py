import pyttsx3


class Tts:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voice_id = 53
        self.get_voice()

    def get_voice(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[self.voice_id].id)

    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == '__main__':
    Tts().speak("Testando a voz do assistente virtual")
