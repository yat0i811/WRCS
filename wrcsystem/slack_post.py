import requests

def slack_post(post_text):
  TOKEN = 'xoxb-4159801049456-4295338328721-1XmmFo7PyPg2zz4ppRLfYC3j'
  CHANNEL = 'bot-space'
  
  url = "https://slack.com/api/chat.postMessage"
  headers = {"Authorization": "Bearer "+TOKEN}
  data  = {
    'channel': CHANNEL,
    'text': post_text,
  }
  r = requests.post(url, headers=headers, data=data)
  print(r)
  return r

