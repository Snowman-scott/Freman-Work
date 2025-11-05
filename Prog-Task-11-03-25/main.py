import replit

print("Welcome to Guess the word! \n Player 1 please enter a Word")
sw = input("Secret word: ")
replit.clear()
print("Player 2 You now have to guess the secret word")
low = len(sw)
print("The word is", low ,"characters long")

c = 0
for i in range(len(sw)):
  if sw[i] == c:
    c=c+1

print()
for y in range(4):
  g = input("Player 2 Enter a letter: ")
  if g == :
    print("There is an", g ,"in the word")
  else:
    print("Nope")