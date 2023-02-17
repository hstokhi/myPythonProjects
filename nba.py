from requests import get

url = 'https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json'

data = get(url).json()
date = data['scoreboard']['gameDate']
print(date, '\n')
games = data['scoreboard']['games']


def scoreboard(games):
    for game in games:
        clock = game['gameStatusText']
        hcity = game['homeTeam']['teamCity']
        hteam = game['homeTeam']['teamName']
        hscore = game['homeTeam']['score']
        acity = game['awayTeam']['teamCity']
        ateam = game['awayTeam']['teamName']
        ascore = game['awayTeam']['score']
        print(hcity, hteam, 'vs', acity, ateam)
        print(clock)
        print('Score:', hscore, 'to', ascore)
        print('\n')

def leadingScorer(games):
    for game in games:
        hteam = game['gameLeaders']['homeLeaders']['teamTricode']
        hscorer = game['gameLeaders']['homeLeaders']['name']
        hpoints = game['gameLeaders']['homeLeaders']['points']
        ateam = game['gameLeaders']['awayLeaders']['teamTricode']
        ascorer = game['gameLeaders']['awayLeaders']['name']
        apoints = game['gameLeaders']['awayLeaders']['points']
        
        print(hteam, hscorer, 'Points:', hpoints)
        print(ateam, ascorer, 'Points:', apoints)
        print('\n')

scoreboard(games)
print('--------------------------------------------------------\n')
leadingScorer(games)


        

