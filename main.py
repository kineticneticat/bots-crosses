import tweepy
import json


text = ''


# Authenticate to Twitter
auth = tweepy.OAuthHandler("XNuI1ic0dewKKe9HhfWXZGhqz", "ZcQUqfW1gpEGznJAQsYupxvrxp6DWTZhZs8WX6thlCrrfAZ7uR")
auth.set_access_token("1488876360705654794-AcVkOkoMmqEKfZaLrInqTlekGs4ZBj", "CuGpmf2THPyBnPbhLEKU9Tvbj1FrMbz4ULF5K3r6SXWHJ")

api = tweepy.API(auth)
client = tweepy.Client()

api.verify_credentials()



unicode = {
    'black': '⬛',
    'blue': '🟦',
    'brown': '🟫',
    'green': '🟩',
    'orange': '🟧',
    'purple': '🟪',
    'red': '🟥',
    'yellow': '🟨',
}

class cell():
    def __init__(self, x, y, index, value):
        self.x = x
        self.y = y
        self.index = index
        self.value = value

cells = [
    [cell(0, 0, 0, unicode['red']), cell(1, 0, 1, unicode['red']), cell(1, 0, 2, unicode['red'])],
    [cell(0, 1, 3, unicode['red']), cell(1, 1, 4, unicode['red']), cell(2, 1, 5, unicode['red'])],
    [cell(0, 2, 6, unicode['red']), cell(1, 2, 7, unicode['red']), cell(2, 2, 8, unicode['red'])]
]

board = [
    [cells[0][0].value, unicode['black'], cells[0][1].value, unicode['black'],cells[0][2].value],
    [unicode['black'], unicode['black'], unicode['black'], unicode['black'], unicode['black']],
    [cells[1][0].value, unicode['black'], cells[1][1].value, unicode['black'], cells[1][2].value],
    [unicode['black'], unicode['black'], unicode['black'], unicode['black'], unicode['black']],
    [cells[2][0].value, unicode['black'], cells[2][1].value, unicode['black'], cells[2][2].value],
]

def refresh():
    board = [
    [cells[0][0].value, unicode['black'], cells[0][1].value, unicode['black'],cells[0][2].value],
    [unicode['black'], unicode['black'], unicode['black'], unicode['black'], unicode['black']],
    [cells[1][0].value, unicode['black'], cells[1][1].value, unicode['black'], cells[1][2].value],
    [unicode['black'], unicode['black'], unicode['black'], unicode['black'], unicode['black']],
    [cells[2][0].value, unicode['black'], cells[2][1].value, unicode['black'], cells[2][2].value],
]

def wait(minutes):
    import time
    time.sleep(minutes * 60)

def send():
    refresh()
    text = ''
    for row in board:
        for col in row:
            text += col
        text += '\n'
    with open('stats.json', 'r') as fr:
        fr = fr.read()
        data = json.loads(fr)
        data['rounds'] += 1
    with open('stats.json', 'w') as fw:
        fw.write(json.dumps(data))
    
    text += '\n'
    text += 'Rounds: '
    text += str(data['rounds'])
    api.update_status(text)
    print(text)

def get_loc():
    like_dict = 

    return []

while True:
    send()
    wait(10)







