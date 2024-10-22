import requests

class GithubApi:
    def __init__(self):
        self._base_url = "https://api.github.com"

    def get_all_commits_from_all_repositories(self, user):
        url = f"{self._base_url}/users/{user}/repos"
        response = requests.get(url)

        if response.status_code == 200:
            repositories = response.json()
        elif response.status_code == 403:
            yield f"Error: Rate limit reached (403)"
            return
        else:
            yield f"Error: {response.status_code}"
            return

        for repository in repositories:
            commits_url = repository['commits_url'][:-6]
            response = requests.get(commits_url)

            if response.status_code == 200:
                for commit in response.json():
                    yield commit
            elif response.status_code == 403:
                yield f"Error: Rate limit reached (403)"
                return
            else:
                yield f"Error: {response.status_code}"
                return