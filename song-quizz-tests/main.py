import random


Music = []
Fh = open("Music.txt","r")
for line in Fh:
  line = line.strip()
  s,a = line.split(":")
  Music.append([s,a])
print(Music)

score = 0
stop = 0

qnum = 1
while stop == 0:
  print("question",qnum)
  qnum += 1
  print("score = ",score)
  num = random.randint(0, len(Music)-1)
  print("ran num = ",num)
  question = Music[num]
  song = Music[num]
  print(question[0])
  Song = song[1]
  Song = Song.lower()
  S_list = Song.split
  for word in S_list():
    print(word[0])
  PA = input("ans")
  if PA == song[1]:
    print("cool")
  else:
    exit()