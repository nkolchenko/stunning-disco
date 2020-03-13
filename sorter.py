import os
#get current dir
#cwd=os.getcwd()
cwd='/tmp/trash'

#list all the filetypes in it
lof=os.listdir(cwd)
print("list of files in dir: " + str(lof))
b=[]

for filename in lof :
    s=filename.split('.')
    ext=s[-1]
    b.append(ext)
    #print(b)

#b.sort()
c=set(b)

print("filetypes set: "+str(c))

# check which subdirs to be created if not exist

subpath='ololo'
newdir=cwd+subpath
#print(newdir)

#redo for lists
if subpath not in lof:
    print("NotIn")
else:
    print("got it")

#os.mkdir(newdir)


'''
basedir=

for path in

os.makedirs(path)

basepath = sys.argv[1]
for entry in os.listdir(basepath):
    s = entry.split('.')
    ext = s[-1]
    if os.path.isfile(os.path.join(basepath, entry)):
        if len(s) <= 1:
            print("skipping file ", entry)
            continue

        dirName = os.path.join(basepath, ext)
        if not os.path.exists(dirName):
            print("dir ", dirName, " doeas not exist; creating it")
            # os.mkdir(dirName)
        fromFile = os.path.join(basepath, entry)
        toFile = os.path.join(dirName, entry)
        print("moving ", fromFile, " to ", toFile)
        # os.rename(fromFile, toFile)
    else:
        print(entry, " is not a file; skipping")
        continue
'''