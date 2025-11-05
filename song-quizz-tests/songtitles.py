  # songtitles.py

artists = [
  "Marty mone ",
  "Marty_mone ",
  "Marty-mone ",
  "the wurzzles ",
  "Eminem ",
  "INTERWORLD ",
  "Glass animals ",
  "Bruno mars ",
  "Electric light orchestra ",
  "The Killers ",
  "oatis mcdonald ",
  "C418 "
  ]

Songs_titles = [
  "Hit the diff",
  "Steer the rear",
  "Slip the clutch",
  "I can drive a tractor",
  "Mockingbird",
  "Metamorphisis",
  "Heatwaves",
  "Locked out of hevan",
  "Mr blue sky",
  "Mr brightside",
  "Scarlet fire",
  "Beginning"
  ]

Song = Songs_titles[0]

  # Refactor the assignment of Song based on artist
for idx, artist in enumerate(artists):
  if artist == "Marty mone ":
    Song = Songs_titles[0]
  elif artist == "Marty_mone ":
    Song = Songs_titles[1]
  elif artist == "Marty-mone ":
    Song = Songs_titles[2]
  elif artist == "the wurzzles ":
    Song = Songs_titles[3]
  elif artist == "Eminem" :
    Song = Songs_titles[4]
  elif artist == "INTERWORLD ":
    Song = Songs_titles[5]
  elif artist == "Glass animals ":
    Song = Songs_titles[6]
  elif artist == "Bruno mars ":
    Song = Songs_titles[7]
  elif artist == "Electric light orchestra ":
    Song = Songs_titles[8]
  elif artist == "The Killers ":
    Song = Songs_titles[9]
  elif artist == "oatis mcdonald ":
    Song = Songs_titles[10]
  elif artist == "C418 ":
    Song = Songs_titles[11]