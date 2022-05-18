import imghdr
import os, json

def photo_src_json(path, n):
    isimg = lambda x : not os.path.isdir(f"{path}/{x}") and imghdr.what(f"{path}/{x}")
    img_list = list(filter(isimg, list(os.listdir(path))))

    data = []
    for i in range(0, len(img_list), n):
        temp = []
        for img in img_list[i:i+n]:
            temp.append({"src": f"{path}/{img}"})
        data.append(temp)

    return data

# partners
with open("data/partners.json", "w") as f:
    data = photo_src_json("images/jsf/partners", 4)
    json.dump(data, f)

# donors
with open("data/donors.json", "w") as f:
    data = photo_src_json("images/jsf/donors", 4)
    json.dump(data, f)

# gallery
with open("data/gallery.json", "w") as f:
    data = photo_src_json("images/jsf/uploads", 4)
    json.dump(data, f)
    
    