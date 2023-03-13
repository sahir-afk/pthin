import pyinputplus as pyip
import random
questions = pyip.inputNum("How many questions do you want?\n", max=100, greaterThan=0) 
correct=0

for i in range(questions):
    num1 = random.randint(0,12)
    num2 = random.randint(0,12)
    prompt = "What is {} X {}?\n".format(num1,num2)
    try:
        pyip.inputNum(prompt,limit=3, timeout=15, allowRegexes=[r"^%s$" % (num1*num2)], blockRegexes=[r".*", "WRONGGG!! DUMBOOOOO"])
    except pyip.TimeoutException:
        print("out of time dumbo!!!")
    except pyip.RetryLimitException:
        print("out of tries dumbo!!!")
    else:
        print("correct!")
        correct += 1

    

print("only a {}/{}? geez you suck!".format(correct, questions))