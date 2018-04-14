score = input("enter score <range 0.0 - 1.0>: ")
try :
  intscore = float(score)
except :
  intscore = -1
  print ("please enter a numeric value")
if intscore > 1.0 :
  print ("Value is out of range, please enter value within 0.0 to 1.0")
elif intscore >=0.9 and intscore < 1.0 :
  print ("A")
elif intscore >=0.8 and intscore < 0.9 :
  print ("B")
elif intscore >=0.7 and intscore < 0.8 :
  print ("C")
elif intscore >=0.6 and intscore < 0.7 :
  print ("D")
elif intscore < 0.6 and intscore > 0.0 :
  print ("F")
else :
    print ("Please try agian")
