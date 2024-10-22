from api.Formatter import Formatter
from api.Github import GithubApi
import argparse
import sys
from halo import Halo
from colorama import Fore, Style

def print_logo():
    logo = """                                                                                      
          ____ _ _   __  __       _ _    _____ _           _           
         / ___(_) |_|  \/  | __ _(_) |  |  ___(_)_ __   __| | ___ _ __ 
        | |  _| | __| |\/| |/ _` | | |  | |_  | | '_ \ / _` |/ _ \ '__|
        | |_| | | |_| |  | | (_| | | |  |  _| | | | | | (_| |  __/ |   
         \____|_|\__|_|  |_|\__,_|_|_|  |_|   |_|_| |_|\__,_|\___|_|
           """

    lines = logo.splitlines()
    for line in lines[:-4]:
        print(line)
    for line in lines[-4:]:
        print(Fore.RED + line)

    print(Fore.RED + "[+] Author: " + Fore.LIGHTWHITE_EX + "Omar Izquierdo")
    print(Fore.RED + "[+] Blog: " + Fore.LIGHTWHITE_EX + "https://omarizquierdo.dev/ \n")


def get_github_data(username):
    spinner = Halo(text=Fore.LIGHTGREEN_EX + "Fetching data for GitHub user: " + Fore.WHITE + f"{username}", spinner='dots')
    spinner.start()

    api = GithubApi()
    formatter = Formatter()
    commits = api.get_all_commits_from_all_repositories(username)
    result = []

    for commit in commits:
        if isinstance(commit, str) and "Rate limit" in commit:
            print("\n You have reached the limit of requests. Please try again later.")
            break
        result.append(commit)

    if result:
        formatter.show_table(result)

    spinner.stop()

def main():
    parser = argparse.ArgumentParser(description='Find Github Emails')
    parser.add_argument('-u', '--username', help='GitHub username', required=True)
    args = parser.parse_args()

    if not args.username:
        parser.print_help()
        sys.exit(1)

    print_logo()
    get_github_data(args.username)

if __name__ == "__main__":
    main()