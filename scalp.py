import json, os

logins = {
    "email":[],
}

f = open(f'{os.getcwd()}//info.txt', "r")

data = f.read()
f.close()


while len(data) != 0:
    pstart = data.find(":")
    end = data.find("|")

    user = data[1:pstart]
    password = data[pstart + 1: end]
    data = data[end + 1:]
    logins["email"].append([user, password])
with open("logins.json", "w") as outfile:
    json.dump(logins, outfile)