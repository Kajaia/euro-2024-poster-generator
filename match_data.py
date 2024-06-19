from image_generate import generate_match_image
import requests

def get_match_data(match_id):
    try:
        res = requests.get(f"https://prosoccer.tv/api/fixtures?t=info&id={match_id}")
        res.raise_for_status()
        
        data = res.json()
        match = data.get('data')
        
        if match is None:
            return 'No match data found.'

        home_team = match['teams']['home']['name']
        away_team = match['teams']['away']['name']
        home_logo_url = match['teams']['home']['img']
        away_logo_url = match['teams']['away']['img']

        generate_match_image(home_team, away_team, home_logo_url, away_logo_url)
    except Exception as e:
        return f'An unexpected error occurred: {e}'