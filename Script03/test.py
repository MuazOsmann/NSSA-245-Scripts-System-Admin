import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            name = os.path.join(root, name)
        if(name == None):
            print("ERROR: The file does not exist!")

print(find('testtasdkasml', '/home/'))