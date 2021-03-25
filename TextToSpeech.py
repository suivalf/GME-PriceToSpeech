import urllib
from urllib import request
from urllib.request import Request
from gtts import gTTS
from bs4 import BeautifulSoup
import playsound
import os
import time

while True:
    req = Request('https://www.google.com/search?q=gme&sxsrf=ALeKk00-KepoGqsoslPj8wnH_KRQdSMrfQ%3A1616689982060&ei=PrtcYOKcA5GQlwS345b4Dg&oq=gme&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjECcQnQIyBAgjECcyBAgjECcyCggAELEDEIMBEEMyCAgAELEDEIMBMgoIABDHARCjAhAKMggIABCxAxCDATIKCAAQsQMQgwEQQzIECAAQQzICCAA6BQgAELEDUOMZWMYdYJYiaABwAngBgAGxBYgBrwiSAQcwLjMuNS0xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz&ved=0ahUKEwjis97A78vvAhURyIUKHbexBe8Q4dUDCA0&uact=5', headers={'User-Agent': 'Chrome/89.0.4389.90'})
    url_contents = urllib.request.urlopen(req).read()

    soup = BeautifulSoup(url_contents, "html.parser")
    div = soup.find("div", {"id": "main"})
    result = div.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
    result = str(result)
    price = result[71:77]
    price = price.replace(",", ".")
    language = 'en'
    myobj = gTTS(text=price, lang=language, slow=False)
    myobj.save("price.mp3")
    playsound.playsound('price.mp3', True)
    os.remove("price.mp3")
    #time.sleep(10) #Uncomment this line for slower annoucments. (Or increase/decrease the value between {}

