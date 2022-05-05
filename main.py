import tweepy
import json


text = ''
turn = 'x'


# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler('plBbHFBVp2CnGVT8vWM3DNup2', 'R2drRU7IUxKBjnZsvPtiVBkNm5DO7FBZclwHGnJDTzvOPN5dfz', access_token='1488876360705654794-e6BW9ypcmHBXOf1h5KI1HipeC1FKvb', access_token_secret='dacLACy1o4cNAYXXPdJGpIlNytl5QOpY3Kb1tNKPFHYsz')
auth.set_access_token('1488876360705654794-e6BW9ypcmHBXOf1h5KI1HipeC1FKvb', 'dacLACy1o4cNAYXXPdJGpIlNytl5QOpY3Kb1tNKPFHYsz')
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAANFGYwEAAAAAuf4iuc36ULEKbKlUT3z07RO245E%3DHaabvLcYQEwVZlOJI3HSUqpOhGzksDz4AAYgefPUfPsKbRAgHA', consumer_key='plBbHFBVp2CnGVT8vWM3DNup2', consumer_secret='R2drRU7IUxKBjnZsvPtiVBkNm5DO7FBZclwHGnJDTzvOPN5dfz', access_token='1488876360705654794-e6BW9ypcmHBXOf1h5KI1HipeC1FKvb', access_token_secret='dacLACy1o4cNAYXXPdJGpIlNytl5QOpY3Kb1tNKPFHYsz')

api = tweepy.API(auth)


api.verify_credentials()

def get_last_tweet_likes():
  try:
    tweet = api.user_timeline(user_id = 'BotsCrosses', count = 1)[0]
    likes = client.get_liking_users(id=tweet.id)
  except IndexError:
    return 0
  return likes.meta['result_count']

def get_last_tweet_rts():
  try:
    tweet = api.user_timeline(user_id = 'BotsCrosses', count = 1)[0]
    rts = client.get_retweeters(id=tweet.id)
  except IndexError:
    return 0
  return rts.meta['result_count']


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
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.value = unicode['black']
    def x(self):
        self.value = unicode['blue']
    def o(self):
        self.value = unicode['yellow']

cells = [
    [cell(0, 0, 0), cell(1, 0, 1), cell(1, 0, 2)],
    [cell(0, 1, 3), cell(1, 1, 4), cell(2, 1, 5)],
    [cell(0, 2, 6), cell(1, 2, 7), cell(2, 2, 8)]
]

board = [
    [cells[0][0].value, cells[0][1].value, cells[0][2].value],
    [cells[1][0].value, cells[1][1].value, cells[1][2].value],
    [cells[2][0].value, cells[2][1].value, cells[2][2].value],
]

def refresh():
    board = [
    [cells[0][0].value, cells[0][1].value, cells[0][2].value],
    [cells[1][0].value, cells[1][1].value, cells[1][2].value],
    [cells[2][0].value, cells[2][1].value, cells[2][2].value],
]

def wait(minutes):
    import time
    time.sleep(minutes * 60)

def get_loc():
    x = False
    y = False
    if get_last_tweet_likes() != 0: 
      y = get_last_tweet_likes() % 3
    if get_last_tweet_rts() != 0: 
      x = get_last_tweet_rts() % 3
    return [x, y]

def set_cells():
  print('a')
  x = get_loc()[0]
  y = get_loc()[1]
  if turn == 'x' and x and y:
    cells[y][x].value = unicode['yellow']
  print(['debug', x, y, cells[y][x].value])
  

def send():
  
    
    
    box = ''
    report = ''
    
    for row in cells:
        for col in row:
            box += col.value
        box += '\n'
    with open('stats.json', 'r') as fr:
        fr = fr.read()
        data = json.loads(fr)
        data['rounds'] += 1
    with open('stats.json', 'w') as fw:
        fw.write(json.dumps(data))

    # if (get_last_tweet_likes() != 0 and get_last_tweet_rts() != 0) and (data['rounds'] != 0):
    set_cells()
    refresh()
    if (get_last_tweet_likes() == 0 and get_last_tweet_rts() == 0) and (data['rounds'] != 0):
      report = 'No Input, Restarting round!\n'
    
    text = (
    f'Bots & Crosses\n'
    f'Rounds: {data["rounds"]}\n'
    f'Turn: {turn}\n'
    f'{report}'
    f'{box}'
    )
    print(text)
    api.update_status(text)
    for i in cells:
      for j in i:
        print([j, j.value])
    

while True:
    send()
    input()

print(get_last_tweet_rts())
print(get_last_tweet_likes())