run = True

# input to continue shortened to inC
inC = "\n\nInput to continue"

# Used to automatically space out text
def inSpace(stringVar):
    return input(stringVar + "\n\n" + "Input to continue\n\n")

def enterName():
    name = input("These are the survivors of humanities extinction. One day, you were brought a flyer from your pet xenomorph ... what was her name again?")
    if name == "":
        print("Name cannot be blank!")
        enterName()


while run == True:
    inSpace("Haven Town\nKevin Roadarmel")
    inSpace("You awaken in a desolate field. The aliens have taken a majority of the planets resources, but there is thing one thing they have left behind.\n\nXenos.")
    inSpace("These creatures have assisted in humanities extinction, but have also aided a skillfull few who were able to tame these monsters and use them for protection.")
    enterName()
    
    