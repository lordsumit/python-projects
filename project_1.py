import random
 
 secret_number = random.randint(1,100)
 attempts = 15

 print ( "I'm thinking of a number between 1 to 100")

 while attempts > 0:
  guess=(int(input("take a guess")))
  if guess == secret_number:
    print ("congratulations! you guessed the right number!")
    break
  elif guess < secret_number:
    print('too low')
  else:
    print("too high")
  attempts -= 1

  if attempts == 0:
    print("sorry you've ran out of attempts , the secret number was:" , secret_number)