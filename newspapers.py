from bs4 import BeautifulSoup
import requests

def getMilliyet(date):
    base="http://www.milliyet.com.tr/Milliyet.aspx?aType=GazeteResim&Date="

    page = requests.get(base+date)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.select_one("#_Middle > div > div.MG_SonDakMiddle > div > div.MG_SonDakBG > div > div.MG_galeriCont > a > img")['src']
    return img


def getSabah(date, page):
    base="http://egazete.sabah.com.tr/eGazete/image/www_sabah_com_tr/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/" + page

    return url

def getTakvim(date, page):
    base="http://egazete.takvim.com.tr/eGazete/image/www_takvim_com_tr/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/" + page

    return url

def getFotoMac(date, page):
    base="http://egazete.fotomac.com.tr/eGazete/image/www_fotomac_com_tr/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/" + page

    return url

def getDailySabah(date, page):
    base="https://www.dailysabah.com/daily-paper-image/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/" + page

    return url

def getYeniAsir(date, page):
    base="http://egazete.yeniasir.com.tr/eGazete/image/www_yeniasir_com_tr/"

    date_splited=date.split('.')
    url = base + date_splited[2] + "/" + date_splited[1] + "/" + date_splited[0] + "/" + page

    return url

def getAnadolu(date):
    base="http://www.anadolugazetesi.com/egazete/?"

    date_split = date.split('.')
    url = base + "gun=" + date_split[0] + "&ay=" + date_split[1] + "&sene=" + date_split[2]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.select_one("div.resim > img")['src']
    return "http://www.anadolugazetesi.com/" + img



def getNetgazete(id):
    base="http://gazete.netgazete.com/gazeteler.php?id="

    page = requests.get(base+id)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.select_one(".gazeteBuyukResim > a > img")['src']
    return img