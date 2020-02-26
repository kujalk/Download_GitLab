#Purpose - To download all repo files from GitLab
#Requirement - Access Token must be created in GitLab console
#Developer - K.Janarthanan
#Date - 25/2/2020


import json
import requests

token_id=input("Please provide your Private Token : ")
server=input("Please provide your GitLab URL [http://<server IP>:<port>] : ")

url=server+"//api/v4/projects?private_token="+token_id+"&per_page=50"

response=requests.get(url=url,verify=False)

data=response.json()

print("Total Repos : ",len(data))

for i in range(len(data)):
    print ("\nRepo ID : ",data[i]['id'])
    print ("Repo ID : ",data[i]['name'])

    download_url=server+"//api/v4/projects/"+str(data[i]['id'])+"/repository/archive.zip?private_token="+token_id

    download_repo=requests.get(url=download_url,verify=False)

    path="E:\All_Source_Codes\\"+data[i]['name']+".zip"
    with open(path, 'wb') as s:
        s.write(download_repo.content)
