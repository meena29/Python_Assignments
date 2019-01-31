def readfile(path): 
    with open(path, 'r') as f: 
       for line in f :
       		yield line

for item in readfile("ex.txt"):
    print(item)