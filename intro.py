from bs4 import BeautifulSoup
import requests
url = "https://realpython.com/python-web-scraping-practical-introduction/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
needed = []
t = 0
print(soup.get_text())
for link in soup.find_all('a'):
  needed.append(link.get('href'))
  if t == 3: break
  t += 1
print(needed)