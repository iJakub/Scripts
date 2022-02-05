import requests

username = input("Github Username: ")
reponame = input("Repository Name: ")

request = requests.get(f'https://api.github.com/repos/{username}/{reponame}')
repository_size = request.json().get('size')
print(repository_size) #in KB
