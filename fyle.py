import requests
import json
from transformers import pipeline

# Set up BERT sentiment analysis pipeline
sentiment_classifier = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Define list of football matches to search for
matches = ['Liverpool vs Manchester United', 'Barcelona vs Real Madrid', 'Bayern Munich vs Borussia Dortmund']

# Loop through each match and retrieve the latest result
for match in matches:
    # Build query string for football results API request
    query_string = f'https://api.football-data.org/v2/matches?matchday=1&status=FINISHED&match={match}'

    # Send football results API request and parse response
    response = requests.get(query_string, headers={'X-Auth-Token': 'YOUR_API_KEY'})
    data = json.loads(response.text)
    matches = data['matches'][:1]

    # Loop through each match and perform sentiment analysis on the result
    for match in matches:
        # Extract match details
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        home_score = match['score']['fullTime']['homeTeam']
        away_score = match['score']['fullTime']['awayTeam']

        # Perform sentiment analysis on match result
        text = f'{home_team} {home_score} - {away_score} {away_team}'
        sentiment = sentiment_classifier(text)[0]['label']

        # Print results
        print(f'{match}: {sentiment}')
