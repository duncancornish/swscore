#Blue Cards
#Warmongering - Victories and Defeats
#Money
#Wonder
#Guilds
#Science
#Yellow Cards
#Other
class Player:
    def __init__(self, pnum):
        self.pnum=pnum
        self.score=0

    def show(self):
        print("Player "+str(self.pnum)+" has a score of "+str(self.score)+".")

def calculateScience(cogs, compasses, tablets):
    score=cogs**2
    score+=compasses**2
    score+=tablets**2
    lowest=min(cogs, compasses, tablets)
    score+=lowest*7
    return score

players={}
pcount=input("How many players? ")
for p in range(int(pcount)):
    players[p]=Player(p+1)

for p in players:
    players[p].show()
