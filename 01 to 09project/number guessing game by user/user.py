import random
print("Computer has thought secret number! now guess please!")
secret_number = random.randint(1, 10)
try:
 while True:
     user_input = int(input("now guess yourself (1-10):"))
     if user_input == secret_number:
       print("Bingo! you have correctly guess!✅")
       break
     elif user_input < secret_number:
      print("Think big")
     elif user_input > secret_number:
         print("Think small")
except ValueError:
   print("Invalid Input")
try:
  user_input=int(input("Enter a Number"))
  a= 10/user_input
  print(a)
except ZeroDivisionError:
  print("ZeroDivisionError")
except ValueError:
  print("Invalid input")
else:
  print("else",a)
finally:
  print("program end ..")
  