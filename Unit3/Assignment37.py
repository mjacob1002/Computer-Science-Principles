players = set()

# got rid of while loop
print("Hi, what's your name?")
x = input()
if x is in players:
  print("Welcome back, ", x)
else:
  players.add(x)
  print("Thanks for joining us, ", x)
