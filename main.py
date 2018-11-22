#main function
import pyttsx3
from tkinter import *
from TTS import speech



def main():
    count = 0
    sp = speech.Speech(title="speech one",text="Notice all student council members, the student council is having a meeting today at lunch at room 3O1, please wear your shirts.",speaker="Ting-Ting",order=1)
    sps = []
    sps.append(sp)
    engine = pyttsx3.init()

    # functions setup
    def start_notification(name):
        print("start speaking la", name)

    def start_word_notification(name, location, length):
        print("proceeding", name, location, length)

    def finish_utterance_notification(name, completed,count = 0):
        if count >= len(sps):
            print(0)
            engine.say("jasdfasdf","sd")
            count += 1
        else:
            engine.endLoop()

    def on_error_notification(name, exception):
        return exception
    engine = pyttsx3.init()

    for voice in engine.getProperty("voices"):
        if voice.name == "Samantha":
            engine.connect(topic="started-utterance", cb=start_notification)
            engine.connect(topic="started-word", cb=start_word_notification)
            engine.connect(topic="finished-utterance", cb= finish_utterance_notification)
            engine.connect(topic="error", cb=on_error_notification)

            engine.setProperty(name="voice", value=voice.id)
            engine.setProperty(name="rate", value=engine.getProperty(name="rate") - 15)
            engine.setProperty(name="rate", value=engine.getProperty(name="volume") + 0.25)

            engine.say(text=sps[0].getText(),name=sps[0].getText())
            engine.startLoop()




if __name__ == '__main__':
    main()