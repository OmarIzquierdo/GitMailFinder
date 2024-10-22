import requests

class GithubApi:
    def __init__(self):
        self.email = ""
        self._base_url = "https://api.github.com"

    def get_email(self, user):
        self.__get_commits(user)
        return self.email

    def __get_repos(self, user):
        url = f"{self._base_url}/users/{user}/repos"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"

    def __get_commits(self, user):
        for repository in self.__get_repos(user):
            commits_url = repository['commits_url'][:-6]
            response = requests.get(commits_url)

            if response.status_code == 200:
                commits = response.json()
                self.email = self.__get_email_from_commit(commits)
                if self.email:
                    break
            else:
                return f"Error: {response.status_code}"

    def __get_email_from_commit(self, commits):
        for commit in commits:
            self.email = commit['commit']['author']['email']
            if self.email:
                return self.email

        return "Email couldn't be found"