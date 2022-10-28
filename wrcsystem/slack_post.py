import requests

def slack_post(post_text):
  TOKEN_a = '4159801049456'; TOKEN_b = '4295338328721'; TOKEN_c = 'bgMCh6xnOGTMrSUjw9Y14NFG'
  CHANNEL = 'bot-space'
  TOKEN = 'xoxb-'+ TOKEN_a + '-' + TOKEN_b + '-' + TOKEN_c
  
  url = "https://slack.com/api/chat.postMessage"
  headers = {"Authorization": "Bearer "+TOKEN}
  data  = {
    'channel': CHANNEL,
    'text': post_text,
  }
  r = requests.post(url, headers=headers, data=data)
  print(r)
  return r

