'''
I pledge my honor that I have abided by the Stevens Honor System.
@author: Oscar Tavara
'''
import requests
import json

def get_repo(user):
    if (user == ""):
        return "Please provide a username"
    elif (user == []):
        return "A list of repos was not provided"
    elif (not isinstance(user, str)):
        return "The input " + str(user) +" is not valid"
    elif((requests.get("https://api.github.com/users/" + str(user) + "/repos")).json() == []):
        return "The account [" + user +"] does not have any repositories"
    else:
        array = []
        j = json.loads(requests.get('https://api.github.com/users/'+str(user)+'/repos').text)
    
        for i in j:
            try:
                array += [i['name']]
            except:
                print("API RATE LIMIT EXCEEDED")


    return array


def get_num_commits(user, repo_list, repo):
    if(not isinstance(repo_list, list)):
        return "A list of repos was not provided"
    if (user == ""):
        return "Please provide a username"
    if (repo == ""):
        return "Please provide a repo to view"
    try:
        j = json.loads(requests.get('https://api.github.com/repos/'+user+'/'+ repo +'/commits').text)
        commits_num = len(j)
    except:
        print(repo + " not found in " + user +"'s repo")

    return commits_num

def main():
    user = input('GitHub User ID: ')
    print(str(json.loads(requests.get('https://api.github.com/users/'+ user +'/repos').text)['message']))
    r_list = get_repo(user)
    for repo in (r_list):
        print('Repo: '+ repo +' Number of commits: '+ get_num_commits(user, r_list, repo))

if __name__ == '__main__':
    main()