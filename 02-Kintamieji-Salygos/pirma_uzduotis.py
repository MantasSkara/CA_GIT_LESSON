a = int(input("Įveskite skaičių "))
b = float(input("Įveskite skaičių "))
if b > a:
  print("a mažesnis už b")
  print("dalyba: " + str(b/a))
elif a == b:
  print("a lygu b")
  print("Sudėtis: " + str(a+b))
else:
  print("a didesnis už b")
  print("dalyba: " + str(a/b))

