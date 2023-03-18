import bs4, sys
import requests as re
import webbrowser as wb

print("Searching...")
q = "+".join(sys.argv[1:])
page = re.get("https://mojeek.com/search?q=" + q)           #downloads page html

page.raise_for_status()                                         #checks if page exists
soup = bs4.BeautifulSoup(page.text, "html.parser")            #parses html of webpage 
linkElems = soup.select(".title")                          #finds all <a> elements in the yuRUbf class

numOpen = min(len(linkElems), 5)

for i in range(numOpen):                                              #opens each link in a new tab
    link = linkElems[i].get("href")
    txt = linkElems[i].getText()
    print("Opening", txt)
    wb.open(link)