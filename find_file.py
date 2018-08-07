import os

def findTextureFile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        file_type = ".png"
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            # 输出文件大于512KB的文件
            if file.endswith(file_type) and os.path.getsize(filepath)/1024 > 512:
                print("resArray.push(\"" + filepath[0:len(filepath) - len(file_type)].replace("\\", "/") + "\");")
                # print(file.endswith("json"))
                pass
        elif os.path.isdir(filepath):
            findTextureFile(filepath)
            pass
    pass

def findAnimFile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        file_type = ".json"
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            # 输出文件大于512KB的文件
            if file.endswith(file_type):
                print("resArray.push(\"" + filepath[0:len(filepath) - len(file_type)].replace("\\", "/") + "\");")
                # print(file.endswith("json"))
                pass
        elif os.path.isdir(filepath):
            findAnimFile(filepath)
            pass
    pass

if __name__ == '__main__':
    game_name = "jsll"
    #path = "E:/workSpace/client/branches/xinxinyao/xxyhall/assets/resources/textures/hall"

    path = "E:/workSpace/client/branches/xibao/" + game_name + "/assets/resources/textures/" + game_name + ""
    findTextureFile(path)

    path = "E:/workSpace/client/branches/xibao/" + game_name + "/assets/resources/anims"
    findAnimFile(path)
