import time

Attempts = 0
pwrd = input("Please enter password: ")
if pwrd == "Secret":
  print("Correct password")
  time.sleep(2)
  print("Logging in \n [--------]")
  time.sleep(1)
  print("[¦¦------]")
  time.sleep(3)
  print("[¦¦¦¦----]")
  time.sleep(5)
  print("[¦¦¦¦¦¦--]")
  time.sleep(8)
  print("Logged in \n [¦¦¦¦¦¦¦¦]")
else:
  print("Incorrect password")
  if Attempts == 4:
    print("Locked \n Try again in 1 minuet")
    time.sleep(60)
  elif Attempts == 6:
    print("Locked \n Try again in 2 minuets")
    time.sleep(120)
  elif Attempts == 8:
    print("Locked \n Try again in 4 minuets")
    time.sleep(240)
  elif Attempts == 10:
    print("Locked \n Try again in 8 minuets")
    time.sleep(480)
  elif Attempts == 12:
    print("Locked\n Please plug phone into Computer and restore")
    exit()
while pwrd != "Secret":
  Attempts += 1
  pwrd = input("Please enter password: ")
  if pwrd == "Secret":
    print("Correct password")
    time.sleep(2)
    print("Logging in \n [--------]")
    time.sleep(1)
    print("[¦¦------]")
    time.sleep(3)
    print("[¦¦¦¦----]")
    time.sleep(5)
    print("[¦¦¦¦¦¦--]")
    time.sleep(8)
    print("Logged in \n [¦¦¦¦¦¦¦¦]")
  else:
    print("Incorrect password")
    if Attempts == 4:
      print("Locked \n Try again in 1 minuet")
      time.sleep(60)
    elif Attempts == 6:
      print("Locked \n Try again in 2 minuets")
      time.sleep(120)
    elif Attempts == 8:
      print("Locked \n Try again in 4 minuets")
      time.sleep(240)
    elif Attempts == 10:
      print("Locked \n Try again in 8 minuets")
      time.sleep(480)
    elif Attempts == 12:
      print("Locked\n Please plug phone into Computer and restore")
      exit()