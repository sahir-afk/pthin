import webbrowser as wb
saddress = input("What address do you want to open?(#### streetname [streetdesgination], City, State) ")
saddress = saddress.replace(",", "")
address = saddress.split(" ")
sadress = "+".join(address)

url = "https://www.google.com/maps/place/" + sadress

wb.open(url)

