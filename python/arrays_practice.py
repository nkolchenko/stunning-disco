'''# Given an array of arrays, flatten into a single array. Ex: [[1,2,3,4], [5,6],[7]]. Output [1,2,3,4,5,6,7].
from collections.abc import Iterable
a=[[1,2,3,4], [5,6,7],[7,[8,[9,10,[11]]]]]
z=[]
y=1
b=a

print(a)
#while any(isinstance(i, list) for i in a) or  y<len(a):

print('_y_ ',y)
print('len a: ',len(a))
for sublist in a:
    print('HERE')
    print('Sublist: ',sublist)
    for item in sublist[:]:
        #print('item--: ',item)
        if not isinstance(item, list):
            #print('Here added: ',item)
            z.append(item)
            #print('z now: ', z)
        else:
            orig_len=len(item)
            print('ori_len',orig_len)
            s=0
            while orig_len >= s:
                print('\n------LOOP---- \nlen: ',len(item),'\ns=',s,'\nitem: ', item)
                for sub in item[:]:
                    #while len(item)!=0:
                    if isinstance(sub, list):
                        print("Sub: ",sub, "is a list")
                        z.append(sub[0])
                        print('got SUB: ',sub[0], 'stripping it')
                        print('z now: ', z)
                        sub.pop(0)
                        print('sub_now:', sub)
                        #item.remove(sub)
                        print('item_now: ', item)
                        s=s+1
                    else:
                        print("Sub: ",sub, "is NOT a list")
                        z.append(sub)
                        print("stripping it")
                        item.remove(sub)
                        print('item_now: ',item)
                        print('z_appp: ',z,'\n')
                        s=s+1

print('Original List', a)
print('Transformed Flat List', z)
'''

a="qwerty"
for b in a:
    print(b.capitalize())