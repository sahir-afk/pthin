import pyinputplus as pyip
response = pyip.inputNum("enter a month ", greaterThan=0,  max = 12, blank=False, limit=3, default="N/A")
res = pyip.inputNum("enter a day ", greaterThan=0, max=31, limit=2, default="N/A")
re = pyip.inputNum("enter a number ", allowRegexes=[r"(I|V|X|L|C|M|D)", r"zero"])
odd = pyip.inputNum("enter an odd number ", default="n/a", blockRegexes=[r"[2468]$"], limit=2)

def adds_up_to_ten(numbers):
    numbersList = list(numbers)                 #converts the string numbers into a list with every character having its own index
    for i, digit in enumerate(numbersList):     #converts the string number to an int at each index i
        numbersList[i] = int(digit)

    if sum(numbersList) != 10:
        raise Exception("the digits must add up to ten idiot! Not {}".format(sum(numbersList)))
    

adds = pyip.inputCustom(adds_up_to_ten, blockRegexes=[r"10"])

