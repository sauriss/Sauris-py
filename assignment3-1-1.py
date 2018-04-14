strhr = input("Input Hours: ")
strrate = input("Input Rate: ")
try :
    hr = float(strhr)
    rate = float(strrate)
except :
    print("please enter numeric values")
    quit()
if hr<=40 and hr>=0 :
  pay = hr * rate
  print("Gross pay is :",pay)
else :
    exhr = hr-40
    pay = (40 * rate) + (exhr * rate * 1.5)
    print("Gross pay is :",pay)
