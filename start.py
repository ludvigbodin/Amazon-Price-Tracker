import time
import requests
from bs4 import BeautifulSoup
import messagebird

api_key = '5dJG4cUIU2mS7o82slCTsMRjO'
URL = 'https://www.amazon.com/GoPro-HERO7-Black-Waterproof-Streaming-Stabilization/dp/B07GDGZCCH/ref=sr_1_3?keywords=gopro&qid=1566756913&s=gateway&sr=8-3'

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}



def send_sms(title, price):
    client = messagebird.Client(api_key)
    try:
        msg = client.message_create('+46766526406', '+46766526406', f'Hello Ludvig, the {title} is ready to be bought! the price is {price}')
        print(msg.__dict__)
        print('sms sent')
    except messagebird.client.ErrorException as e:
        for error in e.errors:
            print(error)


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup1 = BeautifulSoup(soup.prettify(), "html.parser")


    title = soup1.find(id='productTitle').get_text().strip()
    price_value = soup1.find(id='priceblock_ourprice').get_text()

    index_of_dot = price_value.find('.')
    price = float(price_value[1:index_of_dot])

    if price > 300:
        send_sms(title, price)

while True:
    check_price()
    time.sleep(60*15)
