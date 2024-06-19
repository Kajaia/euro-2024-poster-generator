import requests

match_id = input('Match ID: ')
response = requests.post('http://127.0.0.1:5000/generate_poster', json={'match_id': match_id})

if response.status_code == 200:
    print('Poster generated successfully:', response.json()['result'])
else:
    print('Error:', response.json()['error'])
