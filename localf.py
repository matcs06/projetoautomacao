import sys
import os
from dotenv import load_dotenv

load_dotenv()
print("\n Criando pasta local \n")

foldername = str(sys.argv[1])
path = os.getenv("FILEPATH")
username = str(os.getenv("GITHUBUSERNAME"))
_dir = path + '/' + foldername

print(_dir)
def create_local_folder():
  try:
    os.mkdir(_dir)
    os.chdir(_dir)
    os.system('git init')
    os.system(f'git remote add origin git@github.com:{username}/{foldername}.git')
    os.system(f'echo "# {foldername}" >> README.md')
    os.system('git add .')
    os.system('git commit -m "Initial commit"')
    os.system('git push -u origin master')

    print(f'{foldername} criado localmente e linkado remotamento ao repositório no Github')
    os.system('code .')
  except:
    print("create <project_name> remote")

if __name__ == '__main__':
  create_local_folder()