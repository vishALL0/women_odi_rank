import pandas as pd
from bs4 import BeautifulSoup
import requests
from csv import writer
url="https://www.cricbuzz.com/cricket-stats/icc-rankings/women/batting"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
name=soup.find_all('div',class_="cb-col cb-col-100 cb-font-14 cb-lst-itm text-center")

with open("odi_women.csv","w") as f:
    thewriter=writer(f)
    header=["Position","Player Name","Country","Rating"]
    thewriter.writerow(header)
    for i in name:
        player=i.find('a',class_="text-hvr-underline text-bold cb-font-16").text
        country=i.find('div',class_="cb-font-12 text-gray").text
        position=i.find('div',class_="cb-col cb-col-16 cb-rank-tbl cb-font-16").text
        rating=i.find('div',class_="cb-col cb-col-17 cb-rank-tbl pull-right").text

        ## now we create data set with the help of panad
        info=[position,player,country,rating]
        thewriter.writerow(info)
