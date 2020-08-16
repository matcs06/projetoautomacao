import sys 
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

print("\nCriando repo no github\n")


path = str(os.getenv("FILEPATH"))
username = str(os.getenv("GITHUBUSERNAME"))
password = str(os.getenv("PASSWORD"))

def create_git_repo():
  folderName = str(sys.argv[1])
  user = Github(username, password).get_user()
  repo = user.create_repo(folderName)
  print(f'Repositório {repo} criado com sucesso')

if __name__ == '__main__':
  create_git_repo()