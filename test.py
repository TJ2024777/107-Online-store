# JavaScript way
# create variable
# let, var or const
# let name = "Terry"

name = "Terry"
last_name = "Johnson"
age = "34"
found = False
print(name)

# if / else statements
# if(found==False)
# {
#  console.log("hello world!")
# }else if(found==True){}

if age < 100:
    print("great you're not that old")
    print("im inside of the statement")
elif age >100:    
    print("yeah seems that youre not that young anymore")
else:
    print("i dont know how you get here")    
print("im outside of the if statement")   

#function () {
#
# }

def sayHello():
    print("hello there")

sayHello()

# list .... these at the arrays
colors = ["black", "red", "green", "yellow"]
#add
colors.append("pink")
# get any element
print(colors[1])

# travel the list - for the loop
# for (i=0; i<colors.length; i++)
#{
    #let tmp=colors[i]
    #console.log(tmp)
#}

for color in colors:
    print(color)



print(colors)


# dictionary
me = {
    "firstName": "Terry",
    "lastName": "Johnson",
    "age": 34,
}
print(me)
# modify
me["age"]=99
#get the value
print(me)["firstName"]






























# create a calculator using functions.

def printMenu():
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    
    #plain instructions
    printMenu()
    opt = input("Select the option")


    number1=float(input("please give me the first number"))
    number2=float(input("please give me the second number"))

    if opt=="1":
        total= number1 + number2
        print("the total is: " + str(total))

    elif opt=="2":
        total= number1 - number2
        print("the total is: " + str(total))
    elif opt=="3":
        total= number1 * number2
        print("the total is: " + str(total)) 
    elif opt=="4":
        if number2==0:
            print("you cannot divide by zero")
        else:
            total= number1 / number2
            print("the total is: " + str(total))





