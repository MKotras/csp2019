import hashlib
import base64
import random
from datetime import datetime
#Function to create the password, given the password type and the input
def convert(type, input):
    if option=="low":
        a = hashlib.sha1()
    elif option=="medium":
        a = hashlib.sha256()
    elif option=="high":
        a = hashlib.sha512()
    if randomness==True:
        a.update(str(random.randint(-10000,10000)))
        a.update(str(datetime.now()))
    a.update(input)
    a.digest()
    return base64.b64encode(a.digest())

#Continues until you select an option
option = ""
while not (option=="low" or option=="medium" or option=="high"):
    print "Low/Medium/High security?"
    option = raw_input("Input: ").lower()

#Once an option is selected
if option=="low":
    type = hashlib.sha1()
elif option=="medium":
    type = hashlib.sha256()
elif option=="high":
    type = hashlib.sha512()
#If you  enter that you want randomness, it'll add a random integer and the time to the password generation
randomness = raw_input("randomness (if you use the same word, you'll get different results)\n(y/n)? ")  == "y"


#Loops until you type done, accepts input and prints out the password generated
while True:
    input = raw_input("Input, type \"done\" when done: ")
    if input=="done":
        break
    print "Password: "
    p = convert(type, input)
    #Removes either the last character or the last 2 since they are always "=" signs
    if option=="high":
        print p[0:len(p)-2] 
    else:
        print p[0:len(p)-1]
    
