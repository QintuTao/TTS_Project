# the speech module defined the data of user input
# the single speech class

class Speech:
    def __init__(self,title:str,text:str,order:int,isAlexSpeaking:bool):
        self._title = title
        self._text = text
        self._order = order
        self._isAlexSpeaking = isAlexSpeaking

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
        return self._voiceGender

    #setters
    def setTitle(self,t):
        self._title = t

    def setText(self,t):
        self._text = t

    def setOrder(self,l):
        self._order = l




    def changeSpeaker(self):
        self._isAlexSpeaking = not self._isAlexSpeaking


#testing
if __name__ == "__main__":
    sp1 = Speech("q1","apple",1,True)
    sp2 = Speech("q2","banana",2,False)
    sp3 = Speech("q3","chips",3,False)
    sp3.changeSpeaker()
    print()