strhr = input("Input Hours: ")
hr = float(strhr)
strrate = input("Input Rate: ")
rate = float(strrate)
if hr<=40 :
  pay = hr * rate
  print("Gross pay is :",pay)
else :
    exhr = hr-40
    pay = (40 * rate) + (exhr * rate * 1.5)
    print(pay)
