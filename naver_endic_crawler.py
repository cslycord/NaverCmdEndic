from bs4 import BeautifulSoup
import requests

def naver_endic_crawler(text):
    url = 'http://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query='+text
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')
    target = soup.find_all('dt', attrs={'class':'first'})
    link = target[0].findAll("a")[0].get("href")
    print(link)
    url = 'http://endic.naver.com'+link
    #request again to get the meaning of the word.
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser', from_encoding='utf-8')
    target = soup.find_all('div', attrs={'class':'box_wrap1'})
    return target
