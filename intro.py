from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib
from collections import deque
import re


url = "https://realpython.com/python-web-scraping-practical-introduction/"
urls = deque([url])
scraped_urls = set()
emails = set()
count = 0

try:
  while urls:
    count += 1
    if count == 100: break
    cur_url = urls.popleft()
    scraped_urls.add(cur_url)
    parts = urllib.parse.urlsplit(cur_url)
    base_url = "{0: scheme}://{0:netloc}".format(parts)
    path = url[url.rfind('./') + 1] if '/' in parts.path else url
    try:
      response = requests.get(url)
    except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):      
      continue
    new_mail = set(re.findall(r"[a-z0-9\.\-+_] + @[a-z0-9\.\-+_] + \.[a-z]+", response, re.I))
    emails.update(new_mail)
    soup = BeautifulSoup(response.text, features="lxml")
    for a in soup.find_all("a"):
      link = a.attrs['href'] if 'href' in a.attrs else ''    
      if link.startswith('/'):
        link = base_url + link
      elif not link.startswith('http'):
        link = path + link
      if not link in urls and not link in scraped_urls:
        urls.append(link)
except KeyboardInterrupt:
  print('closing')
for mail in emails:
  print(mail)