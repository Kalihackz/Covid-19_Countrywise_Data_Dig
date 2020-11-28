from bs4 import BeautifulSoup
import requests,json

url="https://www.worldometers.info/coronavirus/"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

contentTable  = soup.find('table', { "class" : "table"})

rows = contentTable.find_all('td')

dictJs={}

def getVal( country ):
    for row in range(len(rows)):
        if rows[row].get_text()==country:
            cou=rows[row].get_text()
            row = row + 1
            tot=rows[row].get_text()
            dictJs.update({cou:tot})

with open('countriesNames.txt','r') as f:
    countries=f.read().splitlines()
for country in countries:
    getVal(country)
   

out_file = open("data.json", "w")      
json.dump(dictJs, out_file, indent = 6)  
out_file.close()

