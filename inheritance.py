class Dad:
    def __init__(self,color,dadhobby):
        self.color=color
        self.dadhobby=dadhobby
class Mum:
    def __init__(self,color,mumhobby):
        self.color=color
        self.mumhobby=mumhobby
class Boy(Dad):
    def boyinherits(self):
        print(f"Boy inherits  {self.color} and the {self.dadhobby}")
   # instance
myobj=Boy("african decent","watching football")
myobj.boyinherits()

class Girl(Mum):
    def girlinherits(self):
        print(f"Girl inherits {self.mumhobby} and the {self.color}")
myobj=Girl("African decent","singing")
myobj.girlinherits()

