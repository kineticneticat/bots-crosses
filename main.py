import tweepy
import json

turn = 'x'
report = ''
loop = input('loop?<y/n>')


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


def log(state, likes, rts):
  data = {
    'state': state,
    'likes': likes,
    'rts': rts,
  }
  print(json.loads(data))

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
  global turn, report
  x = get_loc()[0]
  y = get_loc()[1]
  if turn == 'x' and (x or y) and cells[y][x].value == unicode['black']:
    cells[y][x].value = unicode['yellow']
    turn = 'o'
  elif turn == 'o' and (x or y) and cells[y][x].value == unicode['black']:
    cells[x][y].value = unicode['purple']
    turn = 'x'
  elif cells[y][x].value != unicode['black']:
    report = 'Overwrite, Restarting Round!\n'
  print(['debug', x, y, cells[y][x].value], 're: '+report)
  

def send():
  
    
    
    box = ''
    global report
    
    #get round num
    with open('stats.json', 'r') as fr:
        fr = fr.read()
        data = json.loads(fr)
    
    #check for "things"
    data['rounds'] += 1
    if (get_last_tweet_likes() == 0 and get_last_tweet_rts() == 0) and (data['rounds'] != 0):
      report = 'No Input, Restarting round!\n'
    if not report: 
      set_cells()
    
    with open('stats.json', 'w') as fw:
        fw.write(json.dumps(data))
    #create the box
    for row in cells:
        for col in row:
            box += col.value
        box += '\n'
    # format text
    text = (
    f'Bots & Crosses\n'
    f'Rounds: {data["rounds"]}\n'
    f'Turn: {turn}\n'
    f'{report}'
    f'{box}'
    )
    print(text)
    for i in cells:
      for j in i:
        print([j, j.value])
    print('report: '+report)
    print('likes: '+str(get_last_tweet_likes()))
    print('rts: '+str(get_last_tweet_rts()))
    print([get_last_tweet_likes()%3, get_last_tweet_rts()%3])
    api.update_status(text)
    

while True:
  send()
  if loop == 'y':
    wait(10*60)
  else:
    input('go: ')