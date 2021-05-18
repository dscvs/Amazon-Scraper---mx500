import requests
from bs4 import BeautifulSoup
import smtplib
import time

url11 = 'https://www.amazon.pl/Crucial-MX500-CT1000MX500SSD1-NAND-wewn%C4%99trzny/dp/B077SF8KMG' #pln
url12 = 'https://www.amazon.pl/Crucial-Mx500-CT1000MX500SSD1-Nand-Wewn%C4%99trzny/dp/B078211KBB' #pln
url21 = 'https://www.amazon.co.uk/dp/B077SF8KMG' #funty
url22 = 'https://www.amazon.co.uk/dp/B078211KBB' #funty
url31 = 'https://www.amazon.de/dp/B077SF8KMG' #euro
url32 = 'https://www.amazon.de/dp/B078211KBB' #euro

headers = {
    "User-Agent": 'user agent'}  # my user agent


def check_price():
    page1 = requests.get(url11, headers=headers)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    price1 = soup1.find(id="priceblock_ourprice").get_text().replace(",", ".")
    convert_price = float(price1[0:6])
    if convert_price < 400:
        send_mail(url11)
    else:
        print(convert_price, 'PLN - Nie ma promocji')
        page2 = requests.get(url12, headers=headers)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        price2 = soup2.find(id="priceblock_ourprice").get_text().replace(",", ".")
        convert_price2 = float(price2[0:6])
        if convert_price2 < 400:
            send_mail(url12)
        else:
            print(convert_price2, 'PLN - Nie ma promocji')
            page3 = requests.get(url21, headers=headers)
            soup3 = BeautifulSoup(page3.content, 'html.parser')
            price3 = soup3.find(id="priceblock_ourprice").get_text().replace(",", ".")
            convert_price3 = float(price3[1:6])
            if convert_price3 < 77:
                send_mail(url21)
            else:
                print(convert_price3, '£ - Nie ma promocji')
                page4 = requests.get(url22, headers=headers)
                soup4 = BeautifulSoup(page4.content, 'html.parser')
                price4 = soup4.find(id="priceblock_ourprice").get_text().replace(",", ".")
                convert_price4 = float(price4[1:6])
                if convert_price4 < 77:
                    send_mail(url22)
                else:
                    print(convert_price4, '£ - Nie ma promocji')
                    page5 = requests.get(url31, headers=headers)
                    soup5 = BeautifulSoup(page5.content, 'html.parser')
                    price5 = soup5.find(id="priceblock_ourprice").get_text().replace(",", ".")
                    convert_price5 = float(price5[0:6])
                    if convert_price5 < 89:
                        send_mail(url31)
                    else:
                        print(convert_price5, '€ - Nie ma promocji')
                        page6 = requests.get(url32, headers=headers)
                        soup6 = BeautifulSoup(page6.content, 'html.parser')
                        price6 = soup6.find(id="priceblock_ourprice").get_text().replace(",", ".")
                        convert_price6 = float(price6[0:6])
                        if convert_price6 < 89:
                            send_mail(url32)
                        print(convert_price6, '€ - Nie ma promocji')


def send_mail(url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@gmail.com', 'password')

    subject = 'promocja'
    body = url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email sender',
        'email receiver',
        msg
    )
    print('email wysłany')

    server.quit()

if __name__ == "__main__":
    check_price()

