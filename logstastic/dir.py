import os
for filename in os.listdir("./info"):
    # print filename
    file_object = open('./info/' + filename)
    for line in file_object:
        print(line)
    file_object.close()