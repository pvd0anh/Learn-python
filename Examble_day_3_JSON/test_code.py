dict1 = {}
dict1 = {1:"PVD",2:[1,2,3,4,5,6]}

print((type(dict1)))
for i in dict1:
    print(type(dict1[i]))
    for j in dict1[i]:
        print(j)