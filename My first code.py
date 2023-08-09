def bmi(a,b):
    return a/b**2
    
a = int(input("enter your weight:"))
b = float(input("enter your height :"))


print("your bmi is",bmi(a,b))
if bmi(a,b)<18:
  print("you are underweight")
  print("  Suggestion: Eat balanced diet and do regular exercise")
if 18 <=bmi(a,b)<=25 :
  print("Great! you are fit")
if bmi(a,b)>25:
  print("you are obesed")
  print("Suggestion: Do dieting!")