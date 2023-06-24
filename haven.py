import random
import time
from save import *

# Main menu
init0=("Haven Town\nKevin Roadarmel\n\nEnter C to Coninute\n\nEnter N for New Game\n\n")
# Beginning
init1 = "\n\nHaven Town\nKevin Roadarmel\n\nAliens have depleted Earth of its resources and left behind creatures known as xenomorphs, which humanity has befriended, in order to save themselves from the brink of extinction."
init2 = "\nAs one of the lone survivors, you must travel to Haven Village to meet with the others, but you will first have to traverse...\n\nThe Forest."
init3 = "\nYou awaken from your slumber in your makeshift home made of tree limbs and leaves, your xenomorph pet by your side.\nWhat was her name again?\n"
init4 = "\nYou emerge into the cool-weathered and dark world of The Forest. Despite being populated by millions of creatures, you can only hear the rustling of your footsteps.\n"
init5 = "\nYou trek deeper and deeper - until suddenly..."
# init6 goes with first fight 
init7 = "\nYou trek onward to Haven Village...\n"
inputContinue = "\n\nInput to continue"


answer = ""
running = True



# Different every time
class enemy():
    def __init__(self, name, health, maxhealth, damage, move, move2):
        self.name = name
        self.health = health 
        self.maxhealth = maxhealth
        self.damage = damage
        self.move = move
        self.move2 = move2
# Enemy list
steelwulf = enemy("Steelwulf", 100, 100, 15, "Slash", "Steel Claw")
warpdemon = enemy("Warpdemon", 23, 100, 25, "Blarp", "Timewarp")


def save():
    f = open("save.py", "w")
    f.write("petname = \"" + petname +"\"\n")
    f.write("health = " + str(health) +"\n")
    f.write("maxhealth = " + str(maxhealth)+"\n")
    f.write("damage = " + str(damage)+"\n")
    f.write("movename =\"" + movename+"\"\n")
    f.write("movename2 =\"" + movename2+"\"\n")
    f.write("stage = " + str(stage)+"\n")
    f.close()
    print("******** Saved *********")
    
def confirmName():
  global petname
  petname = input("Enter your xenomorph's name\n")
  answer = input(petname + "? Y or N\n")
  if answer.upper() == "Y" and petname != "":
   print("Pet name confirmed as " + petname + "\n")
  else:
    confirmName()

def stepDrama():
  num = 0
  while num < 3:
    print("\n+1 mile traversed")
    time.sleep(0.5)
    num = num + 1
    
def fight(enemy):
  global health
  global petname
  global damage
  global maxhealth
  while health > 0 and enemy.health > 0:
    askFight = input("\n" + petname + " Health: " + str(int(health)) + "/" + str(maxhealth) + "\n" + enemy.name + " Health: " + str(int(enemy.health)) + "/" + str(enemy.maxhealth) + "\nEnter 1 to use " + movename + " (1x damage)\nEnter 2 to use " + movename2 + " (2x damage)\n\n")
    
    
    if askFight == str(1):
        number = input("\nAttempt to guess a number between 1 and 10 better than the opponent\n\n")
        if number.isdigit():
          number = int(number)
        else:
          fight()
        numAns = random.randrange(1,10)  
        enemyAns = random.randrange(1,10)
        
        
        if number - numAns > enemyAns - numAns:
          enemy.health -= damage
          print("\nYou selected a closer number!\n" + petname + " used " + movename + "\n")
          
          if number - numAns == -1 or number - numAns == 3:
            print("Critical hit! 1.5x damage applied")
            enemy.health -= 1.5 * (damage)
            
        if number - numAns < enemyAns - numAns:
          health -= enemy.damage
          print("\n" + enemy.name + " has selected a better number\n" + enemy.name + " used " + enemy.move)
    if askFight == str(2):
        print("Rolling dice")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        print("...")
        dice = random.randrange(1,6)
        
        if dice == 1:
            print("You rolled a " + str(dice) + "!\n75% of " + enemy.name +"'s health is gone!")
            enemy.health -= 0.75 * enemy.health
        elif dice == 2:
            print("You rolled a " + str(dice) + "!\n" + petname + " hurt herself in confusion!")
            health -= 0.2*(enemy.damage)
        elif dice == 3:
            print("You rolled a " + str(dice) + "!\nNothing happened!")
        elif dice == 4:
            print("You rolled a " + str(dice) + "!\n" + petname + " inleft herself open to an attack, but countered it!")
            health -= 0.5*enemy.damage
            enemy.health -= damage
        elif dice == 5:
            print("You rolled a " + str(dice) + "!\n" + petname + " missed the enemy " + enemy.name+"!")
        elif dice == 6:
            print("You rolled a " + str(dice) + "!\n75% of " + enemy.name +"\'s health is gone!")
            enemy.health -= 0.75 * enemy.health
        
  if enemy.health <= 0:
    print("\nYou have won the battle against " + enemy.name + "!\n")
    health = maxhealth
  elif health <= 0:
    print("\n\nGame over.")
    quit()


cONTrue = True
while cONTrue:

    continueOrNew = input(init0)

    if continueOrNew.upper() == "N":
        petname = ""
        health = 100
        maxhealth = 100
        damage = 50
        movename = "Chomp"
        movename2 = "Buzz"
        stage = 0
        cONTrue = False
    elif continueOrNew.upper() == "C":
        cONTrue = False

    else:
        pass

while running:

    if stage == 0:

        input(init1 + inputContinue)
        input(init2 + inputContinue)
        print(init3)

        confirmName()
        stage = 1
        save()

    elif stage == 1:
        input(init4 + inputContinue)
        stepDrama()
        input(init5 + inputContinue)
        enemyname = "Steelwulf"
        init6 = "\nA " + enemyname + " has appeared!"
        input(init6 + inputContinue)

        fight(steelwulf)
        stage = 2
        save()
    
    elif stage == 2:
        input(init7 + inputContinue)
        stepDrama()

        enemyname = "Warpdemon"
        init6 = "\nA " + enemyname + " has appeared!"
        input(init6 + inputContinue)
        fight(warpdemon)
        input(init7 + inputContinue)
        stage = 3
        save()
        running = False

quit()