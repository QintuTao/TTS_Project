# the speech module defined the data of user input
# the single speech class

class Speech:
    speakers = ["Alex","Ting-Ting","Samantha"]
    def __init__(self,title:str,text:str,order:int,speaker:str):
        self._title = title
        self._text = text
        self._order = order
        self._speaker = speaker if speaker in self.speakers else "Samantha"

    def __str__(self):
        return f"The title of the speech is \"{self._title}\""



    # getters
    def getTitle(self):
        return self._title

    def getText(self):
        return self._text

    def getOrder(self):
        return self._order

    def getSpeaker(self):
        return self.speaker

    #setters
    def setTitle(self,t):
        self._title = t

    def setText(self,t):
        self._text = t

    def setOrder(self,l):
        self._order = l




    def changeSpeakerTo(self,speaker:str):
        if speaker not in self.speakers:
            self.speaker = "Samantha"
            raise NameError(f"The name {speaker} is not in the speakers list")
        else:
            self.speaker = speaker

        #make it multiple speaker


#testing
if __name__ == "__main__":
    sp1 = Speech("q1","apple",1,"Alex;")
    sp2 = Speech("q2","banana",2,"Alex")
    sp3 = Speech("q3","chips",3,"Ting-Ting")
    sp3.changeSpeakerTo("Ting-Ting")
    print(sp3.getSpeaker())
    exit(Speech)