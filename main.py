from GithubApi import GithubApi

api = GithubApi()

email = api.get_email("OmarVoxel")
print(email)
