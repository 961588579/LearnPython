import tinify
import os

tinify.key = "LDY6ZCkKe2nnacJJTa_FDqPZcyv8z2Jr"

all_png = []

def find_all_png(file_path):
    file_list = os.listdir(file_path)
    for file in file_list:
        path = os.path.join(file_path, file).replace("\\", "/")
        if os.path.isfile(path):
            if path.endswith(".png"):
                all_png.append(path)
            pass
        elif os.path.isdir(path):
            find_all_png(path)
        pass
    

def do_tiny_png(path):
    print("tinypng " + path)
    source = tinify.from_file(path)
    source.to_file(path)

if __name__ == '__main__':

    # game_name = "xbhall"
    # find_all_png("E:/workSpace/client/branches/xibao/" + game_name + "/assets/resources/")
    # find_all_png("E:/workSpace/client/branches/xibao/xbhall/assets/resources/textures/hall/")
    find_all_png("E:/workSpace/client/branches/xibao/xbhall/assets/resources/textures/loading/")
    find_all_png("E:/workSpace/client/branches/xibao/xbhall/assets/resources/textures/srnn/")
    find_all_png("E:/workSpace/client/branches/xibao/xbhall/assets/resources/textures/symj/")

    old_size = 0
    new_size = 0
    
    size = len(all_png)
    index = 0
    for file in all_png:
        oz = os.path.getsize(file) * 1.0/1024
        do_tiny_png(file)
        nz = os.path.getsize(file) * 1.0/1024
        old_size += oz
        new_size += nz
        index += 1
        print("compress rate " + str(nz * 100.0 / oz) + "%")

    print("compress done before:" + str(old_size) + ",after:" + str(new_size))
