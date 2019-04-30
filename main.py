#main function
import pyttsx3
import time
from TTS import speech

def main():
    count = 0
    sp = speech.Speech(title="speech1",text="Notice all student council members, the student council is having a meeting today at lunch at room 3O1, please wear your shirts.",speaker="Samantha",order=1)
    sps = []
    sp2 = speech.Speech(title="speech2",text="End",order=1,speaker="Samantha ")
    sp3 = speech.Speech(title="speech3",text="  ",order=1,speaker="Samantha ")
    sp2.setTimer(4.00)
    sps.append(sp)
    sps.append(sp2)
    sps.append(sp3)

    engine = pyttsx3.init()
    print(pyttsx3.Engine)

    # functions setup
    def start_notification(name):
        print("start speaking:", name)

    def start_word_notification(name, location, length):
        global L
        L = length
        print("proceeding", name, "at", location,"with length of", length)

    def finish_utterance_notification(name, completed):
        if name == f"speech{count}" and count <= len(sps):
            print(f"finish speaking speech #{count}")
        else:
            engine.endLoop()

    def on_error_notification(name, exception):
        return exception
    engine = pyttsx3.init()

    while count < len(sps):
        for voice in engine.getProperty("voices"):
            if voice.name == "Samantha":
                engine.connect(topic="started-utterance", cb=start_notification)
                engine.connect(topic="started-word", cb=start_word_notification)
                engine.connect(topic="finished-utterance", cb= finish_utterance_notification)
                engine.connect(topic="error", cb=on_error_notification)

                engine.setProperty(name="voice", value=voice.id)
                engine.setProperty(name="rate", value=engine.getProperty(name="rate") - 15)
                engine.setProperty(name="rate", value=engine.getProperty(name="volume") + 0.25)



                engine.say(text=sps[count].getText(),name=sps[count].getTitle())
                engine.startLoop()
        # operate timer
        # if not user specified, use the default value: 1secs
        print(f"Timer operating. The next speech will be delivered in {sps[count].getTimer()} secs!")
        time.sleep(sps[count].getTimer())
        count += 1

if __name__ == '__main__':
    main()
