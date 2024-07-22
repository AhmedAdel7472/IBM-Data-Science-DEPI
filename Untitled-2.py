def factorial(number):
   if number==0 or number==1:
      return 1
   else:
      return number*factorial(number-1)
factoz=0
factoz=factorial(5)
print(factoz)