import requests


def get_events(user):
    url_github = f"https://api.github.com/users/{user}/events"
    response = requests.get(url_github)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
    

def get_issues(user, repo_name):
    url_github = f"https://api.github.com/repos/{user}/{repo_name}/issues/events"
    response = requests.get(url_github)

    
    if response.status_code == 200:
        data = response.json()
        return data