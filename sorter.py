import os
#get current dir
#cwd=os.getcwd()
cwd='/var/tmp/trash'  # that's the playgarden

#file types associations
mus=['.mp3', '.waw']
vid=['.mp4', '.avi']
doc=['.txt', '.pdf']

#list all the filetypes in playgarden dir

lof=os.listdir(cwd)
print("list of files in dir: " + str(lof))

list_ext=[]   #list of extensions found

for filename in lof:
    s = filename.split('.')
    ext = s[-1]
    list_ext.append("." + ext)

list_ext.sort()
#print(list_ext)
c=set(list_ext)  #converted list to set to DEDUP and for further usage

print("filetypes found [c]: "+str(c))

# check which subdirs to be created if not exist

fa={"Music": mus,"Videos":vid,"Documents":doc}

tbd=[]

for ft in fa:
    i=0
    while i < len(fa[ft]):
        #print("cycle: "+ft)
        #print(fa[ft][i])
        if fa[ft][i] in c :
            print(str(fa[ft][i]) + " is in: " + str(c) + " " + ft + " dir to be created")
            tbd.append(ft)
        else:
            None    # just a placeholder
            #print(str(fa[ft][i]) + " is NOT in: " + str(c))
        #print(ft)
        i=i+1

tbc=set(tbd)        # dedup set of dirs to be created
print("Dirs to be created: " + str(tbc))

# TBD create dirs and move files there
for i in tbc:
    print(cwd+"/"+i)