import re
import sys
import requests

url = "Введите страницу для поиска"

website = requests.get(url)
html = website.text

emails = re.findall(r"[\w\.-]+@[\w\.-]+", html)

print(emails)
