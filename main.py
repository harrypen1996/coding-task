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


        for id in array:              ##[EDIT] why loop the index and not just id???

            ## Task 1 Check
            if not (len(id) == 10 and id.isdigit() and not func.identDig(id)): #[EDIT] Condition statement for loop change
                invalid += 1
                continue           

            # Task 2 Check
            if func.wfCalc(id): #[EDIT] Condition statement for loop change        
                valid += 1
            else:
                invalid += 1

        print("Valid: ["+ str(valid) + "]")     #Print determined results
        print("Invalid: ["+str(invalid) + "]")
       

main()
