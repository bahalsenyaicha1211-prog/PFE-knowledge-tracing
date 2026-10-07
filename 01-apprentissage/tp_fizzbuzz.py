for i in range(1,51):
    if i%15 == 0: #multiple de 3 et 5
      print("FizzBuzz")
    elif i%5 == 0: #multiple de 5
      print("Buzz")
    elif  i%3==0:#multiple de 3
      print("Fizz")
    else:
      print(i) #affiching the number if it is not a multiple of 3 or 5
print("Fin du programme")