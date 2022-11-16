import requests

def slack_post_test(post_title,post_text):
  TOKEN_a = '4159801049456'; TOKEN_b = '4295338328721'; TOKEN_c = 'bgMCh6xnOGTMrSUjw9Y14NFG'
  CHANNEL = 'bot-space'
  TOKEN = 'xoxb-'+ TOKEN_a + '-' + TOKEN_b + '-' + TOKEN_c
  
  url = "https://slack.com/api/chat.postMessage"
  headers = {"Authorization": "Bearer "+TOKEN}
  data  = {
    'channel': CHANNEL,
    'text': str(post_title) + ":" + str(post_text),
  }
  r = requests.post(url, headers=headers, data=data)
  print(r)
  return r

def slack_post_water_temp(RaspberryPi_Name,celsius,fahrenheit):
  TOKEN_a = '4159801049456'; TOKEN_b = '4295338328721'; TOKEN_c = 'bgMCh6xnOGTMrSUjw9Y14NFG'
  CHANNEL = 'bot-space'
  TOKEN = 'xoxb-'+ TOKEN_a + '-' + TOKEN_b + '-' + TOKEN_c
  
  url = "https://slack.com/api/chat.postMessage"
  headers = {"Authorization": "Bearer "+TOKEN}
  data  = {
    'channel': CHANNEL,
    'text': "ラズパイ名：" + str(RaspberryPi_Name) + "\n" + "摂氏温度：" + str(celsius) + "°C" + "\n" + "華氏温度：" + str(fahrenheit) + "°F",
  }
  r = requests.post(url, headers=headers, data=data)
  print(r)
  return r

def slack_post_water_high(RaspberryPi_Name,high):
  TOKEN_a = '4159801049456'; TOKEN_b = '4295338328721'; TOKEN_c = 'bgMCh6xnOGTMrSUjw9Y14NFG'
  CHANNEL = 'bot-space'
  TOKEN = 'xoxb-'+ TOKEN_a + '-' + TOKEN_b + '-' + TOKEN_c
  
  url = "https://slack.com/api/chat.postMessage"
  headers = {"Authorization": "Bearer "+TOKEN}
  data  = {
    'channel': CHANNEL,
    'text': "ラズパイ名：" + str(RaspberryPi_Name) + "\n" + "水位：" + str(high) + "%",
  }
  r = requests.post(url, headers=headers, data=data)
  print(r)
  return r
