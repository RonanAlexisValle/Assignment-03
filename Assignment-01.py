#taking users information about apple
def boughtApple ():
    boughtapple_func = int(input("How many apples you want to buy: "))
    return boughtapple_func

#taking users information about oranges
def boughtOrange ():
    boughtorange_func = int(input("How many oranges you want to buy: "))
    return boughtorange_func

#total amount of apples and oranges
def gettotalPrice ():
    totalprice_func = ((apple*20) + (orange*25))
    return totalprice_func

def displayOutput (totalprice_func):
    print(f"Total amount is {totalprice_func}")

apple = boughtApple()
orange = boughtOrange()
totalPrice = gettotalPrice()
displayOutput (totalPrice)