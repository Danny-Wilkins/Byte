import requests
from BeautifulSoup import BeautifulSoup
import csv

url = "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp"
response = requests.get(url)
html = response.content
#print html

soup = BeautifulSoup(html)
table = soup.find("tbody", attrs={"class" : "stripe"})
#print table.prettify()

list_of_rows = []
for row in table.findAll("tr"):
    list_of_cells = []  
    for cell in row.findAll("td")[1:]:
        #print cell.text.replace("&nbsp;","")
        text = cell.text.replace("&nbsp;","")
        list_of_cells.append(text)
    #print list_of_cells
    list_of_rows.append(list_of_cells)

#print list_of_rows
outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
outfile.close()

