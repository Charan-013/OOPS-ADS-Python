from functools import cmp_to_key
class Team:
    def __init__(self,TeamName,wins,losses,draws,noResult,points):
        self.TeamName = TeamName
        self.wins = int(wins)
        self.losses = int(losses)
        self.draws = int(draws)
        self.noResult = int(noResult)
        self.points = int(points)

    

    def __str__(self):
        return f"{self.TeamName}: Points={self.points}, Wins={self.wins}, Losses={self.losses}, Draws={self.draws}, NoResult={self.noResult}"
    
def compare(team1, team2):
    if team1.points < team2.points:
        return 1
    elif team1.points > team2.points:
        return -1
    
    if team1.wins < team2.wins:
        return 1
    elif team1.wins > team2.wins:
        return -1
    
    if team1.losses > team2.losses:
        return 1
    elif team1.losses < team2.losses:
        return -1
    
    if team1.draws < team2.draws:
        return 1
    elif team1.draws > team2.draws:
        return -1
    
    if team1.noResult > team2.noResult:
        return 1
    elif team1.noResult < team2.noResult:
        return -1
    
    if team1.TeamName > team2.TeamName:
        return 1
    elif team1.TeamName < team2.TeamName:
        return -1
    
    return 0

def main():
    teamList = []

    try:
        while True:
            inp = input()

            if not inp:
                break
            
            values = inp.split(",")
            team = Team(*values)
            teamList.append(team)


    except EOFError:
        pass

    teamList = sorted(teamList,key=cmp_to_key(compare))
    print("Sorted Leaderboard:")
    for ele in teamList:
        print(ele)

main()