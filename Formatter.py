import pandas as pd
from tabulate import tabulate

class Formatter:

    def show_table(self, json_commits):
        names, emails, commit_hashes, url_commits = [], [], [], []

        for commit in json_commits:
            try:
                email = commit['commit']['author']['email']
                name = commit['commit']['author']['name']
                commit_hash = commit['sha']
                url_commit = commit['url']

                if email and email not in emails and name not in names:
                    emails.append(email)
                    names.append(name) if name else names.append("unknown name")
                    commit_hashes.append(commit_hash)
                    url_commits.append(url_commit.replace("api.github.com/repos", "github.com").replace("/commits/", "/commit/"))
            except:
                pass

        data = {
            'emails': emails,
            'names': names,
            'commit_hashes': commit_hashes,
            'url_commit':   url_commits
        }

        table = pd.DataFrame(data)

        print(tabulate(table, headers='keys', tablefmt='grid', showindex=False))