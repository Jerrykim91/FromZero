import os, glob
import pandas as pd
# 크롤링
import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote

page = "2"
choiceNum = 2
stockNumber = str(357120)

def choice(choiceNum):

    """
    1 -> 메인 , 2 -> 게시판
    """
    choiceNum = str(choiceNum)

    if choiceNum == "1":
        subject = "main"
        return(subject)
    elif choiceNum == "2":
        subject = "board"
        return(subject)

# test
mainUrl    = f'https://finance.naver.com'
subject    = choice(choiceNum)
paramUrl  = f"/item/{subject}.nhn?code={stockNumber}"
targetUrl = mainUrl + paramUrl


try:
    if page == str(1):
        req  = requests.get( targetUrl , headers={'User-Agent':'Mozilla/5.0'})
    else:
        req  = requests.get( targetUrl , headers={'User-Agent':'Mozilla/5.0'}, params = {'page': page} )
        
except:
    if page == str(1):
         req  = requests.get( targetUrl )
    else:
        req  = requests.get( targetUrl , params = {'page': page} )
        
print(req.url) 
html    = req.text
soup    = BeautifulSoup( html, 'html.parser' )