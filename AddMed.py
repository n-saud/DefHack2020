import json
import requests

drug = input()
information = requests.get("https://api.fda.gov/drug/label.json?search=" + drug)
info = json.loads(information.content)
file = open("symp.txt","r")
lines = file.readlines()
re = []

if info["results"][0].get("stop_use"):
    for pmatch in lines:
        if pmatch.strip().lower() in info["results"][0].get("stop_use")[0].lower():
            re.append(pmatch.strip())
    print(re)
else:
    for pmatch in lines:
        if pmatch.strip().lower() in info["results"][0]["adverse_reactions"][0].lower():
            re.append(pmatch.strip())
    print(re)
