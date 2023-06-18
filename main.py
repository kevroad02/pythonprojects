import random

# Beginning
init1 = "Haven Town\n\nKevin Roadarmel\n\nAliens have extracted the Earth's materials and left behind creatures known as xenomorphs. As humanity neared extinction, they befriended these creatures in order to survive."
init2 = "You are one of the lone survivors. You must travel to Haven Village to meet with other survivors, but you will have to traverse...\n\nThe Forest."
init3 = "You awaken from your slumber in your makeshift home with your xenomorph pet by your side.\nWhat was her name again?\n"
# Post-Name confirm
init4 = "You emerge into the cool and dark world of The Forest"
init5 = "You trek deeper and deeper - until suddenly..."
# init6 goes with first fight 
init7 = "You trek onward to Haven Village..."
inputContinue = "\n\nInput to continue\n"
answer = ""
petname = ""
running = True
health = 100
damage = 50
movename = "Chomp"
enemyname = ""
enemyhealth = 0
enemydamage = 0
enemymove = ""

def confirmName():
  global petname
  petname = input("Enter your xenomorph's name\n")
  answer = input(petname + "? Y or N\n")
  if answer.upper() == "Y" and petname != "":
   print("Pet name confirmed as " + petname)
  else:
    confirmName()

def stepDrama():
  num = 0
  while num < 2:
   input("+1 mile traversed" + inputContinue)
   num = num + 1
    
def fight(enname, enhealth, endamage, enmove):
  enemyname = enname
  enemyhealth = enhealth
  enemydamage = endamage
  enemymove = enmove
  global health
  global petname
  global damage
  while health > 0 and enemyhealth > 0:
    number = input("\nGuess a number between 1 and 10\n")
    if number.isdigit():
      number = int(number)
    else:
      fight()
    numAns = random.randrange(1,10)  
    enemyAns = random.randrange(1,10)
    if number - numAns > enemyAns - numAns:
      enemyhealth -= damage
      print(petname + " used " + movename + "\nEnemy health is now " + str(enemyhealth) + "!")
    else:
     health -= enemydamage
     print(enemyname + " used " + enemymove + "\nPlayer health is now " + str(health) + "!")
  if enemyhealth <= 0:
    print("\nYou have won the battle against " + enemyname + "!\n")
  elif health <= 0:
    print("Game over.")
    quit()

input(init1 + inputContinue)
input(init2 + inputContinue)
print(init3)

confirmName()

input(init4 + inputContinue)
stepDrama()
input(init5 + inputContinue)
enemyname = "Steelwulf"
init6 = "A " + enemyname + " has appeared!"
input(init6 + inputContinue)

fight("Steelwulf", 100, 15, "Slash")

input(init7 + inputContinue)
stepDrama()
   
  