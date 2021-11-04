#Step1: This will ask the user on how much money they have
def amountofMoney():
    Money = input("Amount of money you have: ")
    Money = int(Money)
    return Money

#Step2: This will ask the current price of apple
def costofApple():
    applePrice = input("How much does apple cost?: ")
    applePrice = int(applePrice)
    return applePrice

#Step3: This will calculate the total apples the money can buy
def totalApples():
    applesinTotal = userCash//applePrice
    return applesinTotal

#Step4: This will calculate the users change if there is any
def getChange():
    change = userCash%applePrice
    return change

#Step5: This will let the user know the total number of apples the money can buy as well as the change
def letuserKnow():
    print(f"You can buy {maximumBuy} apples and your change is {remainingChange} pesos.")

userCash = amountofMoney()
applePrice = costofApple()
maximumBuy = totalApples()
remainingChange = getChange()
letuserKnow()