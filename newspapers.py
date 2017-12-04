from bs4 import BeautifulSoup
import requests

def getMilliyet(date):
    base="http://www.milliyet.com.tr/Milliyet.aspx?aType=GazeteResim&Date="

    page = requests.get(base+date)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.select_one("#_Middle > div > div.MG_SonDakMiddle > div > div.MG_SonDakBG > div > div.MG_galeriCont > a > img")['src']
    return img


def getSabah(date):
    base="http://egazete.sabah.com.tr/eGazete/image/www_sabah_com_tr/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/1"

    return url

def getTakvim(date):
    base="http://egazete.takvim.com.tr/eGazete/image/www_takvim_com_tr/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/1"

    return url

def getFotoMac(date):
    base="http://egazete.fotomac.com.tr/eGazete/image/www_fotomac_com_tr/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/1"

    return url
