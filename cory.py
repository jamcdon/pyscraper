import schedule
import time
import requests
from bs4 import BeautifulSoup

def scrapeSite (**kwargs):
    r = requests.get('https://jokesoftheday.net/')

    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', class_='jokeContent')
    content = s.find_all('p')
    print(content)

schedule.every(2).hours.do(scrapeSite, time_period='2')

schedule.run_all()

while True:
    schedule.run_pending()
    time.sleep(120)

scrapeSite()
