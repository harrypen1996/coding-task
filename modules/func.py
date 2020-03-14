import urllib.request as request
import json

wFactor = [11,10,9,8,7,6,5,4,3] ## Weighted array for wfCalc function

def identDig(inpt):      ## Task 1 check if all digits are identical function                  
    if all(i == inpt[0] for i in inpt):
        return True       
    else:
        return False    


def wfCalc(inpt):        ## Task 2 check digit verification using weighted array function
    wSum = []
    for i in range(len(inpt)-1): 
        wSum.append(int(inpt[i]) * wFactor[i])
    
    remainder = sum(wSum) % 12

    if remainder in {10,12}:
        return False
    
    if remainder == int(inpt[9]) or (remainder == 11 and int(inpt[9]) == 0):
        return True
    else:
        return False 

def importJson():         ## Task 3 import json file from URL function
     with request.urlopen('https://s3.amazonaws.com/cognisant-interview-resources/identifiers.json') as r:
        s = r.read()
        array = json.loads(s)
        return array

    