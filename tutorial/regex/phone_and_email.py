import pyperclip, re
text = str(pyperclip.paste())

phoneRegex = re.compile(r"""
(\d{3}|\(\d{3}\))   #area code
(-|\.|\s)           #dashes
(\d{3})             #numba 2
(-|\.|\s)           #dashes
(\d{4})             #last numbers
""", re.VERBOSE)

emailRegex = re.compile(r'''
    ([^@\s]+)       #username
    (@)             #@
    ([^@\s]+)       #site
    (\.[^@\s]+)     #domain
    ''', re.VERBOSE)

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[0], groups[2], groups[4]])
    matches.append(phoneNum)
    
for emails in emailRegex.findall(text):
    emailX = "".join([emails[0], emails[1],emails[2],emails[3]])
    matches.append(emailX)

if(len(matches) > 0):
    pyperclip.copy("\n".join(matches))
    print("\n".join(matches))
else:
    print(":(")