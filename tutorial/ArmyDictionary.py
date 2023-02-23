    
while(True):
    army_alphabet = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    character = input("Enter a letter to see what the army word for that letter is ")
    characterUpper = character.upper()
    if characterUpper in army_alphabet:
        print(army_alphabet[characterUpper])
    else:
        print("Invalid input. Try inputting a single letter. ")
        