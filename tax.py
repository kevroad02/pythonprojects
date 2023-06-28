# Global variable for how many hours have been worked
dwHours = 0

# Global num used for intPut function results
num = 0

# Here's the global tax number if you want to change that
tax = 0.13



def intPut(question):
    global num
    # Gets string intPut to ask the questions 
    theInput = input(question)
    # If input is an integer
    if theInput.isnumeric():
        num = int(theInput)
    else:
        print("\nPlease enter a number without decimals.")
        # Re-asks question if false
        intPut(question)
    



def daysWorked():
    global dwHours
    global num
    days = ["Sunday: ", "Monday: ","Tuesday: ", "Wednesday: ","Thursday: ","Friday: ","Saturday: "]
    howMany = "\nHow many hours did you work on "
    # Runs through days of the week list and adds up each number responses
    for i in days:
        dayWorked = intPut(howMany + i)
        dwHours = dwHours + num
    
    print("\nYou have entered in working " + str(dwHours) + " hours.")
        
    
    
    
    
    
def approximate(wk):
    global dwHours
    global tax
    # If weekly
    if wk == "W":
        hoursWorked = input("\nDo you know how many hours you've worked this week? Y or N: ")
        if hoursWorked.upper() == "Y":
            intPut("\nEnter how many hours you've worked: ")
            # intPut responses are always converted to nums so dwHours now equals how many hours user has worked
            dwHours = num
        elif hoursWorked.isnumeric():
            intPut("\nEnter how many hours you've worked: ")
            dwHours=num
        else:
            # daysWorked function goes through each day and asked them how mant hours they've worked on that dau
            daysWorked()
        perHourQ = intPut("\nWhat is your salary per hour?: ")
        perHour = num
        # Hourly salary times hours worked minus taxes
        print("\nYou will be paid $" + str(((perHour*dwHours) - ((perHour*dwHours)*tax))))
    elif wk == "BW":
        hoursWorked = input("\nDo you know how many hours you've worked over these two week? Y or N: ")
        if hoursWorked.upper() == "Y":
            intPut("\nEnter how many hours you've worked: ")
            dwHours = num
        elif hoursWorked.isnumeric():
            intPut("\nEnter how many hours you've worked: ")
            dwHours = num
        else:
            # Asks to enter each week of work, data combines automatically since it just keeps adding together in the dwHours variable 
            print("\nEnter your first week of work")
            daysWorked()
            print("\nEnter your second week of work")
            daysWorked()
        perHourQ = intPut("\nWhat is your salary per hour?: ")
        perHour = num
        print("\nYou will be paid $" + str(((perHour*dwHours) - ((perHour*dwHours)*tax))))
    



# Beginning of program, asks if looking for weekly or biweekly results
weekAmount = input("Pennsylvania Paycheck Approximator (13% Tax)\nKevin Roadarmel\n\nEnter W if you get paid weekly, or BW for biweekly: ")
if weekAmount.upper() == "BW":
    print("\nBiweekly has been selected")
    wkOrBi = "BW"
    # Sends biweekly to function 
    approximate(wkOrBi)
if weekAmount.upper() == "W":
    print("\nWeekly has been selected")
    # Sends weekly to function
    wkOrBi = "W"
    approximate(wkOrBi)