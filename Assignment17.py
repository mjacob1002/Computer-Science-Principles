import random
def count(x: float):
  print("I'm going to count to ", x, ".")
  k = int(x)
  for i in range(k):
    print(i+1)
print("What is your name?")
x = input()
print("Hello ", x)

def game():
  flag = False
  x = random.randint(1,5)
  print("Give correct number between 1 and 5 inclusive to leave loop")
  while(flag == False):
      y = input()
      y = int(y)
      if x == y:
          flag = True
      else:
          print("Try again")
            
        
      
# personalize 1
print("Give an integer between 1 and 10")
y = input()
count(y)

#personalize 2
game()
#personalize 3
print("End of program. THis is my personalization.")


