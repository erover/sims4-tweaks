import sys
import os

#stores values for aging option ratios
#medium is not allowed to be changed from 1

namingConvention = "S4_03B33DDF_00000000_5D0152209188C58B%%+ITUN.tuning"

ratios = {1 : 2, #short
          2 : 1, #medium
          3 : 0.25 #long
          }
ratioStr = {1 : "Short",
            2 : "Medium",
            3 : "Long"
            }
tempRatios = {1 : "$FAST_MULT",
              2 : "$NORMAL_MULT",
              3 : "$SLOW_MULT"
              }
#stores values for age lengths under medium setting
medLengths = {1 : 3, #baby
              2 : 13, #child
              3 : 13, #teen
              4 : 20, #young adult
              5 : 20, #adult
              6 : 10 #elder
        }
#dictionary corresponds the index of the medLengths to the name of the age stage it corresponds to
ageStr = {1 : "Baby",
              2 : "Child",
              3 : "Teen",
              4 : "Young Adult",
              5 : "Adult",
              6 : "Elder"
        }
tempAges = {1 : "$B_THRESH",
            2 : "$C_THRESH",
            3 : "$T_THRESH",
            4 : "$YA_THRESH",
            5 : "$A_THRESH",
            6 : "$E_THRESH"
            }
#both dictionaries are initialized to the default Sims 4 age lengths and ratios

def menu():
    print("\n")
    print("Please Choose an Option:")
    print("1. Change Lifespan Ratios")
    print("2. Set Age Lengths")
    print("3. Show Current Age Legnths")
    print("4. Finish & Export")
    return 0
                
def displayCurrentSettings():
    print("Lifespan Setting Ratios")
    print("-----------------")
    print("Setting | Ratio |")
    print("-----------------")
    for x in range (1, 4):
        print(ratioStr[x].ljust(7) + " | " + str(ratios[x]).center(5) + " |")
    print("-----------------")
    print("\nLife Stage Lengths")
    print("-------------------------------------")
    print("Stage       | Short | Medium | Long |")
    print("-------------------------------------")
    for x in range(1, 7):
        print(ageStr[x].ljust(11) + " | " + str(medLengths[x]/ratios[1]).center(5) + " | " + str(medLengths[x]).center(6) + " | " + str(medLengths[x]/ratios[3]).center(4) + " |")
    print("-------------------------------------")
    print("!!Elder stage length is determined by multiple in-game factors.!!\n!!The value displayed here is just the bottom limit.!!")

    print("\nEstimated Lifespan")
    print("--------------------")
    print("Setting | Lifespan |")
    print("--------------------")
    for x in range(1, 4):
        span = 0
        for y in range(1, 7):
            span = span+(medLengths[y]/ratios[x])
        print(ratioStr[x].ljust(7) + " | " + str(span).center(8) + " |")
    print("--------------------")

def setAgeLengths():
    print("Enter the length of each age state on the medium setting...")
    print("Note: The length of the Elder life stage is determined by more than this value and the value you set here is just the minimum length of the stage.")
    inputLengths = []
    for x in range(1, 7):
        print("Enter new length for the "+ ageStr[x] +" stage:")
        lenInput = input("> ")
        inputLengths.append(lenInput)
    print("\nLife Stage Lengths")
    print("-------------------------------------")
    print("Stage       | Short | Medium | Long |")
    print("-------------------------------------")
    for x in range(1, 7):
        print(ageStr[x].ljust(11) + " | " + str(inputLengths[x - 1]/ratios[1]).center(5) + " | " + str(inputLengths[x - 1]).center(6) + " | " + str(inputLengths[x - 1]/ratios[3]).center(4) + " |")
    print("-------------------------------------")
    while True:
        print("Is this correct? (y/n)")
        confirmation = raw_input("> ")
        if confirmation.lower() == "y":
            for x in range(1, 7):
                medLengths[x] = inputLengths[x - 1]
            return 0
        else:
            print("Change cancelled. Returning to menu.")
            return -1
        return 0
    
def setRatios():
        print("Enter new ratio for the " + ratioStr[1] + " setting:")
        shrt = input("> ")
        print("Enter new ratio for the " + ratioStr[3] + " setting:")
        lng = input("> ")
        print("\n-----------------")
        print("Setting | Ratio |")
        print("-----------------")
        print(ratioStr[1].ljust(7) + " | " + str(shrt).center(5) + " |")
        print(ratioStr[2].ljust(7) + " | " + "1".center(5) + " |")
        print(ratioStr[3].ljust(7) + " | " + str(lng).center(5) + " |")
        print("-----------------")
        while True:
                print("\n Are these values correct? (y/n)")
                confirmation = raw_input("> ")
                if confirmation.lower() == "y":
                        ratios[1] = shrt
                        ratios[3] = lng
                        print("Setting ratios overwritten.")
                        return 0
                else:
                        print("Change cancelled. Returning to menu.")
                        return -1
        
        return 0
def export():
    #IF YOU HAVE PRVIOUSLY GENERATED XML USING THIS SCRIPT AND HAVE NOT MOVED IT OUT OF THE DEFAULT DIRECTORY THIS FUNCTION WILL DELETE AND REPLACE IT
    #cleans up files that previous runs of the scipt may have created
    if os.path.isfile(namingConvention):
        os.remove(namingConvention)

    template = open("template.tuning")
    newXML = open("new.tuning", "wt")

    #first pass over both template.tuning and new.tuning
    #fills in new.tuning with the contents of the template but with the variable placeholders replaced with our actual variables
    for line in template:
        for x in range(1, 7):
            line = line.replace(tempAges[x], str(medLengths[x]))
        newXML.write(line)
    newXML.close()
    template.close()

    #second pass over new.tuning, first pass over the final file
    #purges whitespace from new file because EA recommends to do so
    #probably a performance thing
    final = open(namingConvention, "wt")
    newXML = open("new.tuning")
    for line in newXML:
        line = line.strip()
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        final.write(line)
    newXML.close()
    final.close()

    #cleans up new.tuning
    os.remove(new.tuning)
    return 0

def promptedInput():
        while True:
                menu()
                option = input("> ")
                if option == 1:
                        setRatios()
                elif option == 2:
                        setAgeLengths()
                elif option == 3:
                        displayCurrentSettings()
                elif option == 4:
                        if (export() == 0):
                            return 0
                else:
                        print("Invalid choice.")
        return 0
        
def argumentInput(argv):
        #creates .tuning file based on .txt file passsed as an argument
        #to be implemented eventually I guess
        return 0

#Main
title = "Sims 4 Custom Age Mod Generator v.0.0.0" #version number ought to be updated every now and then I suppose
print(title)
print("By Exx\n".center(len(title)))
print("For instructions, please refer to AgeMod.md.")
##if len(sys.argv) > 1:
##      argumentInput(argv)
##else:
##      promptedInput()
##How main is going to work eventually, once passing a .txt file as an argument is implemented
promptedInput()