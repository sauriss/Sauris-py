num = 0
tot = 0.0
while True :
    val = input("enter a number:")
    if val == "done" :
        break
    try:
        fval = float(val)
    except:
        print ("please enter only interger value")
        continue
    num = num + 1
    tot = tot + fval
print ("all done")
print ("total numbers -- total value-- total average")
print(num,tot,tot/num)
