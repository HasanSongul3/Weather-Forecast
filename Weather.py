import requests
from bs4 import BeautifulSoup

city = input("Enter your city: ")

url = f'https://weather.com/weather/today/l/{city}'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

temp = soup.find('span', {'class': 'CurrentConditions--tempValue--3KcTQ'}).text
condition = soup.find('div', {'class': 'CurrentConditions--phraseValue--2xXSr'}).text.strip()

print(f'Temperature: {temp}')
print(f'Condition: {condition}')
