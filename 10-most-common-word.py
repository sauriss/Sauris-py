handle = open('romeo.txt')



di = dict()
for line in handle:
    words = line.split()
    for wrd in words:
        di[wrd] = di.get(wrd, 0) + 1
print(di)

li = list()
for k,v in di.items():
    newtup = (v,k)
    li.append(newtup)
    li = sorted(li,reverse=True)
print(li)
for val,key in li[:10] :
    print(val,key)
