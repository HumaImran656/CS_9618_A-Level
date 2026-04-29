# print a message by a function
def myFunction():       #Function definition
    print ("Hello world")
myFunction()            # function call


# passing arguements to a function
# making an email ID
def nameFunction(username,domain):  #called with the same number of arguemtns 
    print (username +"@" + domain+".com")
nameFunction("imranhuma77","gmail")

# if number of arguements varies , will generate an error

#Default parameter value

def nameFunction(country="Pakistan"):  #called with the same number of arguemtns 
    print ("i am from " + country)
nameFunction("Sweden")
nameFunction("Norway")
nameFunction("Germany")
nameFunction()      # if no arguemtn then take a default value

#arbitrary afguements
#put * while giving arguements
#Subject preferences
def favSubjects(*arg):
    print("My first subjects preference is:" + arg[0])
    print("My Second subjects preference is:" + arg[1])
    print("My third subjects preference is:" + arg[2])
favSubjects("CS", "Maths", "English","Urdu")

# passing a list of arguemtns
#def myList=["CS", "Maths", "Urdu","English"]:











    
    
