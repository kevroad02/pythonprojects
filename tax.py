wkOrBi = ""
stage = 0
intNumeric = True


def checkInt(number):
    if number.isnumeric():
        intNumeric = True
    else:
        intNumeric = False
    

def daysWorked():
    global stage
    run = True
    while run:
        if stage == 0:
            day = "Sunday"
            dayWorked = input("How many hours did you work on " + day)
            checkInt(dayWorked)
            stage = 1
        
        elif stage == 1:
            day = "Monday"
            dayWorked = input("How many hours did you work on " + day)
            checkInt(dayWorked)
            stage = 2
        
        elif stage == 2:
            day = "Tuesday"
            dayWorked = input("How many hours did you work on " + day)
            checkInt(dayWorked)
            stage = 3
        elif stage == 3:
            day = "Wednesdau"
            dayWorked = input("How many hours did you work on " + day)
            checkInt(dayWorked)
            stage = 4
        elif stage == 4:
            day = "Thursday"
            dayWorked = input("How many hours did you work on " + day)
            checkInt(dayWorked)
            stage = 5
        elif stage == 5:
            day = "Friday"
            dayWorked = input("How many hours did you work on " + day)
            checkInt(dayWorked)
            stage = 6
        elif stage == 6:
            day = "Saturday"
            dayWorked = input("How many hours did you work on " + day)
            checkInt(dayWorked)
            run = False
    
def approximate(wk):
    global wkOrBi
    if wkOrBi == "W":
        hoursWorked = input("\nHow many hours did you work this week? Input IDK for \"I don't know\": ")
        if hoursWorked.upper() == "IDK":
            daysWorked()
            
    




weekAmount = input("Pennsylvania Paycheck Approximator\nKevin Roadarmel\n\nEnter W if you get paid weekly, or BW for biweekly: ")
if weekAmount.upper() == "BW":
    wkOrBi
    print("\nBiweekly has been selected")
    wkOrBi = "BW"
    approximate(wkOrBi)
if weekAmount.upper() == "W":
    wkOrBi
    print("\nWeekly has been selected")
    wkOrBi = "W"
    approximate(wkOrBi)