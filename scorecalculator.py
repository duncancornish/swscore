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
    print("Player "+str(players[p].pnum)+":")
    cogs=input("How many cogs? ")
    compasses=input("How many compasses? ")
    tablets=input("How many tablets? ")
    score=calculateScience(int(cogs), int(compasses), int(tablets))
    score+=int(input("How many points from blue cards? "))
    score+=int(input("How many points from military victories? "))
    score-=int(input("How many military defeats? "))
    money=float(input("How much leftover gold? "))
    score+=int(money/3)
    score+=int(input("How many points from the wonder? "))
    score+=int(input("How many points from the guilds? "))
    score+=int(input("How many points from yellow cards? "))
    players[p].score=score
print("Final scores:")
for p in players:
    print("Player "+str(players[p].pnum)+" had a score of "+str(players[p].score))
