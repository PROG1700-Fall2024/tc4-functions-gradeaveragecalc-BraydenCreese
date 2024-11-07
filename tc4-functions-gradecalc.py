############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Brayden Creese W0491583

# did my best with this today, just could not get my brain to work and output stuff today. 
# Code Does Not Run.

def gradeCalc(letterGrade, modifier):

    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3

    return numericGrade

gradeCalc()


def main():

    courses = ['PROG1700', 'NETW1700', 'OSYS1200', 'WEBD1000', 'COMM1700', 'DBAS1007']

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    numericGrade = 0.0

    for i in range(6):
        #Gather user inputs
        letterGrade = input("Please enter a letter grade: ").upper()
        modifier = input("Please enter a modifier (+, - or nothing): ")


    print("*" * 60)
    print(f"The numeric value for {courses} is: {0:.1f}".format(numericGrade))

    print("=" * 60)
    print(f"Your grade point average for the semester is: {0:.1f}".format(averageGrade))
    print("=" * 60)

main()

