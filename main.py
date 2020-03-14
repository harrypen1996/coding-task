from modules import *

def main():
    Running = True

    while Running:
        string = input("Patient ID(s):  ")  # Input

        valid = 0     # Create int variable to contain summed (in)valid ids
        invalid = 0

        if string == "exit": # Exit application loop
            Running = False
            break

        if string == "url":  # Import URL file as array when "url" as input
            array = func.importJson()
        else:
            array = [string] # else string becomes list for loop


        for id in range(len(array)): ## indexing loop for array

            ## Task 1 Check
            if not (len(array[id]) == 10 and array[id].isdigit() and not func.identDig(array[id])):
                invalid += 1
                continue           

            # Task 2 Check
            if func.wfCalc(array[id]):
                valid += 1
            else:
                invalid += 1

        print("Valid: ["+ str(valid) + "]")     #Print determined results
        print("Invalid: ["+str(invalid) + "]")
       

main()