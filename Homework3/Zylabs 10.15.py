#Bryan Nguyen
#1855265

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == '__main__':
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team1 = Team()
    team1.team_name = team_name
    team1.team_wins = team_wins
    team1.team_losses = team_losses

    if team1.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team1.team_name, 'has a winning average!')
    else:
        print('Team', team1.team_name, 'has a losing average.')