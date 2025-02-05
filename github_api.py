import requests


def get_events(user):
    url_github = f"https://api.github.com/users/{user}/events"
    response = requests.get(url_github)
    response.raise_for_status()
    return response.json()