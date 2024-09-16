def main():
    print("Enter 1 for Roman Numeral to Arabic Numeral Conversion.")
    print("Enter 2 for Arabic Numeral to Roman Numeral Conversion.")
    choice = int(input())
    if (choice == 1):
        r2aConverter()
    elif (choice ==2):
        a2rConverter()
    else:
        print("You did not enter a 1 or 2. Goodbye.")

def r2aConverter():
    print("Enter a Roman Numeral")
    ##################### Begin_Citation [1] ##########################
    num2convert = list(input())
    ##################### End_Citation [1] ############################
    workingAnswer = 0
    for i in range(len(num2convert)):
        if num2convert[i] == 'M':
            workingAnswer += 1000
        elif num2convert[i] == 'D':
            if (i != len(num2convert)-1):
                if num2convert[i+1] == "M":
                    workingAnswer -= 500
                else:
                    workingAnswer += 500
            else:
                workingAnswer += 500
        elif num2convert[i] == 'C':
            if (i != len(num2convert)-1):
                if num2convert[i+1] == "D" or num2convert[i+1] == "M":
                    workingAnswer -= 100
                else:
                    workingAnswer += 100
            else:
                workingAnswer += 100
        elif num2convert[i] == 'L':
            if (i != len(num2convert)-1):
                if num2convert[i+1] == "D" or num2convert[i+1] == "M" or num2convert[i+1] == "C":
                    workingAnswer -= 50
                else:
                    workingAnswer += 50
            else:
                workingAnswer += 50
        elif num2convert[i] == 'X':
            if (i != len(num2convert)-1):
                if num2convert[i+1] == "D" or num2convert[i+1] == "M" or num2convert[i+1] == "C" or num2convert[i+1] == "L":
                    workingAnswer -= 10
                else:
                    workingAnswer += 10
            else:
                workingAnswer += 10
        elif num2convert[i] == 'V':
            if (i != len(num2convert)-1):
                if num2convert[i+1] == "D" or num2convert[i+1] == "M" or num2convert[i+1] == "C" or num2convert[i+1] == "L" or num2convert[i+1] == "X":
                    workingAnswer -= 5
                else:
                    workingAnswer += 5
            else:
                workingAnswer += 5
        elif num2convert[i] == 'I':
            if (i != len(num2convert)-1):
                if num2convert[i+1] == "D" or num2convert[i+1] == "M" or num2convert[i+1] == "C" or num2convert[i+1] == "L" or num2convert[i+1] == "X" or num2convert[i+1] == "V":
                    workingAnswer -= 1
                else:
                    workingAnswer += 1
            else:
                workingAnswer += 1
        else:
            print("Invalid Numeral Entered")
        i += 1
    print(workingAnswer)

def a2rConverter():
    print("Enter an Arabic Number")
    num2convert = int(input())
    workingAnswer = []
    while (num2convert > 0):
        if(num2convert >= 1000):
            workingAnswer.append("M")
            num2convert -= 1000
        elif(num2convert >= 900):
            workingAnswer.append("CM")
            num2convert -= 900
        elif(num2convert >= 500):
            workingAnswer.append("D")
            num2convert -= 500
        elif(num2convert >= 400):
            workingAnswer.append("CD")
            num2convert -= 400
        elif(num2convert >= 100):
            workingAnswer.append("C")
            num2convert -= 100
        elif(num2convert >= 90):
            workingAnswer.append("XC")
            num2convert -= 90
        elif(num2convert >= 50):
            workingAnswer.append("L")
            num2convert -= 50
        elif(num2convert >= 40):
            workingAnswer.append("XL")
            num2convert -= 40
        elif(num2convert >= 10):
            workingAnswer.append("X")
            num2convert -= 10
        elif(num2convert >= 9):
            workingAnswer.append("IX")
            num2convert -= 9
        elif(num2convert >= 5):
            workingAnswer.append("V")
            num2convert -= 5
        elif(num2convert >= 4):
            workingAnswer.append("IV")
            num2convert -= 4
        elif(num2convert >= 1):
            workingAnswer.append("I")
            num2convert -= 1
        else:
            break
    #################### Begin_Citation [2] ####################
    print("".join(workingAnswer))
    #################### End_Citation [2] ######################

main()