import os, json

img_list = list(os.listdir("images/jsf/partners_and_donors"))

data = []

n = 5
for i in range(0, len(img_list), n):
    temp = []
    for img in img_list[i:i+n]:
        temp.append({"src": f"images/jsf/partners_and_donors/{img}"})
    data.append(temp)

print(json.dumps(data))