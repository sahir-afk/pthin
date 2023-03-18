import requests, re, sys, bs4, random
import webbrowser as wb

# inp = sys.argv[1:]
print("Loading Page...")
query = "http://books.toscrape.com/"
cat = re.compile(r"\d{3}")
link_list = []

page = requests.get(query)

soup = bs4.BeautifulSoup(page.text, "html.parser")
links = soup.select("a")

print("book found")

for ele in links:
    link = ele.get("href")
    c = cat.search(link)
    if c != None:
        link_list.append(link)

print("Opening random book")
wb.open("http://books.toscrape.com/" + random.choice(link_list))

