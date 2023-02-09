import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '5516582835',
  'message': 'aaa',
  'key': 'textbelt',
})
print(resp.json())