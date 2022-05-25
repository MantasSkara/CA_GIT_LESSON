a = int(input("Įveskite skaičių yyyy"))
b = float(input("Įveskite skaičiųy yyy "))
if b > a:
  print("a mažesnis už b")
  print("dalyba: " + str(b/a))
elif a == b:
  print("a lygu b")
  print("Sudėtis: " + str(a+b))
else:
  print("a didesnis už b")
  print("dalyba: " + str(a/b))

  # if a == b:
#   print("a lygu b")
#   print("Sudėtis: " + str(a+b))
# if a > b:
#   print("a didesnis už b")
#   print("dalyba: " + str(a/b))
