def computepay(T, R) :
  if T>40:
    pay = (40*R) + ((T-40)* R * 1.5)
    print (pay)
  else :
    pay = T * R
    print (pay)
Time = float(input("please enter Time: "))
Rate = float(input("please enter Rate: "))

computepay(Time, Rate)
